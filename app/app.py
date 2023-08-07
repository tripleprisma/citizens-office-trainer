from flask import Flask
from app.extensions.database import db, migrate
from . import cookies, simple_pages, users
from app.extensions.authentication import login_manager



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(cookies.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)


