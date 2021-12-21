import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
    )
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, AnyOf, Email
if os.path.exists("env.py"):
    import env
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


class RegistrationForm(FlaskForm):
    """Registration form class for our registration page"""
    email = EmailField('Email', validators=[InputRequired(),
    Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
    Length(min=6, max=30)])


class LoginForm(FlaskForm):
    """Login form class for our login page"""
    email = EmailField('Email', validators=[InputRequired(),
    Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
    Length(min=6, max=30), AnyOf(values=['password', 'secret'])])


@app.route("/")
@app.route("/get_strong")
def get_strong():
    workouts = mongo.db.workouts.find()
    return render_template("get_strong.html", workouts=workouts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        existing_user = mongo.db.users.find_one({"email": request.form.get("email").lower()})
        return 'Email: {}.  Password: {}.'.format(registration_form.email.data, registration_form.password.data)
        if existing_user:
            flash("An account with this email already exists, please login")
            return redirect(url_for("login"))
    return render_template("register.html", registration_form=registration_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return 'Email: {}.  Password: {}.'.format(login_form.email.data, login_form.password.data)
    return render_template("login.html", login_form=login_form)


@app.route("/logout", methods=['GET', 'POST']) 
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
