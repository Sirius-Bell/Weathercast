from dataclasses import dataclass


@dataclass
class User:
    id: int
    peer_id: int
    name: str
    allow_sending: bool = False
