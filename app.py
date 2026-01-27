from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/nisse')
def hello():
    return 'Hei, hva gjør du her???'