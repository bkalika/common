from flask_migrate import Migrate

from db import db

migrate = Migrate()


class Shop(db.Model):
    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    city = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    owner = db.Column(db.String(60), nullable=False)

    def __init__(self, city, name, owner):
        self.city = city
        self.name = name
        self.owner = owner

    def __repr__(self):
        return f'Shop {self.name}, owner: {self.owner}, located in {self.city}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
                   "city": self.city,
                   "name": self.name,
                   "owner": self.owner
               }, 200

    @classmethod
    def find_shop_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()
