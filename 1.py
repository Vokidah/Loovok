__author__ = 'vokidah'

# fuser -k 5000/tcp
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, jsonify, url_for
from database_setup import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re




app = Flask(__name__)
engine = create_engine('sqlite:///user.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
db_session = DBsession()
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


def valid_username(username):
    if USER_RE.match(username):
        return True
    return False


def valid_password(password):
    if PASS_RE.match(password):
        return True
    return False


def valid_email(email):
    if EMAIL_RE.match(email):
        return True
    return False


def valid_verify(password, verify):
    if password == verify:
        return True
    return False


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']
        verify_password = request.form['verify_password']
        #return "%s %s %s %s"%(nickname, email, password, verify_password)
        if valid_username(nickname) and valid_email(email) and valid_password(password) and valid_verify(password, verify_password):
            newUser = User(nickname=nickname, email=email, password=password)
            db_session.add(newUser)
            db_session.commit()
            return redirect(url_for('hello_world'))
        else:
            return redirect(url_for('registration'))


@app.route('/user/JSON')
def restaurantsJSON():
    users = db_session.query(User).all()
    return jsonify(users=[u.serialize for u in users])


@app.route('/<int:user_id>')
@app.route('/user/<int:user_id>')
def show_user(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return render_template('show_user.html', user=user)


@app.route('/user')
@app.route('/')
def hello_world():
    #db_session.add(User(nickname='Arsen', password='123', email='arsen.khadikov@gmail.com'))
    #db_session.add(User(nickname='Vitya', password='123', email='vitya.sobol@gmail.com'))
    #db_session.add(User(nickname='Vlad', password='123', email='vlad.fedchenko@gmail.com'))
    #db_session.commit()
    users = db_session.query(User).all()
    return render_template('hello_world.html', users=users)



if __name__ == '__main__':
    Bootstrap(app.run(debug=True))