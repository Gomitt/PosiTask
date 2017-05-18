from flask import Flask, url_for, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/<param>')
def main(param='hike'):
    return render_template('explore.html', param = positize(param))

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/do')
def do():
    return render_template('do.html')

def positize(task):
    return 'Posi' + task.title()
