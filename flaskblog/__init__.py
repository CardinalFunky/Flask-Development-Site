from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c8a4ba421534cbcdbbd0e9eb0de3f2d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskblog"
mongo = PyMongo(app)
db = mongo.db
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes