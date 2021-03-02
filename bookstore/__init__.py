from flask import Flask


def create_app():
    '''Create and configure Flask app'''
    app = Flask(__name__)

    app.config.from_object('config.Config')

    with app.app_context():
        pass


    return app
