import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
    )
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import PasswordField, StringField, IntegerField, EmailField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, AnyOf, Email
if os.path.exists("env.py"):
    import env
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
    def __init__(self, user_json):
        self.user_json = user_json
        self.username = user_json.get('username')
        self.library = user_json.get('library')
        self.is_admin = user_json.get('is_admin')

    def get_id(self):
        object_id = self.user_json.get("_id")
        return str(object_id)



@login_manager.user_loader
def load_user(user_id):
    """
    login manager returns a user object and ID to login a user
    """
    user_obj = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    return User(user_obj)


class RegistrationForm(FlaskForm):
    """
    Registration form class for our registration page
    """
    email = EmailField('Email', validators=[InputRequired(),
    Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
    Length(min=6, max=30)])


class LoginForm(FlaskForm):
    """
    Login form class for our login page
    """
    email = EmailField('Email', validators=[InputRequired(),
    Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
    Length(min=6, max=30)])


# Profile Page
@app.route("/")
@app.route("/get_strong/<email>")
@login_required
def get_strong(email):
    """
    Displays the users profile
    """
    email = mongo.db.users.find_one({"email": session["user"]})["email"]
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    workouts = mongo.db.workouts.find({"workouts": session["user"]})["workouts"]
    return render_template("get_strong.html", workouts=workouts, email=email, username=username)


# Sign up Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Let new users to register
    """
    if current_user.is_authenticated:
        return redirect(url_for('get_strong'))
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        existing_user = mongo.db.users.find_one({"email": request.form.get("email").lower()})
        username_taken = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        if existing_user or username_taken:
            flash("An account with this email/username already exists!!")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "workouts": [],
            "is_admin": False
        }
        mongo.db.users.insert_one(new_user)

        session["user"] = request.form.get("email").lower()
        flash("Sign up Successful!")
        return redirect(url_for("get_strong", email=session["user"]))
        
    return render_template("register.html", registration_form=registration_form)


# Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Log users in
    """
    if current_user.is_authenticated:
        return redirect(url_for('get_strong'))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        # Check for existing user in DB
        existing_user = mongo.db.users.find_one({"email": request.form.get("email").lower()})

        if existing_user:
            # Check the password hash matches
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Login for {} was successful!".format(request.form.get("email")))
                loginUser = User(existing_user)
                login_user(loginUser)
                return redirect(url_for("get_strong", email=session["user"]))
        else:
            # Username not found
            flash("Login Failed!")
            return redirect(url_for("login"))

    return render_template("login.html", login_form=login_form)

# Logout
@app.route("/logout", methods=['GET', 'POST']) 
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
