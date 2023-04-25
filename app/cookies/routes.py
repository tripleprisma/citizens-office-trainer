from flask import Blueprint, render_template, request, current_app, redirect, url_for
from .models import Cookie

cookies_data = {
    'chocolate-chip': {'name': 'Chocolate Chip', 'price': '$1.50'},
    'oatmeal-raisin': {'name': 'Oatmeal Raisin', 'price': '$1.00'},
    'sugar': {'name': 'Sugar', 'price': '$0.75'},
    'peanut-butter': {'name': 'Peanut Butter', 'price': '$0.50'},
    'oatmeal': {'name': 'Oatmeal', 'price': '$0.25'},
    'salted-caramel': {'name': 'Salted Caramel', 'price': '$1.00'},
}

blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies/<slug>')
def cookie(slug):
    cookie = Cookie.query.filter_by(slug=slug).first()
    return render_template('cookies/show.html', cookie=cookie)


@blueprint.route('/cookies')
def cookies():
    page_number = request.args.get('page', 1, type=int)
    cookies_pagination = Cookie.query.paginate(
        page=page_number, per_page=current_app.config['COOKIES_PER_PAGE'])
    return render_template('cookies/cookies.html', cookies_pagination=cookies_pagination)


@blueprint.route('/edit-cookie/<id>')
def edit_cookie_page(id):
    cookie = Cookie.query.filter_by(id=id).first()
    return render_template('cookies/edit.html', cookie=cookie)


@blueprint.post('/edit-cookie/<id>')
def edit_cookie(id):
    cookie = Cookie.query.filter_by(id=id).first()
    cookie.name = request.form.get('name')
    cookie.price = request.form.get('price')
    cookie.save()
    return redirect(url_for('cookies.cookies'))


@blueprint.post('/delete-cookie/<id>')
def delete_cookie(id):
    cookie = Cookie.query.filter_by(id=id).first()
    cookie.delete()
    return redirect(url_for('cookies.cookies'))


@blueprint.route('/add-cookie')
def add_cookie_page():
    return render_template('cookies/new.html')


@blueprint.post('/add-cookie')
def add_cookie():
    print("test")

    cookie = Cookie( 
        slug=request.form.get('slug'),
        name =request.form.get('name'),
        price = request.form.get('price')
        )
    cookie.save()
    return redirect(url_for('cookies.cookies'))
