__author__ = 'vokidah'

# fuser -k 5000/tcp
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from database_setup import Base, User
from sqlalchemy import create_engine


app = Flask(__name__)
engine = create_engine('sqlite:///user.db')
Base.metadata.bind = engine
@app.route('/')
def hello_world():
    user = User(name='Arsen', email='arsen.khadikov@gmail.com')
    return "%s %s"%(user.name, user.email)

if __name__ == '__main__':
    Bootstrap(app.run())