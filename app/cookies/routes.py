from flask import Blueprint, render_template, request, current_app, redirect, url_for
from .models import Todo

blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies/<id>')
def cookie(id):
    cookie = Todo.query.filter_by(id=id).first()
    return render_template('cookies/show.html', cookie=cookie)


@blueprint.route('/cookies')
def cookies():
    page_number = request.args.get('page', 1, type=int)
    cookies_pagination = Todo.query.paginate(
        page=page_number, per_page=current_app.config['COOKIES_PER_PAGE'])
    return render_template('cookies/cookies.html', cookies_pagination=cookies_pagination)


@blueprint.route('/edit-cookie/<id>')
def edit_cookie_page(id):
    cookie = Todo.query.filter_by(id=id).first()
    return render_template('cookies/edit.html', cookie=cookie)


@blueprint.post('/edit-cookie/<id>')
def edit_cookie(id):
    cookie = Todo.query.filter_by(id=id).first()
    cookie.name = request.form.get('name')
    cookie.description = request.form.get('price')
    cookie.save()
    return redirect(url_for('cookies.cookies'))


@blueprint.post('/delete-cookie/<id>')
def delete_cookie(id):
    cookie = Todo.query.filter_by(id=id).first()
    cookie.delete()
    return redirect(url_for('cookies.cookies'))


@blueprint.route('/add-cookie')
def add_cookie_page():
    return render_template('cookies/new.html')


@blueprint.post('/add-cookie')
def add_cookie():

    cookie = Todo(
        slug=request.form.get('slug'),
        name=request.form.get('name'),
        description=request.form.get('price')
    )
    cookie.save()
    return redirect(url_for('cookies.cookies'))
