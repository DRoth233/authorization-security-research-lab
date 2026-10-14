"""Local, dependency-free authorization research lab. Fictional data only."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Record:
    record_id: int
    owner_id: int
    note: str

RECORDS = {
    101: Record(101, 1, "Alice's fictional account note"),
    202: Record(202, 2, "Bob's fictional account note"),
}

class Forbidden(Exception):
    """Caller cannot access this record."""

class NotFound(Exception):
    """Record does not exist."""

def vulnerable_read(requester_id: int, record_id: int) -> Record:
    """INTENTIONALLY INSECURE: looks up a record without checking ownership."""
    if record_id not in RECORDS:
        raise NotFound(record_id)
    return RECORDS[record_id]

def secure_read(requester_id: int, record_id: int) -> Record:
    """Authorize on the server for every object read."""
    if record_id not in RECORDS:
        raise NotFound(record_id)
    record = RECORDS[record_id]
    if record.owner_id != requester_id:
        raise Forbidden("Access denied")
    return record

if __name__ == "__main__":
    print("Local fictional-data demonstration")
    print("Insecure: Alice can read Bob's record:", vulnerable_read(1, 202))
    try:
        secure_read(1, 202)
    except Forbidden:
        print("Secure: Alice is denied access to Bob's record")
