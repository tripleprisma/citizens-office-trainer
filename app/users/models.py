from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin


class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password = db.Column(db.String(1024))
