import sys

from vkbottle import Bot

from config import logger, api

if sys.platform.startswith('linux'):
    logger.info("Using uvloop instead of default loop.")

    import uvloop

    uvloop.install()

logger.info("Starting bot...")
bot = Bot(api=api)
