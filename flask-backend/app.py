import sqlite3
from flask import Flask, g, request

app = Flask(__name__)


DATABASE = './cat_door.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db


@app.route('/api/v1/logs', methods=['GET'])
def get_log():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM logs')
    logs = cursor.fetchall()
    cursor.close()
    logs_obj = []
    for log in logs:
        logs_obj.append({'id': log[0], 'timestamp': log[1], 'cat_id': log[2], 'action': log[3]})
    return ({'logs': logs_obj}, 200)


@app.route('/api/v1/logs', methods=['POST'])
def new_log_entry():
    request_data = request.get_json()
    db = get_db()
    cursor = db.cursor()

    cat_id = None

    if 'cat_id' in request_data:
        cat_id = request_data['cat_id']

    cursor.execute('INSERT INTO logs (cat_id, action) VALUES (?, ?)', (cat_id, request_data['action']))
    db.commit()
    cursor.close()
    return ('Success', 200)


@app.route('/api/v1/door', methods=['GET'])
def get_door():
    return ({'door': {'blocked': False, 'locked': False}}, 200)


@app.route('/api/v1/door/lock', methods=['POST'])
def lock_door():
    return 'Lock Door'


@app.route('/api/v1/door/unlock', methods=['POST'])
def unlock_door():
    return 'Unlock Door'


@app.route('/api/v1/door_status', methods=['GET'])
def door_status():
    return 'Door Status'


@app.route('/api/v1/cats', methods=['GET'])
def get_cats():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cats')
    cats = cursor.fetchall()
    cursor.close()
    cats_obj = []
    for cat in cats:
        cats_obj.append({'id': cat[0], 'name': cat[1], 'rfid': cat[2]})
    return ({'cats': cats_obj}, 200)


@app.route('/api/v1/cats/<cat_id>', methods=['GET'])
def get_cat_by_id(cat_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cats WHERE id = ?', (cat_id,))
    cat = cursor.fetchone()
    cursor.close()
    return {'id': cat[0], 'name': cat[1], 'rfid': cat[2]}


@app.route('/api/v1/cats/byRfid/<rfid>', methods=['GET'])
def get_cat_by_rfid(rfid):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cats WHERE rfid = ?', (rfid,))
    cat = cursor.fetchone()
    cursor.close()
    return {'id': cat[0], 'name': cat[1], 'rfid': cat[2]}


@app.route('/api/v1/cats/<cat_id>', methods=['POST'])
def update_cat(cat_id):
    request_data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('UPDATE cats SET name = ?, rfid = ? WHERE id = ?', (request_data['name'], request_data['rfid'], cat_id))
    db.commit()
    cursor.close()
    return ('Success', 200)


@app.route('/api/v1/cats', methods=['POST'])
def add_cat():
    request_data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO cats (name, rfid) VALUES (?, ?)', (request_data['name'], request_data['rfid']))
    db.commit()
    cursor.close()
    return ('Success', 200)


@app.route('/api/v1/cats/<cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM cats WHERE id = ?', (cat_id,))
    db.commit()
    cursor.close()
    return ('Success', 200)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
