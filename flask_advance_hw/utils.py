import json


def read_data(path: str):
    with open(path) as file:
        return json.load(file)


def write_data(data, path):
    # try:
    #     all_data = json.load(open(path))
    # except:
    #     all_data = []
    with open(path, 'w+') as file:
        return json.dump(data, file, indent=4)
