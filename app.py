import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import PasswordField, Stringfield
if os.path.exists("env.py"):
    import env
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

class LoginForm(FlaskForm):
    username = Stringfield('username')
    password = PasswordField('password')

@app.route("/")
@app.route("/get_strong")
def get_strong():
    workouts = mongo.db.workouts.find()
    return render_template("get_strong.html", workouts=workouts)

@app.route("/login", methods=['GET','POST']) 
def login():
    login_form = LoginForm()
    return render_template("login.html", login_form=login_form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)