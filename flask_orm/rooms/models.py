from flask_orm.db import db


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer(), unique=True, nullable=False)
    level = db.Column(db.Integer(), unique=True, nullable=False)
    status = db.Column(db.String(40), unique=True, nullable=False)
    price = db.Column(db.Float(8), unique=True, nullable=False)
