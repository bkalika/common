class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {"name": self.name,
                "passport_id": self.passport_id,
                "position": self.position,
                "salary": self.salary
                }
