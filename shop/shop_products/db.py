# from datetime import datetime
#
# from flask_migrate import Migrate
#
# from db import db
#
# migrate = Migrate()
#
# shops_products = db.Table(
#     'shops_products',
#     db.Column('id', db.Integer, autoincrement=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
#     db.Column('shop_id', db.Integer, db.ForeignKey('shops.id'), primary_key=True),
#     db.Column('delivery_date', db.DateTime, nullable=False, default=datetime.utcnow),
#     db.Column('amount', db.Integer, nullable=False)
# )
