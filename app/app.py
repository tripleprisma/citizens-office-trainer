from flask import Flask, redirect, url_for, render_template, send_file
import urllib.request
from . import cookies

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_blueprints(app)

  return app


# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)


# @app.route('/')
# def index():
#     return 'Hello World!'

# @app.route('/about')
# def about():
#   return render_template('index.html', name=cookies_data, visitor_number=342)




