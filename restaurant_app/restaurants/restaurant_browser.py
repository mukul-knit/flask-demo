from flask import Blueprint, render_template

launch_view = Blueprint("diners", __name__)

@launch_view.route("/diners")
def launchHomePage():
    return render_template("index.html")
