#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from dataclasses import dataclass


@dataclass
class User:
    """
    User model for database(without using this dataclass)
    Represents user in id, peer_id, name, allow_sending
    """
    id: int
    peer_id: int
    name: str
    allow_sending: bool = True
    city: str = "Астрахань"
