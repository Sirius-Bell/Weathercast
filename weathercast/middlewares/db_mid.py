#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from asynctinydb import where
from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from weathercast.config import db


class DatabaseCheck(BaseMiddleware[Message]):

    async def pre(self):
        if not await db.search(where('peer_id') == self.event.peer_id):
            await db.insert({'id': self.event.id, 'peer_id': self.event.peer_id, 'name': self.event.get_user(),
                             'allow_sending': True, "city": "Астрахань"})
