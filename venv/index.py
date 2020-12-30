from flask import Flask, render_template, url_for
from data import tasks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tasks.html', tasks=tasks)