import uuid


class Restaurant:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        self.id = str(uuid.uuid4())


class Table:
    def __init__(self, number, guests_count):
        self.number = number
        self.guests_count = guests_count
        self.id = uuid.uuid4()
