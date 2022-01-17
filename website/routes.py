from flask import (
    flash, render_template,
    redirect, request, url_for
)
from flask_login import (
    LoginManager, login_user, login_required, logout_user, current_user
)
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
import datetime
from website.forms import RegistrationForm, LoginForm


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

        if existing_user or username_taken:
            flash("An account with this email/username already exists!!")
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


@app.route("/users")
def users():
    users = User.objects.all()
    for user in users:
        print(user.email)
    return render_template('users.html', users=users, current_user=current_user)

# Working on this to get the edit user functionality
@app.route("/edit_user")
def edit_user():

    try:
        user_email = request.args.get("email")
        user = User.objects(email = user_email).first()
        username = user.username
        flash(f'User {username} has been updated!', category="success")
        return redirect(url_for('users'))

    except Exception as err:
        flash(f'Error, could not delete user error was {err}', category="error")
        return redirect(url_for('users'))

    edit_user_form = RegistrationForm()
    return render_template('edit_user.html', users=users, current_user=current_user, edit_user_form=edit_user_form)


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


@app.route("/add_exercise")
def add_exercise():

    return "hello"


@app.route("/add_workout")
def add_workout():

    return "hello"


