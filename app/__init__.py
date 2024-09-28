from flask import Flask, request
from datetime import datetime
from project.cookies import cookies_blueprint
from project.users import users_blueprint
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#setting up the db object
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #add application contexts
    @app.context_processor
    def inject_year():
        return dict(current_year=datetime.now().year)

    @app.context_processor
    def inject_cookies_avr():
        cookie_value = request.cookies.get('cookies_avr')
        return dict(cookie_value=cookie_value)

    # Resiter main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register the blueprints
    app.register_blueprint(cookies_blueprint)
    app.register_blueprint(users_blueprint)

    # As we're using an application factory we need to configure the db object
    db.init_app(app)

    # We're using migrate to have version control on the DB tables and content
    migrate.init_app(app, db)

    return app

