from app.orders.models import Order, Address


def test_get_checkout_renders(client):
  # Page loads and renders checkout
  response = client.get('/checkout')
  assert b'Checkout' in response.data

def test_post_checkout_creates_order(client):
  # Creates an order record
  response = client.post('/checkout', data={
    'chocolate-chip': '2',
    'name': 'Jane',
    'street': '123 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip': '12345',
    'country': 'Candyland'
  })
  assert Order.query.first() is not None

  def test_post_checkout_creates_address(client):
    # Creates an address related to the order
    response = client.post('/checkout', data={
      'chocolate-chip': '2',
      'name': 'Jane',
      'street': '123 Main St',
      'city': 'Anytown',
      'state': 'CA',
      'zip': '12345',
      'country': 'Candyland'
    })
    assert Address.query.first().order_id is 1


def test_post_checkout_creates_cookie_order(client):
  # Creates a cookie order related to the order
  new_cookie = Todo(slug='chocolate-chip', name='Chocolate Chip', description=1.50)
  new_cookie.save()

  response = client.post('/checkout', data={
    'chocolate-chip': '2',
    'name': 'Jane',
    'street': '123 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip': '12345',
    'country': 'Candyland'
  })

  assert Order.query.first().cookie_orders[0].number_of_cookies == 2