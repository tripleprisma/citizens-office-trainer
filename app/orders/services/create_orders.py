from app.orders.models import Order, Address, CookieOrder
from flask import request


def create_order():
    # Create an order
    order = Order()
    order.save()

    # Create address
    address = Address(
        name=request.form.get('name'),
        street=request.form.get('street'),
        city=request.form.get('city'),
        state=request.form.get('state'),
        zip=request.form.get('zip'),
        country=request.form.get('country'),
        order=order
    )
    address.save()

    # Create cookie orders
    for cookie in cookies:
        number_of_cookies = request.form.get(cookie.slug, 0)

        if int(number_of_cookies) > 0:
            cookie_order = CookieOrder(
                cookie=cookie,
                order=order,
                number_of_cookies=number_of_cookies
            )
            cookie_order.save()
