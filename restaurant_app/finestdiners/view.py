from flask import Blueprint, request, render_template
from diner import Diner

waiters_view = Blueprint("finestdiners", __name__)
DINERS_LIST_TEMPLATE = "finestdiners.tmpl"


def populate_diners():
    diners = list()
    for i in range(20):
        d = Diner(diner_name= "Restaurant" + str(i), diner_city= "City" + str(i) , diner_rating= i)
        diners.append(d)
    return diners

def get_best_diners():
    diners = populate_diners()
    best_diners = [each_diner for each_diner in diners if each_diner.rating <11 ]
    return best_diners

@waiters_view.context_processor
def get_worst_diners():
    diners = populate_diners()
    worst_diners = [each_diner for each_diner in diners if each_diner.rating > 11]
    return dict(worst_diners = worst_diners, diner_type = "worse_diners")

@waiters_view.route("/finestdiners")
def list_finest_diners():
    return render_template(DINERS_LIST_TEMPLATE, finest_diners = get_best_diners())


@waiters_view.route("/worstdiners")
def list_worst_diners():
    return render_template(DINERS_LIST_TEMPLATE)