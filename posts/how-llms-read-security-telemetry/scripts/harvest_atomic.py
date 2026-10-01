"""Harvest Windows command lines from the Atomic Red Team repo zip -> compact CSV.

Source: https://github.com/redcanaryco/atomic-red-team (MIT license).
Run once to (re)generate the shipped corpus; the notebook only reads the CSV.
"""
import csv
import gzip
import io
import re
import sys
import zipfile
from pathlib import Path

import yaml

zip_path = Path(sys.argv[1])
out_csv = Path(sys.argv[2])

# atomics/T1059.001/T1059.001.yaml   (skip the *.md and index files)
yaml_re = re.compile(r"atomics/T[^/]+/T[^/]+\.yaml$", re.IGNORECASE)
ws_re = re.compile(r"\s+")

rows = []
seen = set()
with zipfile.ZipFile(zip_path) as z:
    names = [n for n in z.namelist() if yaml_re.search(n)]
    for name in names:
        try:
            doc = yaml.safe_load(z.read(name).decode("utf-8", "replace"))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        technique = str(doc.get("attack_technique") or "")
        for test in doc.get("atomic_tests", []) or []:
            platforms = test.get("supported_platforms") or []
            if "windows" not in [p.lower() for p in platforms]:
                continue
            ex = test.get("executor") or {}
            command = ex.get("command")
            if not command or not isinstance(command, str):
                continue
            cmd = ws_re.sub(" ", command).strip()   # collapse newlines/indent to one line
            if len(cmd) < 8:
                continue
            key = cmd.lower()
            if key in seen:
                continue
            seen.add(key)
            rows.append((technique, ex.get("name", ""), cmd))

out_csv.parent.mkdir(parents=True, exist_ok=True)
# a .gz output is written gzip-compressed (the shipped file is, so antivirus is less likely to quarantine it)
opener = gzip.open if out_csv.suffix == ".gz" else open
with opener(out_csv, "wt", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["technique", "executor", "command"])
    w.writerows(rows)

print(f"{len(rows)} unique Windows command lines -> {out_csv}")
print(f"{len({t for t, _, _ in rows})} distinct techniques")
size_kb = out_csv.stat().st_size / 1024
print(f"CSV size: {size_kb:.0f} KB")
for t, ex, c in rows[:5]:
    print(f"  {t:12s} {c[:80]}")
