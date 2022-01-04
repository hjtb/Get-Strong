from flask import (
    Flask, flash, render_template,
    redirect, request, url_for
)
from flask_login import (
    LoginManager, UserMixin, login_user, login_required, logout_user, current_user
)
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from website.models import User
from flask_mongoengine.wtf import model_form
import datetime
from website.models import RegistrationForm


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    """
    login manager returns a user object and ID to login a user
    """
    user = User.objects.get(id=id)
    # if not user:
    #     user = dict(email=None, username=None, _id=None)
    return user


@app.route("/index")
def index():
    user = User(email="a", username="b", date=datetime.datetime.now)
    users = User.objects.all()
    for user in users:
        print(user.id)
    return "hello"


@app.route("/get_strong")
def get_strong():

    return "hello"


@app.route("/add_workout")
def add_workout():

    return "hello"


@app.route("/edit_user")
def edit_user():

    return "hello from edit user"


@app.route("/delete_user")
def delete_user():
    try:
        user_id = request.args.get("id")
        user = User.objects(id = user_id).first()
        username = user.username
        user.delete()
        flash(f'User {username} has been deleted!', category="success")
        return redirect(url_for('users'))
    except Exception as err:
        flash(f'Error, could not delete user error was {err}', category="error")
        return redirect(url_for('users'))

@app.route("/add_exercise")
def add_exercise():

    return "hello"


@app.route("/login")
def login():

    return "hello"


@app.route("/logout")
def logout():

    return "hello"


# Sign up Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Let new users register
    """
    if current_user.is_authenticated:
        return redirect(url_for('get_strong'))

    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        existing_user = User.objects(email = registration_form.email.data).first()
        username_taken = User.objects(username = registration_form.username.data).first()

        if existing_user or username_taken:
            flash("An account with this email/username already exists!!")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "workouts": [],
            "is_admin": True,
            "date":datetime.datetime.now
        }


        User(new_user)
        return redirect(url_for('users'))
    return render_template('register.html', registration_form=registration_form)



    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        existing_user = db.users.find_one(
            {"email": request.form.get("email").lower()})
        username_taken = db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user or username_taken:
            flash("An account with this email/username already exists!!")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "workouts": [],
            "is_admin": True,
        }

        db.users.insert_one(new_user)

        flash("Sign up Successful!")
        return redirect(url_for("get_strong"))

    return render_template("register.html", registration_form=registration_form)




@app.route("/users")
def users():
    users = User.objects.all()
    for user in users:
        print(user.email)
    return render_template('users.html', users=users, current_user=current_user)


