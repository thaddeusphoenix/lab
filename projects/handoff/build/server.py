#!/usr/bin/env python3
"""
Handoff matching server.
Bridges the foreman chat UI → NL matching → OpenProject work packages.
Learns from Superintendent approve/correct decisions via match-rules.json.

Usage:
    pip install flask requests
    python3 server.py
    open http://localhost:5001
"""

import json, os, re, time, uuid
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import requests as http
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file
from requests.auth import HTTPBasicAuth

load_dotenv()

app      = Flask(__name__)
HERE     = Path(__file__).parent
OP_URL   = 'http://localhost:8080'
OP_KEY   = os.environ['OP_API_KEY']
OP_PROJ  = '3'
AUTH     = HTTPBasicAuth('apikey', OP_KEY)
RULES    = HERE / 'match-rules.json'
PHONE_MAP      = HERE / 'phone-map.json'
TWILIO_SID     = os.environ['TWILIO_SID']
TWILIO_TOKEN   = os.environ['TWILIO_TOKEN']
TWILIO_FROM    = '+18339588253'

FOREMEN = [
    {'id':'f1','name':'Marcus T.', 'trade':'Electrical'},
    {'id':'f2','name':'Rosa V.',   'trade':'Mechanical'},
    {'id':'f3','name':'Tomas R.',  'trade':'Fire Protection'},
    {'id':'f4','name':'Aisha K.',  'trade':'Low Voltage'},
    {'id':'f5','name':'Devon K.',  'trade':'Plumbing'},
    {'id':'f6','name':'Priya S.',  'trade':'Steel'},
    {'id':'f7','name':'Yuki O.',   'trade':'Controls'},
]

# In-memory queue of SMS-sourced pending matches
sms_queue = []

# ── Alias tables ──────────────────────────────────────────────────────────────

AREA_ALIASES = {
    'Data Hall 1':    ['hall 1','hall one','dh1','hall a','east hall','east side','a side','a hall'],
    'Data Hall 2':    ['hall 2','hall two','dh2','hall b','west hall','west side','b side','b hall'],
    'Data Hall 3':    ['hall 3','hall three','dh3','hall c'],
    'Data Hall 4':    ['hall 4','hall four','dh4','hall d'],
    'MER-1':          ['mer 1','mer-1','mer1','north mer','north mechanical','mechanical room north'],
    'MER-2':          ['mer 2','mer-2','mer2','south mer','south mechanical','b side mechanical'],
    'ESR':            ['esr','switchgear room','gear room','electrical room','switch room'],
    'Generator Yard': ['gen yard','generator yard','generator area','the yard','gen area'],
    'Roof':           ['roof','rooftop','up top','penthouse'],
    'UPS Room':       ['ups room','ups'],
}

TRADE_ALIASES = {
    'Electrical':      ['electrical','electric','conduit','wire pull','wiring','pipe bending',
                        'elec','lighting','switchgear','panel','busway','home run','pulling wire'],
    'Mechanical':      ['mechanical','mech','hvac','chw','chilled water','duct','ductwork',
                        'crah','cooling','mep','chiller'],
    'Low Voltage':     ['low voltage','lv','low volt','cable tray','tray','fiber','data cabling',
                        'running tray','pulling fiber'],
    'Fire Protection': ['fire','sprinkler','suppression','fire protection','drops','mains',
                        'heads','clean agent','wet pipe'],
    'Plumbing':        ['plumbing','drain','domestic','sanitary','drain work'],
    'Steel':           ['steel','structural','iron','framing','mezzanine','platform',
                        'welding','iron work'],
    'Controls':        ['controls','bas','bms','automation','sensors','sensor','control wiring'],
    'Finishes':        ['raised floor','floor','containment','hot aisle','hot-aisle','rack'],
}

# ── WP cache ──────────────────────────────────────────────────────────────────

_cache = {'wps': None, 'ts': 0}

