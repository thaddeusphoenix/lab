#!/usr/bin/env python3
"""
Import expanded hyperscale DC schedule into OpenProject.

Usage:
    export OP_API_KEY=your_api_key_here
    export OP_PROJECT_ID=1          # numeric project ID from the URL
    python3 import-schedule.py

Find your project ID: open the project in OpenProject, look at the URL —
    http://localhost:8080/projects/your-project-name
Then hit the API: http://localhost:8080/api/v3/projects to get the numeric ID.

Generate an API key: My Account → Access Tokens → Generate.
"""

import csv
import json
import os
import sys
import time
from pathlib import Path
from requests.auth import HTTPBasicAuth
import requests

# --- Config ---
BASE_URL = os.environ.get("OP_URL", "http://localhost:8080")
API_KEY  = os.environ.get("OP_API_KEY", "")
PROJECT_ID = os.environ.get("OP_PROJECT_ID", "")

CSV_PATH = Path(__file__).parent.parent.parent / "projects/handoff/discover/schedule-expanded.csv"

if not API_KEY:
    print("ERROR: Set OP_API_KEY environment variable.")
    sys.exit(1)
if not PROJECT_ID:
    print("ERROR: Set OP_PROJECT_ID environment variable (numeric project ID).")
    sys.exit(1)

auth    = HTTPBasicAuth("apikey", API_KEY)
headers = {"Content-Type": "application/json"}

PROJECT_HREF = f"/api/v3/projects/{PROJECT_ID}"


# --- API helpers ---

def api_get(path):
    r = requests.get(f"{BASE_URL}/api/v3{path}", auth=auth, headers=headers)
    r.raise_for_status()
    return r.json()


def api_post(path, body):
    r = requests.post(f"{BASE_URL}/api/v3{path}", json=body, auth=auth, headers=headers)
    if not r.ok:
        print(f"  ERROR {r.status_code}: {r.text[:300]}")
        r.raise_for_status()
    return r.json()


def get_type_href(types, preferred="Task"):
    """Return the API href for a work package type by name."""
    for t in types:
        if t["name"] == preferred:
            return t["_links"]["self"]["href"]
    # Fallback to first available type
    return types[0]["_links"]["self"]["href"]


def get_status_href(statuses, preferred="New"):
    for s in statuses:
        if s["name"] == preferred:
            return s["_links"]["self"]["href"]
    return statuses[0]["_links"]["self"]["href"]


# --- Load schedule ---

def load_schedule():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# --- Build description ---

def build_description(row):
    """Embed trade, area, and activity ID in description for NL matching context."""
    parts = []
    if row["Area"]:
        parts.append(f"Area: {row['Area']}")
    if row["Trade"]:
        parts.append(f"Trade: {row['Trade']}")
    if row["Resource"]:
        parts.append(f"Resource: {row['Resource']}")
    parts.append(f"Activity ID: {row['Activity_ID']}")
    parts.append(f"WBS: {row['WBS_Code']}")
    return "\n".join(parts)


# --- Create a work package ---

def create_wp(subject, description, type_href, status_href, parent_wp_id=None):
    body = {
        "subject": subject,
        "description": {
            "format": "plain",
            "raw": description
        },
        "_links": {
            "project": {"href": PROJECT_HREF},
            "type":    {"href": type_href},
            "status":  {"href": status_href}
        }
    }
    if parent_wp_id:
        body["_links"]["parent"] = {"href": f"/api/v3/work_packages/{parent_wp_id}"}

    result = api_post("/work_packages", body)
    return result["id"]


# --- Main ---

def main():
    print(f"Connecting to {BASE_URL} ...")

    # Verify project exists
    try:
        project = api_get(f"/projects/{PROJECT_ID}")
        print(f"Project found: {project['name']} (id={PROJECT_ID})")
    except Exception as e:
        print(f"ERROR: Could not find project {PROJECT_ID}. Check OP_PROJECT_ID.")
        print(f"  List your projects: {BASE_URL}/api/v3/projects")
        sys.exit(1)

    # Get available types and statuses
    types    = api_get(f"/projects/{PROJECT_ID}/types")["_embedded"]["elements"]
    statuses = api_get("/statuses")["_embedded"]["elements"]

    task_href      = get_type_href(types, "Task")
    milestone_href = get_type_href(types, "Milestone")
    status_href    = get_status_href(statuses, "New")

    print(f"Using type 'Task' → {task_href}")
    print(f"Using status 'New' → {status_href}")

    rows = load_schedule()
    print(f"Loaded {len(rows)} activities from CSV.")

    # Map activity_id → OpenProject work package id
    wp_id_map = {}

    # Pass 1: create summary and milestone activities (no parent dependency)
    print("\n--- Pass 1: Summary & milestone activities ---")
    for row in rows:
        if row["Level"] not in ("summary", "milestone"):
            continue
        type_href = milestone_href if row["Level"] == "milestone" else task_href
        subject   = row["Activity_Name"]
        desc      = build_description(row)
        try:
            wp_id = create_wp(subject, desc, type_href, status_href)
            wp_id_map[row["Activity_ID"]] = wp_id
            print(f"  [{wp_id}] {row['Activity_ID']} — {subject}")
            time.sleep(0.1)  # be polite to the local server
        except Exception as e:
            print(f"  SKIP {row['Activity_ID']}: {e}")

    # Pass 2: create field-level activities with parent references
    print("\n--- Pass 2: Field-level activities ---")
    skipped = []
    for row in rows:
        if row["Level"] != "field":
            continue
        parent_activity_id = row["Parent_Activity_ID"]
        parent_wp_id = wp_id_map.get(parent_activity_id)
        if not parent_wp_id:
            print(f"  WARN: Parent {parent_activity_id} not found for {row['Activity_ID']} — creating without parent")

        subject = row["Activity_Name"]
        desc    = build_description(row)
        try:
            wp_id = create_wp(subject, desc, task_href, status_href, parent_wp_id)
            wp_id_map[row["Activity_ID"]] = wp_id
            print(f"  [{wp_id}] {row['Activity_ID']} — {subject}")
            time.sleep(0.1)
        except Exception as e:
            print(f"  SKIP {row['Activity_ID']}: {e}")
            skipped.append(row["Activity_ID"])

    # Write ID map for reference
    map_path = Path(__file__).parent / "wp-id-map.json"
    with open(map_path, "w") as f:
        json.dump(wp_id_map, f, indent=2)

    print(f"\nDone. {len(wp_id_map)} work packages created.")
    if skipped:
        print(f"Skipped: {skipped}")
    print(f"ID map written to: {map_path}")


if __name__ == "__main__":
    main()
