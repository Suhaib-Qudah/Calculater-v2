from flask import Flask, render_template, url_for
from data import tasks,tasklists

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tasks.html', tasks=tasks,tasklists=tasklists)
pass

@app.route('/taskslist')
def taskslist():
    return render_template('taskslist.html', tasks=tasks,tasklists=tasklists)