def fetch_wps(force=False):
    if not force and _cache['wps'] and time.time() - _cache['ts'] < 120:
        return _cache['wps']
    r = http.get(
        f'{OP_URL}/api/v3/projects/{OP_PROJ}/work_packages',
        params={'pageSize': 500},
        auth=AUTH
    )
    r.raise_for_status()
    wps = []
    for el in r.json().get('_embedded', {}).get('elements', []):
        # Field-level WPs have a parent; skip summary/milestone activities
        if not el.get('_links', {}).get('parent', {}).get('href'):
            continue
        desc   = el.get('description', {}).get('raw', '')
        area   = next((l.split('Area:')[1].strip()        for l in desc.split('\n') if l.startswith('Area:')), '')
        trade  = next((l.split('Trade:')[1].strip()       for l in desc.split('\n') if l.startswith('Trade:')), '')
        act_id = next((l.split('Activity ID:')[1].strip() for l in desc.split('\n') if l.startswith('Activity ID:')), '')
        wps.append({
            'id': el['id'], 'subject': el['subject'],
            'area': area, 'trade': trade, 'activity_id': act_id,
            'pct': el.get('percentageDone', 0),
            'lockVersion': el.get('lockVersion', 0),
        })
    _cache['wps'] = wps
    _cache['ts']  = time.time()
    return wps

# ── Rules ─────────────────────────────────────────────────────────────────────

def load_rules():
    return json.loads(RULES.read_text()) if RULES.exists() else []

def save_rules(rules):
    RULES.write_text(json.dumps(rules, indent=2))

# ── Matching ──────────────────────────────────────────────────────────────────

def tokenize(text):
    return set(re.sub(r'[^a-z0-9\s]', ' ', text.lower()).split()) - {'the','a','an','is','are','in','on','at','and','of','to','we','it'}

def extract_pct(text):
    t = text.lower()
    m = re.search(r'(\d+)\s*(?:percent|%)', t)
    if m: return int(m.group(1))
    fractions = [
        ('three quarter', 75), ('two third', 67), ('four fifth', 80), ('one third', 33),
        ('halfway', 50), ('half', 50), ('quarter', 25),
    ]
    for phrase, val in fractions:
        if phrase in t: return val
    verbal = [
        ('done', 100), ('complete', 100), ('finished', 100), ('wrapped up', 95),
        ('buttoned up', 90), ('almost done', 90), ('basically done', 92),
        ('mostly done', 80), ('mostly complete', 80), ('far along', 70),
        ('good progress', 60), ('past halfway', 55), ('just started', 10),
        ('broke ground', 5), ("haven't touched", 0), ('not started', 0),
        ('a third', 33), ('one third', 33),
    ]
    for phrase, val in verbal:
        if phrase in t: return val
    return None

MATCH_PROMPT = """\
You are a construction schedule assistant on a hyperscale data center build.
A foreman has sent a plain-language progress update via SMS. Match it to the
correct work package in the schedule.

Foreman: {foreman_name} ({foreman_trade})
Message: "{message}"

Work packages (ID | Name | Trade | Area):
{wp_list}

Past Superintendent decisions — learn from these patterns:
{examples}

Instructions:
- Match based on meaning, not exact keywords. "rough-in" means electrical conduit work.
  "MEP" covers mechanical/electrical/plumbing. "the yard" likely means Generator Yard.
- If the foreman's trade strongly implies a work package with no other signal, use it.
- proposed_pct: extract a completion percentage from the message (0–100), or null if none.
- confidence: 0–100. Use 90+ only when zone, trade, and context all align clearly.
- If no work package is a reasonable match, return null for wp_id.
- Return up to 2 alternatives when the match is ambiguous.

Return ONLY valid JSON — no prose, no markdown:
{{
  "wp_id": <integer or null>,
  "confidence": <0-100>,
  "proposed_pct": <0-100 or null>,
  "reasoning": "<one sentence>",
  "alternatives": [
    {{"wp_id": <integer>, "reasoning": "<brief>"}}
  ]
}}
"""

