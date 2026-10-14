# Security and scope

This repository is an **educational local simulation**, not a vulnerability report about Xbox, Microsoft, or any real service.

- All account identities and records are fictional.
- No external endpoints, credentials, user data, or production services are accessed.
- The intentionally insecure function is for comparison only. Do not deploy it.
- Only test systems you own or have explicit authorization to assess.
- Report real findings privately through the applicable authorized disclosure channel.

## Threat model

A caller is authenticated as fictional user 1 but supplies record ID 202, which belongs to fictional user 2. A missing object-level authorization check discloses another user's note.

## Mitigation

Authorize the requesting identity against the requested object's owner on every server-side read. Avoid trusting a client-supplied owner ID.

## Limitations

The example is an in-memory Python simulation, not a deployed API, penetration test, or discovered real-world vulnerability.
