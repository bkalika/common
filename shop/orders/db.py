from datetime import datetime

from flask_migrate import Migrate

from db import db


migrate = Migrate()


# orders = db.Table(
#     'orders',
#     db.Column('id', db.Integer, primary_key=True, autoincrement=True),
#     db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow)
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
# )

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime, nullable=True)
    is_closed = db.Column(db.Boolean, default=False)
    is_processed = db.Column(db.Boolean, default=False)
    name = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f'Order {self.id}, created_at: {self.created_at}, closed_at: {self.closed_at}, name: {self.name}'
