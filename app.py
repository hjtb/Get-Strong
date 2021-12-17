import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_strong")
def get_strong():
    workouts = mongo.db.workouts.find()
    return render_template("get_strong.html", workouts=workouts)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)