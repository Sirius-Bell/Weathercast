#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle.bot import Message
from asynctinydb import where
from vkbottle.framework.labeler import BotLabeler

from weathercast.config import db

lb: BotLabeler = BotLabeler()


@lb.message(command=("unsub", 0))
async def unsub_handler(message: Message) -> None:
    """
    Unsubscribe handler.
    """

    await db.update({"allow_sending": False}, where("peer_id") == message.peer_id)
    await message.answer(message="Вы успешно отписаны от рассылки")
