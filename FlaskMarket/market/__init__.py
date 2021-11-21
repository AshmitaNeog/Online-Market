# init = initialization
# defines the package market using init file

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # an instance of flask instance
# uri = uniform resource identifier
# identifies 'sqlite:///market.db' as our flask database using sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '5ae3832596f548c4d2d8c1e4'
db = SQLAlchemy(app)  # database for our flask instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes

"""

set FLASK_APP=market.py
set FLASK_DEBUG=1
flask run

pip install flask
pip install flask-sqlalchemy

i1 = Item(name='iPhone 12', price=800, barcode='958283456701', 
            description='desc')
db.session.add(item1)
db.session.commit()
Item.query.all()
Item.query.filter_by(price=500) -> query by price

from market.models import db
db.drop_all()
db.create_all()
from market.models import User, Item

rolls back session to previous version
db.session.rollback()

u1 = User(username='jsc', password_hash='123456', email_address='jsc@jsc.com')
i1 = Item(name='iPhone 12', price=800, barcode='958283456701', description='desc')
i2 = Item(name='Laptop', price=1200, barcode='983412095829', description='desc2')

first() gets the actual object instead of base object
item1 = Item.query.filter_by(name='iPhone 12').first()

get the owner of item by foreign key
item1.owner

i = Item.query.filter_by(name='iPhone 12')
"""