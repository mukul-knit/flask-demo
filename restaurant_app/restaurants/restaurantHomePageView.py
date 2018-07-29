from flask import Blueprint, request
from flask.json import jsonify

restaurant_view = Blueprint("restaurants", __name__, url_prefix="/api")

_RESTAURANTS = {
    1: {"name": "China Town",
        "rating": 1}, 2: {"name": "Beer yani !!!!", "rating": 2}
}


@restaurant_view.route("/restaurants")
def get_restaurant_names():
    return jsonify([val.get("name") for val in _RESTAURANTS.values()])


@restaurant_view.route("/restaurants/<int:restaurant_id>")
def get_restaurant_int(restaurant_id):
    return jsonify(_RESTAURANTS.get(restaurant_id))


@restaurant_view.route("/restaurants/<string:restaurant_id>")
def get_restaurant(restaurant_id):
    return jsonify(_RESTAURANTS.get(restaurant_id))


@restaurant_view.route("/restaurants", methods=["POST", "OPTIONS"])
def add_restaurant():
    _RESTAURANTS[3] = request.get_json(force=True)
    return jsonify("Restaurant created")


@restaurant_view.route("/restaurants/<int:restaurant_id>", methods=["PUT", "OPTIONS"])
def update_restaurant(restaurant_id):
    restaurant_data = _RESTAURANTS.get(restaurant_id)
    if restaurant_data:
        restaurant_data.update(request.get_json(force=True))
    _RESTAURANTS[restaurant_id] = restaurant_data
    return jsonify("Restaurant updated " + str(restaurant_data))


@restaurant_view.route("/restaurants/<int:restaurant_id>", methods=["Delete", "OPTIONS"])
def delete_restaurant(restaurant_id):
    restaurant_data = _RESTAURANTS.pop(restaurant_id, None)
    return jsonify("Restaurant deleted successfully " + str(restaurant_data))

