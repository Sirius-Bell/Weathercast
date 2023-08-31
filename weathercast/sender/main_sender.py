#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

import asyncio
import random

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from weather import WeatherInfo
from weathercast.config import api
from weathercast.config import db


async def sender():
    weather: WeatherInfo = WeatherInfo()

    for people in await db.all():
        if people['allow_sending']:
            data = await weather.getWeather(city=people['city'])
            mess = f"Погода сейчас: {data.current_weather_c}°C, {data.current_weather_desc}\n\nПогода на завтра: {data.next_day_weather_c}°C, {data.next_day_weather_desc}"

            await api.messages.send(peer_id=people['peer_id'], message=mess, random_id=random.randint(0, 100000))


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(sender, 'cron', minute=10, hour=11)
    scheduler.start()

    while True:
        await asyncio.sleep(1000)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
