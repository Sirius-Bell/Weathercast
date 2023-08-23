#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle.bot import Message
from asynctinydb import where
from weathercast.config import labeler, db


@labeler.message(command=("sub", 0))
async def sub_handler(message: Message) -> None:
    """
    Subscribe handler.
    """

    await db.update({"allow_sending": True}, where("peer_id") == message.peer_id)
    await message.answer(message="Вы успешно подписаны на рассылку")