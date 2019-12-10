from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Name: {self.name}, email: {self.email}, role: {self.role}"
