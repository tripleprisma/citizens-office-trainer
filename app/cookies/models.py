from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Cookie(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80))
    name = db.Column(db.String(80))
    price = db.Column(db.String(80))
