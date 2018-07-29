from flask import Flask, render_template
import connexion
from flask.json import jsonify
from restaurant_app.restaurants.restaurantHomePageView import restaurant_view
from restaurant_app.restaurants.restaurant_browser import launch_view
from restaurant_app.finestdiners.view import waiters_view
from restaurant_app.dishes.view import dish_menu_view
from restaurant_app.exceptions.exception_handler import handle_page_not_found_request, handle_bad_request

app = connexion.App(__name__, specification_dir='swagger/', template_folder="restaurant_app/templates")
app.add_api("restaurant_api.yml")
#app = Flask(__name__,template_folder="restaurant_app/templates")

#Register the various Blueprints
app.register_blueprint(restaurant_view)
app.register_blueprint(launch_view, template_folder="restaurant_app/templates")
app.register_blueprint(waiters_view)
app.register_blueprint(dish_menu_view)

#Regsitering error handlers
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, handle_page_not_found_request)

@app.route("/")
def get_api_response():
    return render_template("HomePage.html")

if __name__ == "__main__":
    app.run()