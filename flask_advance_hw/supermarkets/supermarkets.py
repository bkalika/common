import json
import os
import uuid

from flask import Blueprint, render_template, url_for, request, session
from werkzeug.utils import redirect

from supermarkets.forms import AddSupermarket
from utils import read_data, write_data

supermarkets = Blueprint('supermarkets', __name__,
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='/supermarkets')
json_file = 'supermarkets/supermarkets.json'


@supermarkets.route('/add_supermarket', methods=["GET", "POST"])
def add_supermarket():
    form = AddSupermarket()
    if form.validate_on_submit():
        image = form.image.data
        image_path = os.path.join('supermarkets/static/images', image.filename)
        image.save(image_path)
        image_url = image_path.replace('supermarkets/static/images', 'images')
        data = {
            "id": str(uuid.uuid4()),
            "name": form.name.data,
            "location": form.location.data,
            "image": image_url,
        }
        all_data = json.load(open('supermarkets/supermarkets.json'))
        all_data.append(data)
        write_data(all_data, json_file)
        return redirect(url_for('supermarkets.get_supermarkets'))
    return render_template('add_supermarket.html', form=form)


@supermarkets.route("/get_supermarkets", methods=["GET", "POST"])
def get_supermarkets():
    if request.method == "GET":
        data = read_data(json_file)
        return render_template('supermarkets.html', data=data, name_page='Supermarkets')
    elif request.method == "POST":
        return redirect(url_for('supermarkets?location=<location>', location=request.form.get("location")))


@supermarkets.route("/get_supermarkets/<value>", methods=["GET"])
def get_supermarket(value):
    data = read_data(json_file)
    for supermarket in data:
        if supermarket.get('id') == value:
            session[value] = True
            name = supermarket.get('name')
            location = supermarket.get('location')
            image = supermarket.get('image')
            return render_template('supermarket.html', name=name, location=location, image=image)
