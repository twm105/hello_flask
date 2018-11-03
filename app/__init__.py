from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # python sql abstraction
migrate = Migrate(app,db) # manages changes to the database model, analogous to git...
login = LoginManager(app)
login.login_view = 'login' # tells Flask-Login the login view (route) function


from app import routes, models