from flask import Flask, render_template
from app import app
from flask import redirect, render_template, request, session
import user
import parking_lot


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username,password):
            return redirect("/home")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/new_user")
def new_user():
    return render_template("create.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.create(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Tilin luonti ei onnistunut")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")

@app.route("/add_parkinglot")
def add_parkinglot():
    return render_template("new_park.html")

@app.route("/new_park", methods=["POST"])
def new_park():
    description = request.form["description"]
    price = request.form["price"]
    if parking_lot.add_new(description, price):
        return redirect("/home")
    else:
        return render_template("error.html", message="Parkkipaikan lisäys ei onnistunut")

@app.route("/home")
def home():
    return render_template('home.html', lots = user.get_own_parking_lots())

@app.route("/delete_parking_lot", methods=["POST"])
def delete_parking_lot():
    pass

@app.route("/book", methods=["POST"])
def book_parking_lot():
    pass
