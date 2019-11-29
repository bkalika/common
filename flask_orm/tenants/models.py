from flask_orm import db


class Tenant(db.Model):
    __tablename__ = 'tenants'

    passport_id = db.Column(db.String(8), primary_key=True, unique=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    sex = db.Column(db.String(10), unique=False, nullable=True)
    city = db.Column(db.String(100), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)
    tenants = db.relationship('Room', backref='tenant')
