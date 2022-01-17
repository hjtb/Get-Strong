from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    # Create Flask application.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        db.init_app(app)

        # import the routes
        from website import routes

    # all is set up correctly so return the app
    return app