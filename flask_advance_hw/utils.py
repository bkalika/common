import json


def read_data(path: str):
    with open(path) as file:
        return json.load(file)


def write_data(data: str, path: str):
    with open(path, 'w+') as write_file:
        return json.dump(data, write_file, indent=4)
