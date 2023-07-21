import aiohttp

from config import WEATHER_API_KEY
from models.weather_model import Weather


class WeatherInfo:
    """
    Class for getting weather
    """

    def __init__(self):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.params: dict = {
            'key': WEATHER_API_KEY,
            'days': 2
        }

    async def getWeather(self, city) -> Weather:
        self.params.update({'city': city})
        async with self.session.get("https://api.weatherapi.com/v1/forecast.json", json=self.params) as resp:
            return await self._parse(await resp.json())

    async def _parse(self, data) -> Weather:
        pass
