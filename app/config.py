from dotenv import load_dotenv
from os import environ


SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
load_dotenv()