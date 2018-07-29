import json
import os
from flask import jsonify, Blueprint
from flask.views import View, MethodView

dish_menu_view = Blueprint("menu", __name__)

def load_dishes():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.abspath(current_dir + "/../static/menu.json")
    with open(file_path, mode='r') as f:
        json_data = json.load(f)
        return json_data

DISH_DATA = load_dishes()


def load_dish_data():
    category_name_list, sub_menu_items_list = list(), list()
    if DISH_DATA:
        for each_category in DISH_DATA.get("categories"):
            category_name_list.append(each_category.get("name"))
            for each_menu_item in each_category.get("menu-items"):
                sub_menu_items_list.append(each_menu_item.get("name"))
    return category_name_list, sub_menu_items_list


class DishData(View):

    methods = ["GET", "OPTIONS"]

    category_data, sub_meu_items = load_dish_data()


class CategoryView(DishData):

    def dispatch_request(self):
        return jsonify(self.category_data)


class SubMenuView(DishData):

    def dispatch_request(self):
        return jsonify(self.sub_meu_items)


class CategoryWiseDishView(MethodView):

    cache = dict()

    def get(self, category_id):
        if category_id:
            if category_id and self.cache.get("category_cache") and category_id in self.cache.get("category_cache"):
                return jsonify(self.cache.get("category_cache").get(category_id))
            else:
                self.init_category_data()
                if category_id in self.cache.get("category_cache"):
                    return jsonify(self.cache.get("category_cache").get(category_id))

    def init_category_data(self):
        if DISH_DATA:
            category_data = {each_category.get("id"): each_category for each_category in DISH_DATA.get("categories")}
            self.cache["category_cache"] = category_data
            result_dict = dict()
            for each_category in DISH_DATA.get("categories"):
                category_wise_dict = dict()
                category_wise_dict["name"] = each_category.get("name")
                category_wise_dict["dishes"] = list()
                for each_menu_item in each_category.get("menu-items"):
                    category_wise_dict["dishes"].append(each_menu_item.get("name"))
                result_dict[each_category.get("id")] = category_wise_dict
            self.cache["category_cache_succint"] = result_dict


dish_menu_view.add_url_rule("/menu/categories", view_func=CategoryView.as_view("categories"))
dish_menu_view.add_url_rule("/menu/dishes", view_func=SubMenuView.as_view("dishes"))
dish_menu_view.add_url_rule("/menu/categories/<category_id>", view_func=CategoryWiseDishView.as_view("categories/category_id"))
