#!/usr/bin/env python3
"""
Create predecessor (follows) relations between OpenProject work packages.

Covers:
  1. Summary-level P6 logic (from original schedule)
  2. Field-level sequences (conduit → wire pull, mains → drops, etc.)

Usage:
    export OP_API_KEY=20ab7d291d353479659d629e36acc538d0f5d67f8fb01fc2461db12b1532c912
    python3 import-relations.py
"""

import json
import os
import sys
import time
from pathlib import Path
from requests.auth import HTTPBasicAuth
import requests

BASE_URL   = os.environ.get("OP_URL", "http://localhost:8080")
API_KEY    = os.environ.get("OP_API_KEY", "")
MAP_PATH   = Path(__file__).parent / "wp-id-map.json"

if not API_KEY:
    print("ERROR: Set OP_API_KEY")
    sys.exit(1)

auth    = HTTPBasicAuth("apikey", API_KEY)
headers = {"Content-Type": "application/json"}

with open(MAP_PATH) as f:
    ID = json.load(f)   # activity_id → wp_id


# --- Relations as (successor, predecessor) pairs ---
# "successor follows predecessor" = finish-to-start

RELATIONS = [

    # ── Summary: Pre-construction chain ──────────────────────────────────
    ("PRE-1010", "PRE-1000"),
    ("PRE-1020", "PRE-1010"),
    ("PRE-1030", "PRE-1010"),
    ("PRE-1040", "PRE-1020"),
    ("PRE-1050", "PRE-1040"),

    # ── Summary: Procurement chain ───────────────────────────────────────
    ("PRO-2000", "PRE-1030"),
    ("PRO-2010", "PRO-2000"),
    ("PRO-2020", "PRO-2010"),
    ("PRO-2030", "PRO-2020"),
    ("PRO-2040", "PRO-2030"),

    # ── Summary: Civil ───────────────────────────────────────────────────
    ("CIV-3000", "PRO-2040"),
    ("CIV-3010", "CIV-3000"),
    ("CIV-3020", "CIV-3010"),
    ("CIV-3030", "CIV-3020"),
    ("CIV-3040", "CIV-3030"),
    ("CIV-3050", "CIV-3010"),

    # ── Summary: Structural ──────────────────────────────────────────────
    ("STR-4000", "CIV-3050"),
    ("STR-4010", "CIV-3050"),
    ("STR-4020", "STR-4000"),
    ("STR-4030", "STR-4020"),
    ("STR-4040", "STR-4030"),

    # ── Summary: MEP ─────────────────────────────────────────────────────
    ("MEP-5000", "STR-4010"),
    ("MEP-5010", "STR-4040"),
    ("MEP-5020", "MEP-5010"),
    ("MEP-5030", "STR-4040"),
    ("MEP-5040", "PRO-2010"),
    ("MEP-5050", "MEP-5040"),
    ("MEP-5060", "MEP-5010"),
    ("FP-5070",  "STR-4040"),

    # ── Summary: Fit-out ─────────────────────────────────────────────────
    ("FIT-6000", "STR-4040"),
    ("FIT-6010", "MEP-5020"),
    ("FIT-6020", "MEP-5030"),
    ("FIT-6030", "FIT-6000"),
    ("FIT-6040", "FIT-6010"),

    # ── Summary: Commissioning ───────────────────────────────────────────
    ("CXL-7000", "PRO-2010"),
    ("CXL-7010", "MEP-5040"),
    ("CXL-7020", "CXL-7010"),
    ("CXL-7030", "CXL-7020"),
    ("CXL-7040", "CXL-7030"),

    # ── Summary: Turnover ────────────────────────────────────────────────
    ("TUR-8000", "CXL-7040"),
    ("TUR-8010", "TUR-8000"),
    ("TUR-8020", "TUR-8010"),
    ("TUR-8030", "TUR-8020"),

    # ── Field: Electrical — Conduit Rough-In → Wire Pull (per hall) ──────
    ("F-MEP-5000-05", "F-MEP-5000-01"),   # Wire Pull DH1 follows Conduit DH1
    ("F-MEP-5000-06", "F-MEP-5000-02"),   # Wire Pull DH2 follows Conduit DH2
    ("F-MEP-5000-07", "F-MEP-5000-03"),   # Wire Pull DH3 follows Conduit DH3
    ("F-MEP-5000-08", "F-MEP-5000-04"),   # Wire Pull DH4 follows Conduit DH4

    # ── Field: Data Hall sequencing — DH1 → DH2 → DH3 → DH4 ────────────
    ("F-MEP-5000-02", "F-MEP-5000-01"),   # Conduit DH2 follows DH1
    ("F-MEP-5000-03", "F-MEP-5000-02"),   # Conduit DH3 follows DH2
    ("F-MEP-5000-04", "F-MEP-5000-03"),   # Conduit DH4 follows DH3

    ("F-MEP-5000-06", "F-MEP-5000-05"),   # Wire Pull DH2 follows DH1
    ("F-MEP-5000-07", "F-MEP-5000-06"),
    ("F-MEP-5000-08", "F-MEP-5000-07"),

    # ── Field: Mechanical — CHW Piping → Insulation (per MER) ───────────
    ("F-MEP-5030-03", "F-MEP-5030-01"),   # CHW Insulation MER-1 follows Piping MER-1
    ("F-MEP-5030-04", "F-MEP-5030-02"),   # CHW Insulation MER-2 follows Piping MER-2

    # ── Field: Steel — Mezzanine Framing → Equipment Platform (per MER) ─
    ("F-MEP-5030-07", "F-MEP-5030-05"),   # Equip Platform MER-1 follows Mezz MER-1
    ("F-MEP-5030-08", "F-MEP-5030-06"),   # Equip Platform MER-2 follows Mezz MER-2

    # ── Field: Generator Yard — Generator Setting → Conduit → Grounding ─
    ("F-MEP-5040-02", "F-MEP-5040-01"),   # Conduit follows Generator Setting
    ("F-MEP-5040-03", "F-MEP-5040-02"),   # Grounding follows Conduit

    # ── Field: Fuel Oil — Main Piping → Day Tank Connections ────────────
    ("F-MEP-5050-02", "F-MEP-5050-01"),

    # ── Field: Fire Protection — Mains → Drops (per hall) ───────────────
    ("F-FP-5070-05", "F-FP-5070-01"),     # Drops DH1 follows Mains DH1
    ("F-FP-5070-06", "F-FP-5070-02"),
    ("F-FP-5070-07", "F-FP-5070-03"),
    ("F-FP-5070-08", "F-FP-5070-04"),

    # ── Field: Fire Protection — DH sequencing for mains ────────────────
    ("F-FP-5070-02", "F-FP-5070-01"),
    ("F-FP-5070-03", "F-FP-5070-02"),
    ("F-FP-5070-04", "F-FP-5070-03"),

    # ── Field: Roof — Ductwork → Equipment Pad Setting ───────────────────
    ("F-STR-4020-02", "F-STR-4020-01"),

    # ── Field: Fit-out — Cable Tray → Overhead Busway (per hall) ────────
    ("F-FIT-6010-05", "F-FIT-6010-01"),   # Busway DH1 follows Cable Tray DH1
    ("F-FIT-6010-06", "F-FIT-6010-02"),
    ("F-FIT-6010-07", "F-FIT-6010-03"),
    ("F-FIT-6010-08", "F-FIT-6010-04"),

    # ── Field: Fit-out — LV Cable Tray DH sequencing ────────────────────
    ("F-FIT-6010-02", "F-FIT-6010-01"),
    ("F-FIT-6010-03", "F-FIT-6010-02"),
    ("F-FIT-6010-04", "F-FIT-6010-03"),

    # ── Field: Fit-out — Cable Tray → Fiber Backbone (per hall) ─────────
    ("F-FIT-6040-01", "F-FIT-6010-01"),   # Fiber DH1 follows Cable Tray DH1
    ("F-FIT-6040-02", "F-FIT-6010-02"),
    ("F-FIT-6040-03", "F-FIT-6010-03"),
    ("F-FIT-6040-04", "F-FIT-6010-04"),

    # ── Field: Fit-out — Fiber Backbone → Patch Panel Term (per hall) ───
    ("F-FIT-6040-05", "F-FIT-6040-01"),
    ("F-FIT-6040-06", "F-FIT-6040-02"),
    ("F-FIT-6040-07", "F-FIT-6040-03"),
    ("F-FIT-6040-08", "F-FIT-6040-04"),

    # ── Field: Fit-out — CRAH Setting → Ductwork (per hall) ─────────────
    ("F-FIT-6020-05", "F-FIT-6020-01"),   # Ductwork DH1 follows CRAH Setting DH1
    ("F-FIT-6020-06", "F-FIT-6020-02"),
    ("F-FIT-6020-07", "F-FIT-6020-03"),
    ("F-FIT-6020-08", "F-FIT-6020-04"),

    # ── Field: Fit-out — Raised Floor → Hot-Aisle Containment (per hall)
    ("F-FIT-6030-01", "F-FIT-6000-01"),
    ("F-FIT-6030-02", "F-FIT-6000-02"),
    ("F-FIT-6030-03", "F-FIT-6000-03"),
    ("F-FIT-6030-04", "F-FIT-6000-04"),
]


