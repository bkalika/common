from flask_migrate import Migrate

from db import db
from shop_products.db import shops_products

migrate = Migrate()


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    shop = db.Column(db.String, nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    image = db.Column(db.String, nullable=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    shops = db.relationship('Shop', secondary=shops_products, backref='shops')

    def __init__(self, name, price, category, shop, description, image=None):
        self.name = name,
        self.price = price
        self.category = category
        self.shop = shop
        self.description = description
        self.image = image

    def __repr__(self):
        return f'Product {self.name}, cost {self.price}, on the shop {self.shop}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_product_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def json(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "shop": self.shop,
            "description": self.description,
            "image": self.image,
        }
