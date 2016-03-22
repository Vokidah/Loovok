__author__ = 'vokidah'

# fuser -k 5000/tcp
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run()