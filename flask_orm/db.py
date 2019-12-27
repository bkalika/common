from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

rooms_staff = db.Table(
    'rooms_staff',
    db.Column('staff_id', db.String(8), db.ForeignKey('staff.passport_id'), primary_key=True),
    db.Column('room_id', db.Integer, db.ForeignKey('rooms.number'), primary_key=True)
)


class Room(db.Model):
    __tablename__ = 'rooms'

    number = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.String(40), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    tenant_id = db.Column(db.String(8), db.ForeignKey('tenants.passport_id'), nullable=True)


class Tenant(db.Model):
    __tablename__ = 'tenants'

    passport_id = db.Column(db.String(8), primary_key=True, unique=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    sex = db.Column(db.String(10), unique=False, nullable=True)
    city = db.Column(db.String(100), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)
    rooms = db.relationship('Room', backref='tenant')


class Staff(db.Model):
    __tablename__ = 'staff'

    passport_id = db.Column(db.String(8), primary_key=True, unique=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    position = db.Column(db.String(40), unique=False, nullable=True)
    salary = db.Column(db.Float, unique=False, nullable=True)
    rooms = db.relationship('Room', secondary=rooms_staff, backref='rooms')
