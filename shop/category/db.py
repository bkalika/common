from flask_migrate import Migrate

from db import db

migrate = Migrate()


class Category(db.Model):
    _talbename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    products = db.relationship('Products', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
