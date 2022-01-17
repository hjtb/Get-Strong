# Use in conjucntion with a .env file
# Class-based Flask app configuration
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'),override=True)

class Config:

    # first the safe ones that we know the answer to

    # The application entry point
    FLASK_APP = 'wsgi.py'

    # Now the secret and machine specific ones from environment variables - see .env
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = dict(host = os.environ.get('MONGO_URI'))
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))



if __name__ == "__main__":

    # test to see that config is working
    config = Config()
    keys = config.__dir__()
    for key in keys:
        if key[0:2] != "__":
            value = config.__getattribute__(key)
            if isinstance(value, str):
                print(f"key: {key} value: {value}")