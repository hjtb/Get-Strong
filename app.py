import os
from flask import (
    Flask, flash, session, render_template,
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
        user_obj = dict(email=None, username=None, _id=None)
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
    #global_exercises = list(mongo.db.exercises.exercise_name.find())
    #session["global_exercises"] = global_exercises
    if login_form.validate_on_submit():
        # Check for existing user in DB
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # Check the password hash matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                flash(
                    f"Login for {existing_user['username']} was successful!".format(request.form.get("email")
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
@app.route("/add_workout", methods=['GET', 'POST'])
@login_required
def add_workout():
    """
    Enables the user to enter new workouts
    """
    
    username = current_user.username
    user_workouts_names = []
    user_workouts = list(
        mongo.db.workouts.find({'user': current_user.username}))
    for user_workout in user_workouts:
        user_workouts_names.append(user_workout["workout_name"])
    
    print(user_workouts_names)

    # Is this add or edit workout
    workout_name = request.args.get("workout_name")

    if workout_name:
        # Check for workout in url args to see if we're editing an existing workout
        workout = mongo.db.workouts.find_one({ user: username, workout: workout_name.lower()})

    else:
        workout = dict(workout_name="", exercises=[], comments="", user=username)

    # One way or another, we now have a workout
    add_workout_form = AddWorkout()

    # retrieve the exercises from the db and set them as our choices in the SelectField in our form
    db_list_exercises = list(mongo.db.exercises.find())
    add_workout_form.exercise_name.choices = [
        ( exercise["exercise_name"].lower(), exercise["exercise_name"].title()) for exercise in db_list_exercises
        ]

    if add_workout_form.validate_on_submit():
        new_workout = {}
        new_workout['workout_name'] = request.form['workout_name'].lower()
        new_workout['comments'] = request.form['comments']
        new_workout["user"] = username

        # Check if this workout already exists
        workout_already_exists = request.form['workout_name'].lower() in (user_workouts_names)

        if workout_already_exists:
            exercises = list(mongo.db.workouts.find_one(
                {"workout_name": request.form['workout_name'].lower()}
            ))
        else:
            exercises = []

        exercise_row = {
                 "exercise_name": add_workout_form.exercise_name.data,
                 "sets": add_workout_form.sets.data,
                 "reps": add_workout_form.reps.data,
                 "weight": add_workout_form.weight.data
            }

        exercises.append(exercise_row)

        #Add exercises to the new workout dict
        new_workout["exercises"] = exercises

        # We are updating an existing workout
        mongo.db.workouts.replace_one(dict(name=new_workout["workout_name"]), new_workout, upsert=True)

        flash(f"Workout {new_workout['workout_name']} added successfully!")
        return redirect(url_for("add_workout"))

    return render_template(
        "add_workout.html", username=username,
        add_workout_form=add_workout_form
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
                {"exercise_name": request.form.get("exercise_name")}
            )

            if exercise_exists:
                flash('Exercise already in database')
                return redirect(url_for('add_exercise'))

            exercise = {
                "exercise_name": add_exercise_form.exercise_name.data
            }

            flash(f"{exercise['exercise_name']} added to database")
            mongo.db.exercises.insert_one(exercise)
            return redirect(url_for("add_exercise"))

    if current_user.is_admin:
        return render_template(
            "add_exercise.html", add_exercise_form=add_exercise_form,
            exercises=exercises
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
