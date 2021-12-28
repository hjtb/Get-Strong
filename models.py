from pymodm import MongoModel, fields
from datetime import datetime
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Workout(MongoModel):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = fields.CharField(max_length=30)
    exercise = db.relationship("Exercise", secondary=exercises_muscles, backref="muscles_backref")
    set = db.Column(db.String(500), nullable=False)
    weight = db.Column(db.String(100), nullable=False)
    comments = db.Column(db.DateTime(timezone=True), server_default=func.now())
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    
    def __repr__(self):
        return dict(id=self.id, name=self.name, description=self.description, image=self.image ) 


class Exercise(MongoModel):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    muscles = db.relationship("Muscle", secondary=exercises_muscles, backref="exercises_backref")
    machines = db.relationship("Machine", secondary=machines_exercises, backref="exercises_backref")

    def __repr__(self):
        return dict(id=self.id, name=self.name, description=self.description) 


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
