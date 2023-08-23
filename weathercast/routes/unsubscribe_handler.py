#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle.bot import Message
from asynctinydb import where
from weathercast.config import labeler, db


@labeler.message(command=("unsub", 0))
async def unsub_handler(message: Message) -> None:
    """
    Unsubscribe handler.
    """

    await db.update({"allow_sending": False}, where("peer_id") == message.peer_id)
    await message.answer(message="Вы успешно отписаны от рассылки")
