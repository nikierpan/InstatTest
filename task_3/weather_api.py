import asyncio
import json

from aiohttp import ClientSession
from typing import NamedTuple

API_TOKEN = ''

cities = ['Moscow', 'Tbilisi', 'Paris']


class Coordinate(NamedTuple):
    latitude: float
    longitude: float


async def get(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                raise f"Get response with {resp.status} status code!"


async def get_city_coordinate(city_name: str) -> Coordinate:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_TOKEN}"
    data = await get(url=url)
    return Coordinate(latitude=data[0]['lat'], longitude=data[0]['lon'])


async def get_weather_data(coor: Coordinate) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={coor.latitude}&lon={coor.longitude}" \
          f"&appid={API_TOKEN}"
    data = await get(url=url)
    return data


def create_json_file(data: dict, name: str):
    with open(f"{name}.json", "w") as file:
        json.dump(data, file)


async def make_weather_data(city: str):
    coord = await get_city_coordinate(city)
    data = await get_weather_data(coord)
    create_json_file(data, city)


async def run():
    for city in cities:
        await make_weather_data(city)


asyncio.run(run())
