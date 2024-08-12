
from flask import Blueprint, request, render_template, redirect, flash
from app.cb import load_beast_data, print_beast_data

cb_routes = Blueprint("cb_routes", __name__)

load_beast_data()

@cb_routes.route("/cb_form", methods=["GET", "POST"])

def cb_form():
    print("Cassette Beasts Form.")

    if request.method == "GET":

        return render_template("cb_form.html")
    
    if request.method == "POST":
        
        try:
            df = print_beast_data()
        #data = df.to_dict("records")
            html = df.to_html()

            print.html

            flash("Fetched Cassette Beasts Data!", "success")
        
            return render_template("cb_lookup.html",
                data=data
            )

        except Exception as err:
            print('OOPS', err)
            flash("Data Error. Please check your input and try again!", "danger")
            return redirect("/cb_form")
        



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
    