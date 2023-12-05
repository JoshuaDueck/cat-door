import sqlite3
from flask import Flask, g

app = Flask(__name__)


DATABASE = './cat_door.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db


@app.route('/api/v1/logs', methods=['GET'])
def access_logs():
    return 'Access Logs'


@app.route('/api/v1/enable_door', methods=['POST'])
def enable_door():
    return 'Enable Door'


@app.route('/api/v1/disable_door', methods=['POST'])
def disable_door():
    return 'Disable Door'


@app.route('/api/v1/door_status', methods=['GET'])
def door_status():
    return 'Door Status'


@app.route('/api/v1/cats', methods=['GET'])
def get_cats():
    return 'Get Cats'


@app.route('/api/v1/cats', methods=['POST'])
def add_cat():
    return 'Add Cat'


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
