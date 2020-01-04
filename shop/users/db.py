from flask import session
from flask_migrate import Migrate

from db import db

migrate = Migrate()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String(20), nullable=False)
    orders = db.relationship('Order', backref='users', lazy=True)

    ACCESS = {
        "guest": 0,
        "user": 1,
        "admin": 2,
    }

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
        return self.access == self.ACCESS['admin']

    def allowed(self, access_level):
        return self.access >= access_level

    @classmethod
    def profile(cls, email):
        get_email = session.get('email')
        if not get_email:
            return {"User not authorised!"}
        user = cls.query.filter_by(email=email).first()
        return {"msg": f"User {user} authorised"}
