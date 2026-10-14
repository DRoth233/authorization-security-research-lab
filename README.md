# Authorization Security Research Lab

A reproducible **Python security learning project** demonstrating broken object-level authorization (BOLA/IDOR) and a defensive fix using fictional records.

**Scope:** Local educational simulation only. **No Xbox, Microsoft, or third-party systems were tested or compromised.**

## Research question
What happens when an application retrieves a record by a requester-supplied ID without checking whether the requester is authorized to read it?

## Method
1. Define fictional users Alice (user 1) and Bob (user 2).
2. Create records owned by each.
3. Simulate Alice requesting Bob's record (ID 202).
4. Compare an intentionally vulnerable lookup with a server-side owner check.
5. Run automated tests.

## Run locally
Requires Python 3.9+ and no third-party packages.

```bash
python lab.py
python -m unittest discover -v
```

The insecure function exposes Bob's fictional record to Alice; the secure function raises `Forbidden`.

## Findings

| Scenario | Insecure | Secure |
| --- | --- | --- |
| Alice reads her record | Allowed | Allowed |
| Alice requests Bob's record | Incorrectly allowed | Denied |
| Unknown record | Not found | Not found |

**Root cause:** Missing object-level authorization after object lookup.

**Remediation:** Compare the authenticated caller with the object's owner on the server before returning data. Apply this invariant consistently to reads and writes.

## Project files
- [lab.py](lab.py): vulnerable and corrected examples
- [test_lab.py](test_lab.py): regression tests
- [SECURITY.md](SECURITY.md): scope and responsible-use guidance

## Limitations
This is a local in-memory simulation, not a discovered real-world vulnerability, deployed API, or advanced penetration test. It makes no claim about Xbox security.

## Possible extensions
Add a local HTTP API, write/update/delete access-control tests, and a more detailed threat model.
