import datetime
from flask import current_app as app
from mongoengine.fields import ReferenceField
from flask_login import UserMixin
from flask_mongoengine import MongoEngine
from wtforms import (
    PasswordField, StringField, IntegerField, EmailField, HiddenField, BooleanField, FloatField, SubmitField)
db = MongoEngine()


class SelectExercise(db.Document):
    exercise_name = db.StringField(max_length=30, min_length=6, required=True)


class LogExercise(db.EmbeddedDocument):
    exercise_name = db.ReferenceField(SelectExercise)
    sets = db.IntField(required=True, min_value=1, max_value=10)
    reps = db.IntField(required=True, min_value=1, max_value=200)
    weight = db.IntField(required=True, min_value=1, max_value=500)
    meta = {
        'collection': 'log_exercises'
    }


class Workout(db.EmbeddedDocument):
    workout_date = db.DateTimeField(default=datetime.datetime.now)
    workout_name = db.StringField(max_length=30, min_length=6, required=True)
    exercises = db.EmbeddedDocumentListField(LogExercise)
    comments = db.StringField()
    meta = {
        'collection': 'workouts'
    }


# create the user class
class User(db.Document, UserMixin):
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """
 
    # create the user object
    email = db.EmailField(max_length=30, min_length=6, required=True)
    username = db.StringField(max_length=30, min_length=6, required=True)
    workouts = db.EmbeddedDocumentListField(Workout)
    password = db.StringField(max_length=200, min_length=8, required=True, field_args={'password': {'password': True}})
    is_admin = db.BooleanField(default=False)
    date = db.DateTimeField(default=datetime.datetime.now)

    def get_id(self):
        object_id = self.id
        return str(object_id)

    meta = {
        'collection': 'users'
    }
