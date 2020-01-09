from flask_restful import Resource, abort, marshal_with
from sqlalchemy import func

from db import db
from shop_products.structures import products_in_shop
from shops.db import Shop
from products.db import Product, ShopProduct
from shop_products.parser import shop_product_parser


class ShopProductView(Resource):
    @marshal_with(products_in_shop)
    def get(self, shop_id):
        shop = Shop.query.filter_by(id=shop_id).first_or_404()
        return shop.products

    def post(self, shop_id):
        get_shop = shop_id
        data = shop_product_parser.parse_args(strict=True)
        product_id = Product.query.filter_by(id=data["product_id"]).first_or_404()
        products_amount_in_shop = db.session.query(func.sum(ShopProduct.amount).label('sum')).filter_by(product_id=data['product_id'], shop_id=shop_id).scalar()
        if products_amount_in_shop > 10:
            return {"message": f"Products with id {data.get('product_id')} too much in shop with id {shop_id}"}
        elif shop_id and product_id:
            deliver_product = ShopProduct(shop_id=get_shop, product_id=data.get('product_id'), amount=data.get('amount'))
            db.session.add(deliver_product)
            db.session.commit()
            return {"message": "Successfully delivered!"}
        abort(404, message=f'Shops with id {data["shop_id"]} or product with id {data["product_id"]} was not found!')
