from dataclasses import dataclass


@dataclass
class User:
    """
    User model.
    Represents user in id, peer_id, name, allow_sending
    """
    id: int
    peer_id: int
    name: str
    allow_sending: bool = False
