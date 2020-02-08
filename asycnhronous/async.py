import asyncio
import time

import aiohttp

POKEMON_API_URL = "https://pokeapi.co/api/v2/ability/{id}/"


async def get_ability(ability_id):
    async with aiohttp.ClientSession() as session:
        response = await session.get(POKEMON_API_URL.format(id=ability_id))
        return await response.json()


async def get_all_abilities():
    start = time.time()
    abilities = [await get_ability(ability_id) for ability_id in [1, 2, 3]]
    print(time.time() - start)
    print(abilities)


async def get_all_abilities_gather():
    start = time.time()
    abilities = await asyncio.gather(*[get_ability(ability_id) for ability_id in [1, 2, 3]])
    print(time.time() - start)
    print(abilities)


if __name__ == "__main__":
    asyncio.run(get_all_abilities())
    asyncio.run(get_all_abilities_gather())