def match_message(message, foreman_id=''):
    wps      = fetch_wps()
    rules    = load_rules()
    foreman  = next((f for f in FOREMEN if f['id'] == foreman_id), {})

    wp_list = '\n'.join(
        f"  {wp['id']} | {wp['subject']} | {wp['trade']} | {wp['area']}"
        for wp in wps
    )

    # Use last 15 decisions as few-shot examples
    recent = rules[-15:] if rules else []
    example_lines = []
    for r in recent:
        if r['type'] == 'confirm':
            example_lines.append(f"  CONFIRMED: \"{r['message']}\" → WP {r['wp_id']} ({r.get('wp_name','')})")
        elif r['type'] == 'correct':
            example_lines.append(f"  CORRECTED: \"{r['message']}\" → WP {r['wp_id']} ({r.get('wp_name','')}), not WP {r.get('original_wp_id','?')}")
    examples = '\n'.join(example_lines) if example_lines else '  None yet.'

    prompt = MATCH_PROMPT.format(
        foreman_name=foreman.get('name', foreman_id),
        foreman_trade=foreman.get('trade', 'unknown'),
        message=message,
        wp_list=wp_list,
        examples=examples,
    )

    try:
        client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
        response = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=512,
            messages=[{'role': 'user', 'content': prompt}],
        )
        raw = response.content[0].text.strip()
        # Strip markdown fences if present
        if raw.startswith('```'):
            raw = re.sub(r'^```[^\n]*\n?', '', raw).rstrip('`').strip()
        result = json.loads(raw)
    except Exception as e:
        print(f'[LLM match error] {e}')
        return []

    valid_ids = {wp['id'] for wp in wps}
    matches = []

    if result.get('wp_id') and result['wp_id'] in valid_ids:
        top_wp = next(w for w in wps if w['id'] == result['wp_id'])
        matches.append({
            **top_wp,
            'score':        result.get('confidence', 80),
            'confidence':   result.get('confidence', 80),
            'proposed_pct': result.get('proposed_pct') or extract_pct(message),
            'reasoning':    result.get('reasoning', ''),
        })

    for alt in result.get('alternatives', []):
        if alt.get('wp_id') and alt['wp_id'] in valid_ids:
            alt_wp = next(w for w in wps if w['id'] == alt['wp_id'])
            matches.append({
                **alt_wp,
                'score':        max(0, result.get('confidence', 80) - 20),
                'confidence':   max(0, result.get('confidence', 80) - 20),
                'proposed_pct': result.get('proposed_pct') or extract_pct(message),
                'reasoning':    alt.get('reasoning', ''),
            })

    return matches

# ── OpenProject update ────────────────────────────────────────────────────────

def update_wp(wp_id, pct, foreman_name='', message=''):
    r = http.get(f'{OP_URL}/api/v3/work_packages/{wp_id}', auth=AUTH)
    r.raise_for_status()
    wp      = r.json()
    lock    = wp.get('lockVersion', 0)
    current_status = wp.get('_links', {}).get('status', {}).get('href', '')

    body = {'lockVersion': lock}
    if pct is not None:
        body['percentageDone'] = pct
    # Move to In Progress if currently New
    if 'statuses/1' in current_status:
        body['_links'] = {'status': {'href': '/api/v3/statuses/7'}}

    resp = http.patch(
        f'{OP_URL}/api/v3/work_packages/{wp_id}',
        json=body, auth=AUTH,
        headers={'Content-Type': 'application/json'}
    )
    resp.raise_for_status()

    # Post foreman message as a comment
    if message:
        label  = f'**{foreman_name}:** ' if foreman_name else ''
        note   = f'{label}{message}'
        if pct is not None:
            note += f'\n\n*Superintendent approved — {pct}% complete.*'
        else:
            note += '\n\n*Superintendent acknowledged.*'
        http.post(
            f'{OP_URL}/api/v3/work_packages/{wp_id}/activities',
            json={'comment': {'format': 'markdown', 'raw': note}},
            auth=AUTH,
            headers={'Content-Type': 'application/json'}
        )

    _cache['ts'] = 0  # invalidate cache

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return send_file(HERE / 'app.html')

@app.route('/api/work_packages')
def api_wps():
    return jsonify(fetch_wps())

@app.route('/api/match', methods=['POST'])
def api_match():
    body = request.json
    matches = match_message(body['message'], body.get('foreman_id', ''))
    return jsonify({'matches': matches, 'proposed_pct': extract_pct(body['message'])})

