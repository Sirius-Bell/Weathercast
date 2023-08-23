#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from asynctinydb import where
from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from weathercast.config import db
from asynctinydb import Query
from loguru import logger


class DatabaseCheck(BaseMiddleware[Message]):

    async def pre(self):
        if not await db.search(Query().peer_id == self.event.peer_id):
            await db.insert({'id': self.event.id, 'peer_id': self.event.peer_id,
                             'allow_sending': True, "city": "Астрахань"})
