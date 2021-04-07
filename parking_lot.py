from flask import session
from app import app
from db import db
import user


def add_new(description, price):
    user_id = user.get_id()
    if user_id != 0:
        sql = "INSERT INTO parkinglot (owner_id, reserved, who_reserved_id, description , price, time, visible) \
            VALUES (:owner_id, 0, 0, :description, :price, NOW(), :visible)"
        db.session.execute(sql, {"owner_id":user_id, "description":description, "price":price, "visible":1})
        db.session.commit()
        return True
    else:
        return False
        

def delete(id):
    try:
        sql = "UPDATE parkinglot SET visible=0 WHERE id=:park_id"
        db.session.execute(sql, {"park_id":id})
        db.session.commit()
        return True
    except:
        return False

def get_all():
    sql = "SELECT P.id, U.username, P.reserved, P.description, P.price, P.who_reserved_id \
        FROM parkinglot P, users U WHERE P.visible=1 AND owner_id = U.id ORDER BY P.time"
    return db.session.execute(sql).fetchall()

def book(id):
    user_id = user.get_id()
    try:
        sql = "UPDATE parkinglot SET reserved=1, who_reserved_id=:user_id WHERE id=:park_id"
        db.session.execute(sql, {"user_id":user_id, "park_id":id})
        db.session.commit()
        return True
    except:
        return False

def stop_using(id):
    sql = "UPDATE parkinglot SET reserved=0, who_reserved_id=0 WHERE id=:park_id"
    db.session.execute(sql, {"park_id":id})
    db.session.commit()

def get_location():
    pass

def get_comments():
    pass

def give_comment():
    pass

def give_stars():
    pass
