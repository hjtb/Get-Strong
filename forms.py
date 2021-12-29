from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (
    PasswordField, StringField, IntegerField, EmailField, HiddenField, 
    RadioField, SelectField, TextAreaField, BooleanField, SubmitField)
from wtforms.validators import InputRequired, Length, Email, ValidationError, NumberRange


class RegistrationForm(FlaskForm):
    """
    Registration form class for our registration page
    """
    username = StringField('Username', validators=[InputRequired(),
        Length(min=6, max=30)])
    email = EmailField('Email', validators=[InputRequired(),
        Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(min=6, max=30)])


class LoginForm(FlaskForm):
    """
    Login form class for our login page
    """
    email = EmailField('Email', validators=[InputRequired(),
        Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(min=6, max=30)])


class AddWorkout(FlaskForm):
    """
    Form class to add new workouts
    """
    workout_name = validators = [InputRequired(), Length(
        min=4, max=30, message='Length must be 4-30 characters long')]
    exercise = SelectField('Exercise:', validators=[InputRequired()])
    reps = IntegerField('Reps:', validators=[InputRequired(), NumberRange()])
    weight = IntegerField('Weight(kg):', validators=[InputRequired()])
    comments = TextAreaField('Comments:', validators=[InputRequired(), Length(
        min=8, max=300, message='Must be 8-300 characters long')])


class AddExercise(FlaskForm):
    exercise_name = StringField(
        'Exercise name:', validators=[InputRequired(), Length(
            min=4, max=30,
            message='Must be 4-30 characters long')])
