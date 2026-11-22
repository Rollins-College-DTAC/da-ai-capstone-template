#!/usr/bin/env python3
"""Setup-night check. Run it from the project folder:

    uv run python scripts/check_setup.py

It checks that .env exists and is filled in, that Git will NOT upload it,
and that Turso answers. It never prints a key, only whether one is present.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ["ANTHROPIC_API_KEY", "JEV_API_KEY"]
OWN = ["TURSO_DATABASE_URL", "TURSO_AUTH_TOKEN"]
LATER = ["GH_DATA_TOKEN", "GH_REVIEW_TOKEN", "REVIEWER_PASSCODE"]

problems = 0


def ok(msg):
    print(f"  OK    {msg}")


def bad(msg, fix):
    global problems
    problems += 1
    print(f"  FIX   {msg}\n        -> {fix}")


print("\n1. The .env file")
env = ROOT / ".env"
if (ROOT / ".env.txt").exists():
    bad(".env.txt found (Windows Notepad added .txt)",
        "rename it to exactly .env (turn on File name extensions in File Explorer > View)")
if not env.exists():
    bad(".env not found", "copy .env.example to .env in the project folder")
    sys.exit(1)
ok(".env exists")

from dotenv import load_dotenv  # noqa: E402

load_dotenv(env)
for name in SHARED + OWN:
    if os.getenv(name, "").strip():
        ok(f"{name} is set")
    else:
        who = "ask your instructor" if name in SHARED else "create it in Turso (see SETUP.md)"
        bad(f"{name} is empty", who)
for name in LATER:
    print(f"  later {name} {'is set' if os.getenv(name, '').strip() else '(not needed until build week)'}")

print("\n2. Git will not upload secrets")
try:
    ignored = subprocess.run(["git", "check-ignore", "-q", ".env"], cwd=ROOT).returncode == 0
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", ".env"], cwd=ROOT,
                             capture_output=True).returncode == 0
    if tracked:
        bad(".env is already committed", "stop and tell your instructor; the keys must be replaced")
    elif ignored:
        ok(".env is ignored by Git")
    else:
        bad(".env is NOT ignored", "make sure .gitignore is in the project folder and has a line: .env")
except FileNotFoundError:
    print("  skip  git command not found (GitHub Desktop users can ignore this; check that .env is not in the Changes list)")

print("\n3. Turso answers")
url, token = os.getenv("TURSO_DATABASE_URL", ""), os.getenv("TURSO_AUTH_TOKEN", "")
if url and token:
    try:
        import libsql

        conn = libsql.connect(url, auth_token=token)
        conn.execute("select 1").fetchone()
        ok("connected to Turso")
    except Exception as e:  # show the type, not the message, in case it echoes the URL
        bad(f"could not connect to Turso ({type(e).__name__})",
            "check that the URL starts with libsql:// and the token was copied in full")
else:
    print("  skip  Turso values not set yet")

print("\n" + ("All set. Commit and push in GitHub Desktop." if problems == 0
              else f"{problems} thing(s) to fix above, then run this again."))
sys.exit(1 if problems else 0)
