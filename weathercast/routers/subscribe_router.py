#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle.dispatch.rules.base import PayloadRule
from vkbottle.bot import Message
from asynctinydb import where
from weathercast.config import labeler, db
from weathercast.payloads.sub_pay import SUBSCRIBE_PAYLOAD


@labeler.message(PayloadRule(SUBSCRIBE_PAYLOAD))
async def sub_router(message: Message) -> None:
    """
    Subscribe router.
    """

    await db.update({"allow_sending": True}, where("peer_id") == message.peer_id)
    await message.answer(message="Вы успешно подписаны на рассылку")