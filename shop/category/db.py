from flask_migrate import Migrate

from db import db

migrate = Migrate()


class Category(db.Model):
    _talbename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    products = db.relationship('Product', backref='categories', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }, 200
