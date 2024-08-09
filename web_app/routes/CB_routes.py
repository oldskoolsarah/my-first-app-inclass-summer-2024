
from flask import Blueprint, request, render_template, redirect, flash

cb_routes = Blueprint("cb_routes", __name__)

@cb_routes.route("/cb_form")
def cb_form():
    print("Cassette Beasts Form.")
    return render_template("cb_form.html")

@cb_routes.route("/cb_lookup", methods=["GET", "POST"])
def cb_lookup():
    print("Cassette Beasts Lookup.")
    # Parse request data and return result
    return render_template("cb_lookup.html")
    