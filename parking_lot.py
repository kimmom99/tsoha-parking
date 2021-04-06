from flask import session
from app import app
from db import db
import user


def add_new(description, price):
    user_id = user.get_id()
    if user_id != 0:
        sql = "INSERT INTO parkinglots (owner_id, reserved, description , price, visible) VALUES (:owner_id, :reserved, :description, :price, :visible)"
        db.session.execute(sql, {"owner_id":user_id, "reserved":0, "description":description, "price":price, "visible":1})
        db.session.commit()
        return True
    else:
        return False
        

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