from dataclasses import dataclass


@dataclass
class Weather:
    """
    Weather model
    Represents weather in city, current_weather, next_day_weather
    """
    city: str
    current_weather_c: int
    current_weather_desc: str
    next_day_weather_c: int
    next_day_weather_desc: str
