#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import sys

import asyncio
from vkbottle import Bot
from config import logger, api
from routes import labelers
from middlewares import middlewares

if sys.platform.startswith('linux'):
    logger.info("Using uvloop instead of default loop.")

    import uvloop

    uvloop.install()

logger.info("Starting bot...")
bot = Bot(api=api)

for labeler in labelers:
    bot.labeler.load(labeler)

for middleware in middlewares:
    bot.labeler.message_view.register_middleware(middleware)

asyncio.run(bot.run_polling())
