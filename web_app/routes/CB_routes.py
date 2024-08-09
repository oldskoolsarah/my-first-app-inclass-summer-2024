
from flask import Blueprint, request, render_template, redirect, flash

cb_lookup = Blueprint("cb_lookup", __name__)


@cb_lookup.route("/cb_lookup")
def stocks_form():
    print("Cassette Beasts Lookup...")
    return render_template("cb_lookup.html")