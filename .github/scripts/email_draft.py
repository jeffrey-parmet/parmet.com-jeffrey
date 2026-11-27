"""Create a Buttondown draft (email_summary + link) for one post file."""

import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

path = Path(sys.argv[1])
match = re.match(r"---\s*\n(.*?)\n---", path.read_text(), re.DOTALL)
if not match:
    sys.exit(f"{path}: no front matter")
fm = yaml.safe_load(match.group(1)) or {}
title = fm.get("title") or sys.exit(f"{path}: missing title")
summary = str(fm.get("email_summary") or "").strip()
if not summary:
    print(f"::warning file={path}::No email_summary; no email draft created.")
    sys.exit()

slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
url = f"https://parmet.com/jeffrey/writing/{slug}.html?ref=email-{slug}"
email = {
    "subject": title,
    "body": "".join(
        f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>"
        for p in summary.split("\n\n")
    )
    + f'<p><a href="{url}">Read the full post</a></p>',
    "status": "draft",
}
if os.environ.get("DRY_RUN"):
    print(json.dumps(email, indent=2))
    sys.exit()

req = urllib.request.Request(
    "https://api.buttondown.com/v1/emails",
    data=json.dumps(email).encode(),
    headers={
        "Authorization": f"Token {os.environ['BUTTONDOWN_API_KEY']}",
        "Content-Type": "application/json",
    },
)
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    sys.exit(f"{path}: Buttondown {e.code}: {e.read().decode()}")
print(f"Draft created: {title}")
