import datetime
from flask import current_app as app
from mongoengine.fields import ReferenceField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from wtforms import (
    PasswordField, StringField, IntegerField, EmailField, HiddenField, BooleanField, FloatField, SubmitField)
db = MongoEngine()


class SelectExercise(db.Document):
    exercise_name = db.StringField(max_length=30, min_length=6, required=True)


class LogExercise(db.EmbeddedDocument):
    exercise_name = db.ReferenceField('SelectExercise')
    sets = db.IntField(required=True, min_value=1, max_value=10)
    reps = db.IntField(required=True, min_value=1, max_value=200)
    weight = db.FloatField(required=True, min_value=1, max_value=500)


class Workout(db.EmbeddedDocument):
    workout_date = db.DateTimeField(default=datetime.datetime.now)
    workout_name = db.StringField(max_length=30, min_length=6, required=True)
    exercises = db.EmbeddedDocumentListField(LogExercise)
    comments = StringField(min_length=8)
#     username = current_user.username


class Users(db.Document, UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
 
    email = db.EmailField(max_length=30, min_length=6, required=True)
    username = db.StringField(max_length=30, min_length=6, required=True)
    workouts = db.EmbeddedDocumentListField(LogExercise)
    password = db.StringField(max_length=200, required=True)
    is_admin = db.BooleanField(default=False)
    date = db.DateTimeField()

    def get_id(self):
        object_id = self.id
        return str(object_id)
        
RegistrationForm = model_form(Users)