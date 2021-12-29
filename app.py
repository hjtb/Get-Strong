import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, url_for
    )
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from flask_login import (
    LoginManager, UserMixin, login_user, login_required, logout_user, current_user
    )
if os.path.exists("env.py"):
    import env
from bson.objectid import ObjectId
from forms import (LoginForm, RegistrationForm, AddExercise, AddWorkout)
from models import User 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    """
    login manager returns a user object and ID to login a user
    """
    user_obj = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if not user_obj:
        user_obj = dict(email=None,username=None,_id=None)
    print(user_id)
    return User(user_obj)


# Profile Page
@app.route("/")
@app.route("/get_strong")
@login_required
def get_strong():
    """
    Displays the users profile
    """

    username = current_user.username
    workouts = list(
        mongo.db.workouts.find({'user': current_user.username}))

    return render_template(
        "get_strong.html", workouts=workouts, username=username
        )


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
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        username_taken = mongo.db.users.find_one(
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

        mongo.db.users.insert_one(new_user)

        flash("Sign up Successful!")
        return redirect(url_for("get_strong"))
        
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
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # Check the password hash matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                flash(
                    "Login for {} was successful!".format(request.form.get("email")
                    )
                )
                loginUser = User(existing_user)
                login_user(loginUser)
                return redirect(url_for("get_strong"))
            else:
                # Username not found
                flash("Login unsuccessful!")
                return redirect(url_for("login"))
        else:
            # Username not found
            flash("Login Failed!")
            return redirect(url_for("login"))

    return render_template("login.html", login_form=login_form)


# Add Workout Page
@app.route("/add_workout")
@login_required
def add_workout():
    """
    Enables the user to enter new workouts
    """

    add_workout_form = AddWorkout()

    new_workout = {
        "workout_name": request.add_workout_form.get(
            "workout_name").lower(),
        "exercises": [],
        "comments": request.add_workout_form.get("comments"),
        "user": current_user.username
    }

    mongo.db.users.insert_one(new_workout)

    flash("Workout added successfully!")
    return redirect(url_for("workouts"))

    username = current_user.username
    
    return render_template(
        "add_workout.html",  username=username, add_workout_form=add_workout_form
        )


# Add Exercise Page
@app.route("/add_exercise", methods=['GET', 'POST'])
@login_required
def add_exercise():
    """
    page for admin user to add new exercises to database
    """
    exercises = list(mongo.db.exercises.find())
    add_exercise_form = AddExercise()

    # check if current user is_admin
    if current_user.is_admin:

        if add_exercise_form.validate_on_submit():

            # check if exercise already exists
            exercise_exists = mongo.db.exercises.find_one(
                {"exercise_name": request.form.get("exercise_name").lower()}
                )

            if exercise_exists:
                flash('Exercise already in database')
                return redirect(url_for('add_exercise'))

            exercise = {
                "exercise_name":add_exercise_form.exercise_name.data
            }

            flash("Exercise added to database")
            mongo.db.exercises.insert_one(exercise)
            return redirect(url_for("add_exercise"))

    if current_user.is_admin:
        return render_template(
            "add_exercise.html", add_exercise_form=add_exercise_form, exercises=exercises
            )

    return redirect(url_for("get_strong"))


# Logout
@app.route("/logout", methods=['GET', 'POST']) 
def logout():
    flash(f"{current_user.username} Logged out!")
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
