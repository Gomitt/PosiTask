from flask import Flask, url_for, request, render_template, jsonify, flash, redirect
from flask_bootstrap import Bootstrap
from task_db import TaskDB
import json

TASKS_TO_SERVE = 5

db_filename = 'db/db1.pickle'
app = Flask(__name__)
app.secret_key = 'many random bytes'
Bootstrap(app)

tasks_json = {
    "tasks" : [
        {
            "title" : "Go fly a kite",
            "description" : "Go outside and fly the biggest kite you can find",
            "value" : 25,
        },
        {
            "title" : "Go fly another kite",
            "description" : "Go outside and fly the second biggest kite you can find",
            "value" : 30,
        },
        {
            "title" : "Go fly a third kite",
            "description" : "Go outside and fly the third biggest kite you can find",
            "value" : 35,
        },
    ],
}

db = TaskDB(db_filename)
tasks_dict = db.get_tasks_dict()


@app.route('/')
def main():
    return render_template('explore.html', tasks=tasks_dict)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', types=db.task_types)
    else:
        flash('Task created!', category='info')
        return redirect(url_for('main'))


@app.route('/do/<task_id>')
def do(task_id=None):
    task = db.get_by_id(task_id)
    print(task)
    return render_template('do.html', task=task)

