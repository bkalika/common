import time

from requests import get


def get_ability(ability_id):
    response = get(f"https://pokeapi.co/api/v2/ability/{ability_id}/")
    return response.json()


if __name__ == "__main__":
    start = time.time()
    abilities = [get_ability(ability_id) for ability_id in [1, 2, 3]]
    print(time.time() - start)
    print(abilities)
