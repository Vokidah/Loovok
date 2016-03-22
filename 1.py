__author__ = 'vokidah'

# fuser -k 5000/tcp
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from database_setup import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




app = Flask(__name__)
engine = create_engine('sqlite:///user.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def hello_world():
    session.add(User(name='Arsen', email='arsen.khadikov@gmail.com'))
    session.commit()
    user = session.query(User).first()
    return "%s %s"%(user.name, user.email)



if __name__ == '__main__':
    Bootstrap(app.run())