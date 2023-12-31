#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import aiohttp

from weathercast.config import WEATHER_API_KEY, logger
from weathercast.models.weather_model import Weather


class WeatherInfo:
    """
    Class for getting weather
    """

    def __init__(self):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    async def getWeather(self, city: str) -> Weather:
        """
        Simple getting weather with parsing to dataclass Weather
        """
        async with self.session.get(f"https://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=2&lang=ru") as resp:
            return await self._parse(await resp.json())

    async def _parse(self, data: dict) -> Weather:
        logger.debug(f"Get full info, parse...: {data}")
        return Weather(
            city=data['location']['name'],
            current_weather_c=data['current']['temp_c'],
            current_weather_desc=data['current']['condition']['text'],
            next_day_weather_c=data['forecast']['forecastday'][1]['day']['avgtemp_c'],
            next_day_weather_desc=data['forecast']['forecastday'][1]['day']['condition']['text'],
            sunrise=data['forecast']['forecastday'][1]['astro']['sunrise'],
            sunset=data['forecast']['forecastday'][1]['astro']['sunset']
        )
