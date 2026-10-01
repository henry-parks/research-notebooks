# Data

`atomic_commands.csv.gz` holds 1,214 unique Windows command lines across 270 MITRE ATT&CK techniques.
The notebook trains Word2Vec on them in section 2 and measures base64 token costs on them in section 9.

| Column | Meaning |
| --- | --- |
| `technique` | MITRE ATT&CK technique ID, for example `T1059.001` |
| `executor` | how Atomic Red Team runs the test, for example `powershell` |
| `command` | the command line, collapsed to a single line |

Commands keep Atomic Red Team's `#{input_argument}` placeholders, which stop one-off paths and file
names from flooding the vocabulary.

## Source and license

From [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), copyright Red Canary, under the
MIT License. Only Windows tests are kept, deduplicated case-insensitively. The file ships here so the
numbers match the post, because a newer copy of Atomic Red Team gives slightly different numbers. To
regenerate it:

```bash
python scripts/harvest_atomic.py path/to/atomic-red-team-master.zip data/atomic_commands.csv.gz
```

## Antivirus

These are real attack commands, such as LSASS dumps and encoded PowerShell downloaders. The file is
compressed because Microsoft Defender quarantines the plain CSV. If your antivirus still flags it, add
an exclusion for this folder or regenerate the file.
