from flask import Flask, url_for, request, render_template, jsonify, flash, redirect
from flask_bootstrap import Bootstrap
from task_db import TaskDB

app = Flask(__name__)
app.secret_key = 'many random bytes'
Bootstrap(app)


tasks_json = {
    "tasks" : [
        {
            "caption" : "Go fly a kite",
            "description" : "Go outside and fly the biggest kite you can find",
            "points" : 25,
        },
        {
            "caption" : "Go fly another kite",
            "description" : "Go outside and fly the second biggest kite you can find",
            "points" : 30,
        },
        {
            "caption" : "Go fly a third kite",
            "description" : "Go outside and fly the third biggest kite you can find",
            "points" : 35,
        },
    ],
}


@app.route('/')
@app.route('/<param>')
def main(param='hike'):
    filename = 'db/db1.pickle'
    db = TaskDB(filename)
    return render_template('explore.html', tasks = db.get_tasks(words = "", creator = "", in_out_online = "", task_type = "", location = "", value = "", num_of_tasks = 5))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:

        flash('Task created!', category='info')
        return redirect(url_for('main'))


@app.route('/do')
def do():
    return render_template('do.html')

