#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import sys

from vkbottle import Bot

from config import logger, api

if sys.platform.startswith('linux'):
    logger.info("Using uvloop instead of default loop.")

    import uvloop

    uvloop.install()

logger.info("Starting bot...")
bot = Bot(api=api)

