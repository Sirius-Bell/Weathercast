import os
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

LEVEL = "DEBUG"

logger.remove()
logger.add(os.path.join("logs", "log.log"), format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: <level>{message}</level>",
           level=LEVEL, colorize=True)
