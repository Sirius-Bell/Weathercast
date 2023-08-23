#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import os
import sys

from asynctinydb import TinyDB
from dotenv import load_dotenv
from loguru import logger
from vkbottle import API
from vkbottle.bot import BotLabeler

load_dotenv()

VK_TOKEN: str = os.getenv('VK_TOKEN')
VK_GROUP_ID: int = int(os.getenv('VK_GROUP_ID'))
WEATHER_API_KEY: str = os.getenv('WEATHER_API_KEY')

# logger level
LEVEL: str = "DEBUG"

# database name
DB_NAME: str = "db.json"

# logging options
logger.remove()
logger.add(os.path.join("logs", "log.log"), format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: <level>{message}</level>",
           level=LEVEL, colorize=True)

db: TinyDB = TinyDB(os.path.join(os.getcwd(), DB_NAME))

api: API = API(token=VK_TOKEN)
