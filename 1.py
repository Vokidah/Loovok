__author__ = 'vokidah'

# fuser -k 5000/tcp
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, jsonify, url_for
from database_setup import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




app = Flask(__name__)
engine = create_engine('sqlite:///user.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        newUser = User(nickname=request.form['nickname'], email=request.form['email'], password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect(url_for('hello_world'))

#@app.route('login', methods=[])
#def login():

@app.route('/user/JSON')
def restaurantsJSON():
    users = session.query(User).all()
    return jsonify(users=[u.serialize for u in users])


@app.route('/user/<int:user_id>')
def show_user(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return render_template('show_user.html', user=user)


@app.route('/user')
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