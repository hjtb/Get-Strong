from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
    def __init__(self, user_mongo):
        self.id = user_mongo.get("_id")
        self.email = user_mongo.get('email')
        self.username = user_mongo.get('username')
        self.workouts = user_mongo.get('workouts')
        self.is_admin = user_mongo.get('is_admin')

    def get_id(self):
        object_id = self.id
        return str(object_id)
