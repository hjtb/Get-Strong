from flask import (
    flash, render_template,
    redirect, request, url_for
)
from wtforms import ValidationError
from flask_login import (
    LoginManager, login_user, login_required, logout_user, current_user
)
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import LogExercise, User, SelectExercise, Workout
import datetime
from website.forms import RegistrationForm, LoginForm, AddExerciseForm, AddWorkoutForm


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    """
    login manager returns a user object and ID to login a user
    """

    user = User.objects(id=id).first()

  
    return user


@app.route("/landing")
def index():

    return "hello"


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

        )

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
        flash("You're already registered")
        return redirect(url_for('get_strong'))

    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        existing_user = User.objects().filter(email = registration_form.email.data.strip().lower()).first()
        username_taken = User.objects().filter(username = registration_form.username.data.strip().lower()).first()

        if existing_user:
            flash("An account with this email already exists!! Log in!")
            return redirect(url_for("login"))

        if username_taken:
            flash("An account with this username already exists!!")
            return redirect(url_for("register"))

        username= request.form.get("username").lower().strip()
        email= request.form.get("email").lower().strip()
        password= generate_password_hash(request.form.get("password"))
        workouts= []
        date=datetime.datetime.now


        user = User(username=username, email=email, password=password, workouts=workouts, date=date)
        saved = user.save()
        if saved:
            flash("Sign up Successful!")
            login_user(saved)
            return redirect(url_for('users'))
    return render_template('register.html', registration_form=registration_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Let Users login
    """
    if current_user.is_authenticated:
        flash("You're already logged in")
        return redirect(url_for('get_strong'))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        # Check for existing user in DB
        existing_user = User.objects().filter(email = login_form.email.data.strip().lower()).first()

        if existing_user:
            # Check the password hash matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                flash(
                    f"Login for {existing_user['username']} was successful!".format(request.form.get("email")
                    )
                )
                login_user(existing_user)
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


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    flash(f"{current_user.username} Logged out!")
    logout_user()
    return redirect(url_for("login"))

# Users page for admins to manage the users
@app.route("/users")
def users():
    """
    Page for an admin to manage users.
    """
    users = User.objects.all()
    for user in users:
        print(user.email)
    return render_template('users.html', users=users, current_user=current_user)


# Edit user functionality
@app.route("/edit_user", methods=['GET', 'POST'])
def edit_user():
    """
    Page for an admin to edit and delete users.
    """
    try:
        # Get the user email we clicked on from the users page and retrieve the user data from the db
        user_id = request.args.get("id")
        user_to_be_edited = User.objects(id = user_id).first()

    except Exception as err:
        # Flash our error message if we can't retrieve the data and return to the users page
        flash(f'Error, could not edit user error was {err}', category="error")
        return redirect(url_for('users'))

    # Use our registration form template
    edit_user_form = RegistrationForm()

    # Run the validation check on the submitted form but not as a condition
    valid = edit_user_form.validate_on_submit()

    # Now our form is submitted
    if request.method=="POST":
        try:
            # Get the user email we clicked on from the users page and retrieve the user data from the db
            user_id = request.args.get("id")
            user_to_be_edited = User.objects(id = user_id).first()

        except Exception as err:
            # Flash our error message if we can't retrieve the data and return to the users page
            flash(f'Error, could not edit user error was {err}', category="error")
            return redirect(url_for('users'))

        # Get our data from the edit user form
        form_username = edit_user_form.username.data
        form_email = edit_user_form.email.data

        # Check for existing emails/usernames
        existing_email = User.objects().filter(email = form_email.strip().lower()).first()
        existing_username = User.objects().filter(username = form_username.strip().lower()).first()
        
        # Check if the email has been updated
        if form_email == user_to_be_edited.email:
            email = user_to_be_edited.email

        # Check for existing emails
        elif existing_email:
                flash("An account with this email already exists!!")
                return redirect(url_for('edit_user', id=user_id))
        
        # If both checks pass we can update our users email
        else:
            email = form_email

        # Check if the username has been updated
        if form_username == user_to_be_edited.username:
            username = user_to_be_edited.username

        # Check for existing usernames
        elif existing_username:
                flash("An account with this username already exists!!")
                return redirect(url_for('edit_user', id=user_id))

        # If both checks pass we can update our users email
        else:
            username = form_username

        # Check if a new password was entered
        if edit_user_form.password.data:
            password_plaintext = edit_user_form.password.data
            if len(password_plaintext) > 8 and len(password_plaintext) < 30:
                password= generate_password_hash(password_plaintext)
        else:
            password = user_to_be_edited.password

        user_to_be_edited.update(username=username, email=email, password=password)

        flash(f'User {username} with email {email} has been updated!', category="success")
        return redirect(url_for('users'))

    edit_user_form.password.validators = []
    print(edit_user_form.errors)
    return render_template('edit_user.html', user_to_be_edited=user_to_be_edited, current_user=current_user, edit_user_form=edit_user_form)


@app.route("/delete_user")
def delete_user():
    try:
        user_email = request.args.get("email")
        user = User.objects(email = user_email).first()
        username = user.username
        user.delete()
        flash(f'User {username} has been deleted!', category="success")
        return redirect(url_for('users'))
    except Exception as err:
        flash(f'Error, could not delete user error was {err}', category="error")
        return redirect(url_for('users'))



# Add Exercise Page
@app.route("/add_exercise", methods=['GET', 'POST'])
@login_required
def add_exercise():
    """
    page for admin user to add new exercises to database
    """
    exercises_for_dropdown = SelectExercise.objects.all()
    add_exercise_form = AddExerciseForm()

    # check if current user is_admin
    if current_user.is_admin:

        if add_exercise_form.validate_on_submit():

            exercise_name = add_exercise_form.exercise_name.data

            # check if exercise already exists
            exercise_exists = SelectExercise.objects(exercise_name = exercise_name).first()

            if exercise_exists:
                flash('Exercise already exists!')
                return redirect(url_for('add_exercise'))


            exercise = SelectExercise(exercise_name=exercise_name)
            flash(f"{exercise_name} added to database")
            saved = exercise.save()
            return redirect(url_for("add_exercise"))

    if current_user.is_admin:
        return render_template(
            "add_exercise.html", add_exercise_form=add_exercise_form,
            exercises_for_dropdown=exercises_for_dropdown
        )

    flash(f'Only admins can add exercises')
    return redirect(url_for("get_strong"))

# Add Workout Page
@app.route("/add_workout", methods=['GET', 'POST'])
@login_required
def add_workout():
    """
    Enables the user to enter new workouts
    """

    username = current_user.username
    exercises = SelectExercise.objects.all()
    add_workout_form = AddWorkoutForm()

    # new_workout = {
    #     "workout_name": add_workout_form.workout_name.data,
    #     "exercise": add_workout_form.exercise.data,
    #     "sets": add_workout_form.sets.data,
    #     "reps": add_workout_form.reps.data,
    #     "weight": add_workout_form.weight.data,
    #     "comments": add_workout_form.comments.data,
    #     "user": username
    # }

    if add_workout_form.validate_on_submit():
        form_package = request.form.to_dict(flat=False)

        exercises = []
        for index in range(len(form_package['exercise'])):
            exercise_id = form_package['exercise'][index]
            if not exercise_id:
                continue
            exercise = SelectExercise.objects(id = exercise_id).first()
            sets = int(form_package['sets'][index])
            reps = int(form_package['reps'][index])
            weight = int(form_package['weight'][index])

            log_exercise = LogExercise(exercise_name=exercise.exercise_name, sets=sets, reps=reps, weight=weight)

            exercises.append(log_exercise)

        workout = Workout(exercises=exercises, workout_name=form_package['workout_name'][0], comments=form_package['comments'][0])

        user = User.objects.filter(id = current_user.id).first()
        user.workouts.append(workout)
        user.save()

        #db.users.insert_one(new_workout)

        # log_exercise_ids = []
        # for row_index in range(10):
            # exercise_name = request.form[f"exercise_name_{row_index}"]
            # if exercise_name = "":
            #     break
            # sets = request.form[f"set_{row_index}"]
            # reps = request.form[f"reps_{row_index}"]
            # weight = request.form[f"weight_{row_index}"]
            # log_exercise = LogExercise(exercise_name=exercise_name, reps=reps, sets=sets, weight=weight)
            # log_exercise.save()
            # log_exercise_ids.append(log_exercise.id)

        # workout_name = add_workout_form.workout_name.data
        # workout_comments = add_workout_form.comments.data
        # user_id = current_user.id
        # workout = Workout(workout_name=workout_name, comments=workout_comments, exercises=log_exercise_ids, user_id=user_id)
        # workout.save()

        flash(f"Workout added successfully!")
        return redirect(url_for("add_workout"))



    return render_template(
        "add_workout.html",  username=username,
        add_workout_form=add_workout_form, exercises=exercises
    )




