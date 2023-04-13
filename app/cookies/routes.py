from flask import Blueprint, render_template
# from .models import cookies


# cookies_data = {
#   'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
#   'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
#   'sugar' : {'name': 'Sugar', 'price': '$0.75'},
#   'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
#   'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
#   'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
# }

blueprint = Blueprint('cookies', __name__)

@blueprint.route('/cookies/<slug>')
def cookie(slug):
  if slug in cookies_data:
    return '<h1>' + cookies_data[slug]['name'] + '</h1>' + '<p>' + cookies_data[slug]['name'] + '</p>'
  else:
    return 'Sorry we could not find that cookie.' 

@blueprint.route('/cookies')
def cookies():
  return render_template('cookies/index.html', cookies=cookies_data)