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
    #session.add(User(nickname='Arsen', password='123', email='arsen.khadikov@gmail.com'))
    #session.add(User(nickname='Vitya', password='123', email='vitya.sobol@gmail.com'))
    #session.add(User(nickname='Vlad', password='123', email='vlad.fedchenko@gmail.com'))
    #session.commit()
   users = session.query(User).all()
   return render_template('hello_world.html', users=users)
   # return ""



if __name__ == '__main__':
    Bootstrap(app.run(debug=True))