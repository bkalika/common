from flask_orm import db


# class Staff(db.Model):
#     __tablename__ = 'staff'
#
#     passport_id = db.Column(db.String(8), primary_key=True, unique=True)
#     name = db.Column(db.String(40), unique=False, nullable=False)
#     position = db.Column(db.String(40), unique=False, nullable=True)
#     salary = db.Column(db.Float, unique=False, nullable=True)
