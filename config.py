import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://app:app@localhost/jogoteca'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
