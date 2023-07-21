from dataclasses import dataclass


@dataclass
class Weather:
    city: str
    current_weather_c: int
    current_weather_desc: str
    next_day_weather_c: int
    next_day_weather_desc: str
