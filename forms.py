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

    submit = SubmitField("Login")
