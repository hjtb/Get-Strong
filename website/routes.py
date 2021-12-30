from flask import (
    Flask, flash, render_template,
    redirect, request, url_for
)
from flask_login import (
    LoginManager, UserMixin, login_user, login_required, logout_user, current_user
)
from flask import current_app as app
from website import db
from website.models import User


@app.route("/index")
def index():
    user = User(email="a", username="b")
    user.save()
    users = User.objects.all()
    for user in users:
        print(user.email)
    return "hello"