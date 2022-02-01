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