def create_relation(successor_id, predecessor_id):
    body = {
        "type": "follows",
        "_links": {
            "to": {"href": f"/api/v3/work_packages/{predecessor_id}"}
        }
    }
    r = requests.post(
        f"{BASE_URL}/api/v3/work_packages/{successor_id}/relations",
        json=body, auth=auth, headers=headers
    )
    if r.status_code == 422:
        # Duplicate or invalid — skip silently
        return None
    if not r.ok:
        print(f"  ERROR {r.status_code}: {r.text[:200]}")
        return None
    return r.json()


def main():
    print(f"Creating {len(RELATIONS)} relations...")
    ok = 0
    skipped = 0
    for successor_act, predecessor_act in RELATIONS:
        s_id = ID.get(successor_act)
        p_id = ID.get(predecessor_act)
        if not s_id or not p_id:
            print(f"  SKIP (missing ID): {successor_act} → {predecessor_act}")
            skipped += 1
            continue
        result = create_relation(s_id, p_id)
        if result:
            print(f"  {successor_act} [{s_id}] follows {predecessor_act} [{p_id}]")
            ok += 1
        else:
            skipped += 1
        time.sleep(0.05)

    print(f"\nDone. {ok} relations created, {skipped} skipped.")


if __name__ == "__main__":
    main()
