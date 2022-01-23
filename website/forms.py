from flask import Flask
from website.models import SelectExercise, User, Workout
from flask_mongoengine.wtf import model_form


# Using the User class we instantiate the registration form and make sure to 
# Set the password field to a password field as Flask WTF doesn't include PasswordField 
# in the models
RegistrationForm = model_form(User, field_args={'password': {'password': True}})

# Using the SelectExercise class we instantiate the AddExerciseForm
AddExerciseForm = model_form(SelectExercise)

# Using the User class with only the email and password fields we instantiate the LoginForm
LoginForm = model_form(User, only=['email', 'password'], field_args={'password': {'password': True}})

# Using the Workout class we instantiate the AddWorkoutForm
AddWorkoutForm = model_form(Workout, field_args={'comments': {'textarea': True}})



# EditUserForm = model_form(User, exclude=['password'])

# class LoginForm(FlaskForm):
#     """
#     Login form class for our login page
#     """
#     email = EmailField('Email', validators=[InputRequired(),
#         Length(min=6, max=30)])
#     password = PasswordField('Password', validators=[InputRequired(),
#         Length(min=6, max=30)])


# class AddExercise(FlaskForm):
#     exercise_name = StringField(
#         'Exercise name:', validators=[InputRequired(), Length(
#             min=4, max=30,
#             message='Must be 4-30 characters long')])


# class EditUserForm(FlaskForm):
#     """
#     Registration form class for our registration page
#     """
#     username = StringField('Username', validators=[InputRequired(),
#         Length(min=6, max=30)])
#     email = EmailField('Email', validators=[InputRequired(),
#         Length(min=6, max=30)])
#     password = PasswordField('Password', validators=[InputRequired(),
#         Length(min=6, max=30)])
#     is_admin = BooleanField('Is Admin', validators=[InputRequired()])


# class AddWorkout(FlaskForm):
#     """
#     Form class to add new workouts
#     """
#     #exercises = exercises = list(mongo.db.exercises.exercise_name.find())
   
#     workout_name = StringField('Workout name:', validators=[InputRequired(), Length(
#         min=4, max=30, message='Length must be 4-30 characters long')])
#     exercise = SelectField('exercise:',
#         choices=[('1', 'push ups'), ('2', 'pull ups')], validators=[InputRequired()])
#     sets = IntegerField('sets:', validators=[InputRequired(),
#         NumberRange(1, 20, message='Choose a value between 1 and 20')])
#     reps = IntegerField('reps:', validators=[InputRequired(),
#         NumberRange(1, 200, message='Choose a value between 1 and 200')])
#     weight = FloatField('weight:', validators=[InputRequired(),
#         NumberRange(1, 500, message='Choose a value between 1 and 500')])
#     comments = TextAreaField('comments:', validators=[InputRequired(), Length(
#         min=8, max=300, message='Must be 8-300 characters long')])
