import sqlite3
from flask import Flask, g, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat_door.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/api/v1/logs', methods=['GET'])
def get_log():
    logs = db.session.execute(db.select(LogEntry).order_by(LogEntry.timestamp.desc()).limit(100))
    db.session.close()
    return ({'logs': [dict(row) for row in logs]}, 200)


@app.route('/api/v1/logs', methods=['POST'])
def new_log_entry():
    request_data = request.get_json()
    db.session.execute(db.insert(LogEntry), [{
        'action': request_data['action']
    }])
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
    db.session.execute('SELECT * FROM cats')
    cats = db.session.fetchall()
    db.session.close()
    cats_obj = []
    for cat in cats:
        cats_obj.append({'id': cat[0], 'name': cat[1], 'rfid': cat[2]})
    return ({'cats': cats_obj}, 200)


@app.route('/api/v1/cats/<cat_id>', methods=['GET'])
def get_cat_by_id(cat_id):
    db.session.execute('SELECT * FROM cats WHERE id = ?', (cat_id,))
    cat = db.session.fetchone()
    db.session.close()
    return {'id': cat[0], 'name': cat[1], 'rfid': cat[2]}


@app.route('/api/v1/cats/byRfid/<rfid>', methods=['GET'])
def get_cat_by_rfid(rfid):
    db.session.execute('SELECT * FROM cats WHERE rfid = ?', (rfid,))
    cat = db.session.fetchone()
    db.session.close()
    return {'id': cat[0], 'name': cat[1], 'rfid': cat[2]}


@app.route('/api/v1/cats/<cat_id>', methods=['POST'])
def update_cat(cat_id):
    request_data = request.get_json()
    db.session.execute('UPDATE cats SET name = ?, rfid = ? WHERE id = ?', (request_data['name'], request_data['rfid'], cat_id))
    db.commit()
    db.session.close()
    return ('Success', 200)


@app.route('/api/v1/cats', methods=['POST'])
def add_cat():
    request_data = request.get_json()
    db.session.execute('INSERT INTO cats (name, rfid) VALUES (?, ?)', (request_data['name'], request_data['rfid']))
    db.commit()
    return ('Success', 200)


@app.route('/api/v1/cats/<cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    db.session.execute('DELETE FROM cats WHERE id = ?', (cat_id,))
    db.commit()
    db.session.close()
    return ('Success', 200)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rfid = db.Column(db.String(80), nullable=False)

    def __json__(self):
        return {'id': self.id, 'name': self.name, 'rfid': self.rfid}

    def __repr__(self):
        return '<Cat %r>' % self.name


class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
    cat_id = db.Column(db.Integer, nullable=True)
    action = db.Column(db.String(80), nullable=False)

    def __json__(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'cat_id': self.cat_id,
            'action': self.action
        }

    def __repr__(self):
        return '<LogEntry %r>' % self.action
