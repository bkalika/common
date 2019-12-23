class Tenant:
    def __init__(self, name, passport_id, age, sex, city, street, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = {"city": city,
                        "street": street}
        self.room_number = room_number

    def to_dict(self):
        return {"name": self.name,
                "passport_id": self.passport_id,
                "age": self.age,
                "sex": self.sex,
                "address": self.address,
                "room_number": self.room_number,
                }
