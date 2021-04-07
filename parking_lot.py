from flask import session
from app import app
from db import db
import user


def add_new(description, price):
    user_id = user.get_id()
    if user_id != 0:
        sql = "INSERT INTO parkinglot (owner_id, reserved, description , price, visible) VALUES (:owner_id, :reserved, :description, :price, :visible)"
        db.session.execute(sql, {"owner_id":user_id, "reserved":0, "description":description, "price":price, "visible":1})
        db.session.commit()
        return True
    else:
        return False
        

def delete(id):
    pass

def get_location():
    pass

def get_comments():
    pass

def give_comment():
    pass

def give_stars():
    pass
