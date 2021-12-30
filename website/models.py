from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()


class User(db.Document, UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
    __tablename__ = 'users'    
    email = db.StringField(max_length=60)
    username = db.StringField(max_length=60)

    def get_id(self):
        object_id = self.id
        return str(object_id)

        
"""    def __init__(self, user_mongo):
        self.id = user_mongo.get("_id")
        self.email = user_mongo.get('email')
        self.username = user_mongo.get('username')
        self.workouts = user_mongo.get('workouts')
        self.is_admin = user_mongo.get('is_admin')
"""



