from flask import Flask, url_for, request, render_template, jsonify
from flask_bootstrap import Bootstrap


app = Flask(__name__)

Bootstrap(app)

class DummyTask:
    caption = "Go fly a kite"
    description = "Go outside and fly the biggest kite you can find"
    points = 25


@app.route('/')
@app.route('/<param>')
def main(param='hike'):
    return render_template('explore.html', tasks = [DummyTask] * 3)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        pass

@app.route('/do')
def do():
    return render_template('do.html')
