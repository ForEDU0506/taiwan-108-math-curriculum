r"""Create the HAICoWork Chat channel in ClickUp.

Usage (PowerShell):
    $env:CLICKUP_API_TOKEN = "pk_..."              # never commit or paste the token
    python tools\clickup_create_channel.py          # dry run
    python tools\clickup_create_channel.py --apply  # create the channel

ClickUp returns the existing channel if one with the same name already exists.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.clickup.com/api"
NAME = "HAICoWork"
DESCRIPTION = "HAIC 團隊會議室"


def call(token, method, path, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={"Authorization": token, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} failed: HTTP {e.code} {e.read().decode('utf-8', 'replace')}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--workspace-id")
    parser.add_argument("--visibility", choices=["PUBLIC", "PRIVATE"], default="PUBLIC")
    args = parser.parse_args()

    token = os.environ.get("CLICKUP_API_TOKEN")
    if not token:
        sys.exit("Set CLICKUP_API_TOKEN first (ClickUp > Settings > Apps > API Token).")

    teams = call(token, "GET", "/v2/team")["teams"]
    if args.workspace_id:
        teams = [t for t in teams if t["id"] == args.workspace_id]
    if len(teams) != 1:
        choices = ", ".join(f'{t["id"]}={t["name"]}' for t in teams)
        sys.exit(f"Pick one with --workspace-id. Available: {choices}")
    ws = teams[0]["id"]
    print(f"Workspace: {teams[0]['name']} ({ws})")
    print(f"+ Chat channel: {NAME} ({args.visibility})")
    if not args.apply:
        print("Dry run only. Re-run with --apply to create.")
        return

    result = call(
        token,
        "POST",
        f"/v3/workspaces/{ws}/chat/channels",
        {"name": NAME, "description": DESCRIPTION, "visibility": args.visibility},
    )
    channel = result.get("data", result)
    print(f"Done. Channel id: {channel.get('id')}")


if __name__ == "__main__":
    main()