@app.route('/api/decision', methods=['POST'])
def api_decision():
    body = request.json
    wp_id = body['wp_id']
    pct   = body.get('pct')
    msg   = body['message']

    foreman_name = body.get('foreman_name', '')
    try:
        update_wp(wp_id, pct, foreman_name=foreman_name, message=msg)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    rules  = load_rules()
    tokens = list(tokenize(msg))

    # Increment count if a matching confirm rule already exists
    if body['type'] == 'confirm':
        for rule in rules:
            if rule['wp_id'] == wp_id and rule['type'] == 'confirm':
                if len(set(rule['tokens']) & set(tokens)) >= 2:
                    rule['count'] = rule.get('count', 1) + 1
                    rule['last_seen'] = datetime.now(timezone.utc).isoformat()
                    save_rules(rules)
                    return jsonify({'ok': True, 'rules_count': len(rules)})

    entry = {
        'id':         str(uuid.uuid4())[:8],
        'timestamp':  datetime.now(timezone.utc).isoformat(),
        'type':       body['type'],
        'message':    msg,
        'tokens':     tokens,
        'foreman_id': body.get('foreman_id', ''),
        'wp_id':      wp_id,
        'wp_name':    body.get('wp_name', ''),
        'pct':        pct,
        'count':      1,
    }
    if body['type'] == 'correct':
        entry['original_wp_id']   = body.get('original_wp_id')
        entry['original_wp_name'] = body.get('original_wp_name')

    rules.append(entry)
    save_rules(rules)
    return jsonify({'ok': True, 'rules_count': len(rules)})

@app.route('/api/rules')
def api_rules():
    return jsonify(load_rules())

# ── SMS webhook (Twilio) ──────────────────────────────────────────────────────

def load_phone_map():
    return json.loads(PHONE_MAP.read_text()) if PHONE_MAP.exists() else {}

def build_clarification_sms(message):
    tokens  = tokenize(message)
    msg_low = message.lower()
    has_area  = any(a in msg_low for aliases in AREA_ALIASES.values() for a in aliases)
    has_trade = any(a in msg_low for aliases in TRADE_ALIASES.values() for a in aliases)
    parts = []
    if not has_area:  parts.append('which area (e.g. Hall A, MER-1, Gen Yard)')
    if not has_trade: parts.append('which trade (e.g. electrical, mechanical, fire)')
    if not parts:     parts.append('which specific work package')
    return 'Can you clarify ' + ' and '.join(parts) + '?'

@app.route('/sms', methods=['POST'])
def sms_webhook():
    try:
        from twilio.twiml.messaging_response import MessagingResponse
    except ImportError:
        return 'twilio not installed — run: pip3 install twilio', 500

    from_number = request.form.get('From', '').strip()
    body        = request.form.get('Body', '').strip()
    resp        = MessagingResponse()

    phone_map  = load_phone_map()
    foreman_id = phone_map.get(from_number)

    if not foreman_id:
        resp.message("Your number isn't registered on this project. Contact your Superintendent.")
        return str(resp), 200, {'Content-Type': 'text/xml'}

    foreman = next((f for f in FOREMEN if f['id'] == foreman_id), None)
    matches = match_message(body, foreman_id)

    entry = {
        'id':            str(uuid.uuid4())[:8],
        'timestamp':     datetime.now(timezone.utc).isoformat(),
        'source':        'sms',
        'from_number':   from_number,
        'foreman_id':    foreman_id,
        'foreman_name':  foreman['name']  if foreman else from_number,
        'foreman_trade': foreman['trade'] if foreman else '',
        'message':       body,
        'matches':       matches,
        'resolved':      False,
    }
    sms_queue.append(entry)

    if matches:
        first = foreman['name'].split()[0] if foreman else 'there'
        resp.message(f"Got it {first} — update received and queued for Superintendent review.")
    else:
        resp.message(build_clarification_sms(body))

    return str(resp), 200, {'Content-Type': 'text/xml'}

@app.route('/api/sms/queue')
def api_sms_queue():
    return jsonify([e for e in sms_queue if not e['resolved']])

@app.route('/api/sms/<entry_id>/resolve', methods=['POST'])
def api_sms_resolve(entry_id):
    for e in sms_queue:
        if e['id'] == entry_id:
            e['resolved'] = True
            break
    return jsonify({'ok': True})

if __name__ == '__main__':
    print('Handoff matching server → http://localhost:5001')
    app.run(port=5001, debug=True)
