import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_cors import CORS

login_manager = LoginManager()

from app.secrets_manager import get_secret

app = Flask(__name__)

app.config['SECRET_KEY'] = 'plkf124Fas4'
app.config['JWT_SECRET_KEY'] = 'lmomesso2021!!'
app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Pswd123$@db1.cdlikiuniwlk.sa-east-1.rds.amazonaws.com/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db:mysecret@db1.cdlikiuniwlk.sa-east-1.rds.amazonaws.com/db'



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def dbCreate():
    db.create_all()

db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)

########################################
# LOGIN CONFIGS

login_manager.init_app(app)
login_manager.login_view = "users.login"


@app.route('/')
def index():
    return render_template('home.html')

from app.users.views import users

app.register_blueprint(users, url_prefix="/users")