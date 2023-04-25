from flask import Blueprint, render_template, request, redirect, url_for
from app.cookies.models import Cookie
from app.orders.models import Order, Address

blueprint = Blueprint('orders', __name__)


@blueprint.route('/checkout')
def checkout():
    return render_template('orders/new.html')


@blueprint.post('/checkout')
def post_checkout():

    address = Address(
        name=request.form.get('name'),
        street=request.form.get('street'),
        city=request.form.get('city'),
        state=request.form.get('state'),
        zip=request.form.get('zip'),
        country=request.form.get('country')
    )
    address.save()
    return redirect(url_for('cookies.cookies'))