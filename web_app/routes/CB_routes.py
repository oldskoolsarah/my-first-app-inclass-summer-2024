from flask import Blueprint, request, render_template, redirect, flash
from app.cb import load_beast_data, print_beast_data
import os

cb_routes = Blueprint("cb_routes", __name__)

load_beast_data()

@cb_routes.route("/cb_form", methods=["GET", "POST"])

def cb_form():
    print("Cassette Beasts Form.")

    df = print_beast_data()
    #data = df.to_dict("records")
    _html = df.to_html()

    # print(_html)
    print("Fetched Cassette Beasts Data!", "success")

    lookup_file = open('web_app/templates/cb_results.html', 'w+')    
    lookup_file.write(_html)
    lookup_file.close()
    lookup_file = open('web_app/templates/cb_results.html', 'r')
    sanity_check = lookup_file.read()
    # first_char = lookup_file.read(1)
    print("Sanity check starting")
    print(sanity_check)
    lookup_file.close()

    # if not first_char:
    #     print("empty file")
    #     return render_template("cb_form.html")

    print("hello")

    return render_template("cb_results.html")

        #except Exception as err:
        #    print('OOPS', err)
        #    flash("Data Error. Please check your input and try again!", "danger")
        #    return redirect("/cb_form")
        

@cb_routes.route("/cb_lookup", methods=["GET", "POST"])
def cb_lookup():
    print("Cassette Beasts Lookup Result.")

    # Parse request data and return result

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    #print("REQUEST DATA:", request_data)

    #name = request_data.get("name") or "Springheel" # get specified name or use default
    #number = request_data.get("number") or "001" # get specified number or use default
   
    try:
        #df = fetch_stocks_csv(symbol=symbol)
        df = print_beast_data()
        #data = df.to_dict("records")
        html = df.to_html()

        flash("Fetched Cassette Beasts Data!", "success")
        
        return render_template("cb_lookup.html",
            data=data
        )
    
        #return render_template("cb_lookup.html",
        #    number=number,
        #    name=name
        #)

    except Exception as err:
        print('OOPS', err)

        flash("Data Error. Please check your input and try again!", "danger")
        #return redirect("/cb_form")
    