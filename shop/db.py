from flask import session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

ACCESS = {
    "guest": 0,
    "user": 1,
    "admin": 2,
}


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String(20), nullable=False)

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }, 200

    def __repr__(self):
        return f"Name: {self.name}, email: {self.email}, role: {self.role}"

    @classmethod
    def find_user_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def is_admin(self):
        return self.access == ACCESS['admin']

    def allowed(self, access_level):
        return self.access >= access_level

    @classmethod
    def profile(cls, email):
        get_email = session.get('email')
        if not get_email:
            return {"User not authorised!"}
        user = cls.query.filter_by(email=email).first()
        return {"msg": f"User {user} authorised"}



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
        return f'Shop {self.name} who is owner {self.owner}, located in {self.city}'

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


shops_products = db.Table(
    'shops_products',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('shop_id', db.Integer, db.ForeignKey('shops.id'), primary_key=True)
)

users_products = db.Table(
    'users_products',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    shop = db.Column(db.String, nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    image = db.Column(db.String, nullable=True)
    shops = db.relationship('Shop', secondary=shops_products, backref='shops')
    users = db.relationship('User', secondary=users_products, backref='users')

    def __init__(self, name, price, category, shop, description, image=None):
        self.name = name,
        self.price = price
        self.category = category
        self.shop = shop
        self.description = description
        self.image = image

    def __repr__(self):
        return f'Product {self.name}, cost {self.price}, can buy in shop {self.shop}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_product_by_id(cls, id):
        return cls.query.filter_by(id=id).all()

    def json(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "shop": self.shop,
            "description": self.description,
            "image": self.image,
        }
