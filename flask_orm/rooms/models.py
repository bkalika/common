from flask_orm.db import db


class Room(db.Model):
    __tablename__ = 'rooms'

    number = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(40), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    tenant_id = db.Column(db.String(8), db.ForeignKey('tenant.passport_id'), nullable=False)
