from flask import Flask
from app.extensions.database import db, migrate
from . import cookies, simple_pages, orders

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_extensions(app)
  register_blueprints(app)

  return app


# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
#  app.register_blueprint(simple_pages.routes.blueprint)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)


def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)


# @app.route('/')
# def index():
#     return 'Hello World!'

# @app.route('/about')
# def about():
#   return render_template('index.html', name=cookies_data, visitor_number=342)




