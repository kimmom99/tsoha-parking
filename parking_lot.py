from flask import session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import user

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

def add_new(description, price):
    user_id = user.get_id
    sql = "INSERT INTO parkinglots (owner_id, reserved, description , price) VALUES (:owner_id, :reserved, :description, :price)"
    db.session.execute(sql, {"owner_id":user_id,"reserved":0, "description": description, "price": price})
    db.session.commit()
        

def delete():
    pass

def get_parking_lot_id():
    sql = "SELECT owner_id FROM users WHERE username=:username"
    pass

def get_owner():
    pass

def book():
    pass

def is_reserved():
    pass