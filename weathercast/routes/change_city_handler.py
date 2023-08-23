#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from weathercast.config import labeler, db
from typing import Tuple
from asynctinydb import where
from vkbottle.bot import Message


@labeler.message(command=("city", 1))
async def ch_city_handler(message: Message, args: Tuple[str]):
    """
    Change city in database handler.
    """

    await db.update({"city": args[0]}, where("peer_id") == message.peer_id)
    await message.answer(message="Город изменён.")
