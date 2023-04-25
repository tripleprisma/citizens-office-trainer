from flask import Blueprint, render_template, redirect

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')