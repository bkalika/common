class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price

    # def __repr__(self):
    #     return "{'number': " + str(self.number) + ", 'level': " + str(
    #         self.level) + ", 'status': " + str(self.status) + ", 'price': " + str(self.price) + "}"

    def to_dict(self):
        return {"number": self.number,
                "level": self.level,
                "status": self.status,
                "price": self.price,
                }
