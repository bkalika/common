from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

film_studio = db.Table(
    "film_studio",
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('studio_id', db.Integer, db.ForeignKey('studios.id'))
)


class Films(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.String)
    studio_id = db.relationship(db.ForeignKey('studios.id'))


class Studios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    films = db.relationship('Films', secondaty=film_studio, backref='studio')


