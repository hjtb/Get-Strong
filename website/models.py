from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()


class Users(db.Document, UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
 
    email = db.StringField(max_length=60)
    username = db.StringField(max_length=60)
    date = db.DateTimeField()
    workouts = db.ListField(db.StringField())
    is_admin = db.BooleanField(default=False)
    password = db.StringField(max_length=200)

    def get_id(self):
        object_id = self.id
        return str(object_id)




