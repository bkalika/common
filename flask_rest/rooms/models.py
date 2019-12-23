class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price

    def to_dict(self):
        return {"number": self.number,
                "level": self.level,
                "status": self.status,
                "price": self.price,
                }
