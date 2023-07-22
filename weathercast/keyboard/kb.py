#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from vkbottle import Keyboard, Text

from weathercast.payloads.ch_city_pay import CHANGE_CITY_PAYLOAD
from weathercast.payloads.sub_pay import SUBSCRIBE_PAYLOAD
from weathercast.payloads.unsub_pay import UNSUBSCRIBE_PAYLOAD

KEYBOARD = (
    Keyboard(one_time=True, inline=True)
    .add(Text("Сменить город", payload=CHANGE_CITY_PAYLOAD))
    .add(Text("Подписаться", payload=SUBSCRIBE_PAYLOAD))
    .add(Text("Отписаться", payload=UNSUBSCRIBE_PAYLOAD))
).get_json()
