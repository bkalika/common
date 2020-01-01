from flask import Blueprint
from flask import Response, json, request

from infrastructure import DB
from model import Restaurant

restaurant = Blueprint('restaurant', __name__)


@restaurant.route('/restaurants', methods=['GET'])
def all_restaurants():
    print(DB)
    rests = [{'name': rest.name, 'stars': rest.stars, 'id': rest.id} for rest in DB['restaurant']]
    data = json.dumps(rests)
    return Response(data, status=200)


@restaurant.route('/restaurants', methods=['POST'])
def restaurants_create():
    data = request.json
    print(data)
    DB['restaurant'].append(Restaurant("ABC", 5))
    return Response(status=200)
