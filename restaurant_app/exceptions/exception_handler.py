from flask import render_template


def handle_bad_request(e):
    return render_template("400.html")


def handle_page_not_found_request(e):
    return render_template("404.html")

