#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import sys

import asyncio
from vkbottle import Bot
from config import logger, api, labeler
from middlewares import middlewares

if sys.platform.startswith('linux'):
    logger.info("Using uvloop instead of default loop.")

    import uvloop

    uvloop.install()

logger.info("Starting bot...")
bot = Bot(api=api)

bot.labeler.load(labeler)

for middleware in middlewares:
    bot.labeler.message_view.register_middleware(middleware)

asyncio.run(bot.run_polling())
