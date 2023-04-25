from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Order(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  address = db.relationship('Address', backref='order', uselist=False, lazy=True)

class Address(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
