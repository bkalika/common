import json
import os
import uuid

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from products.forms import AddProduct
from utils import read_data, write_data

products = Blueprint('products', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/products')
json_file = 'products/products.json'


@products.route("/add_product", methods=["GET", "POST"])
def add_product():
    form = AddProduct()
    if form.validate_on_submit():
        image = form.image.data
        image_path = os.path.join('products/static/images', image.filename)
        image.save(image_path)
        image_url = image_path.replace('products/static/images', 'images')
        data = {
            "id": str(uuid.uuid4()),
            "name": form.name.data,
            "description": form.description.data,
            "price": form.price.data,
            "image": image_url,
        }
        all_data = json.load(open('products/products.json'))
        all_data.append(data)
        write_data(all_data, json_file)
        return redirect(url_for('products.get_products'))
    return render_template('add_product.html', form=form)


@products.route("/get_products", methods=["GET", "POST"])
def get_products():
    if request.method == "GET":
        data = read_data(json_file)
        return render_template('products.html', data=data, name_page="Products")
    elif request.method == "POST":
        return redirect(url_for('all_product?price=<price>', price=request.form.get("price")))


@products.route("/get_products/<value>", methods=["GET"])
def get_product(value):
    data = read_data(json_file)
    for product in data:
        if product.get("id") == value:
            session[value] = True
            name = product.get("name")
            description = product.get("description")
            price = product.get("price")
            image = product.get("image")
            return render_template('product.html',
                                   name=name,
                                   description=description,
                                   price=price,
                                   image=image)
