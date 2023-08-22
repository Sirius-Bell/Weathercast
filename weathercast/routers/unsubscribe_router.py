#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle.dispatch.rules.base import PayloadRule
from vkbottle.bot import Message
from asynctinydb import where
from weathercast.config import labeler, db
from weathercast.payloads.unsub_pay import UNSUBSCRIBE_PAYLOAD


@labeler.message(PayloadRule(UNSUBSCRIBE_PAYLOAD))
async def unsub_router(message: Message) -> None:
    """
    Unsubscribe router.
    """

    await db.update({"allow_sending": False}, where("peer_id") == message.peer_id)
    await message.answer(message="Вы успешно отписаны от рассылки")
