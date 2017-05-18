from flask import Flask, url_for, request, render_template, jsonify
from flask_bootstrap import Bootstrap
from task_db import TaskDB


app = Flask(__name__)

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
        pass
#
# @app.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     db = get_db()
#     db.execute('insert into entries (title, text) values (?, ?)',
#                [request.form['title'], request.form['text']])
#     db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('show_entries'))
#


@app.route('/do')
def do():
    return render_template('do.html')
