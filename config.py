# Use in conjucntion with a .env file
# format of the .env is plain text with lines as follows

import datetime
# Class-based Flask app configuration
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'),override=True)

class Config:
    #
    # first the safe ones that we know the answer to
    #

    # The application entry point
    FLASK_APP = 'wsgi.py'
    #
    # Now the secret and machine specific ones from environment variables - see .env
    #
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI')
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    # database_password = os.environ.get('database_password')
    # And the dependant on environment variables
    # We don't need the if statement
    # We left it here to show how you can create the database connection string based on the environment variable set in .env file


if __name__ == "__main__":

    # test to see that config is working
    config = Config()
    keys = config.__dir__()
    for key in keys:
        if key[0:2] != "__":
            value = config.__getattribute__(key)
            if isinstance(value, str):
                print(f"key: {key} value: {value}")