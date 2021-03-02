from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    '''Create and configure Flask app'''
    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # import Blueprints
        from . import auth
        from . import catalog

        app.register_blueprint(auth.bp, url_prefix='/')
        app.register_blueprint(catalog.bp, url_prefix='/')

        # Create database models
        db.create_all()


    return app
