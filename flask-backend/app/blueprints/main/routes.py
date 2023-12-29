from flask import request
from app.blueprints.main import bp
from app.extensions import db
import threading

from app.models.log_entry import LogEntry
from app.models.cat import Cat
from app.models.door import Door

from app.utilities import GPIO
import time


@bp.route('/')
def index():
    return "Main Blueprint Root Path"


@bp.route('/door', methods=['GET'])
def get_door():
    door_pin_status = GPIO.input(26)
    door_open = (door_pin_status == GPIO.HIGH)
    door_locked = Door.query.first().locked
    door_blocked = Door.query.first().blocked

    return ({
        'door_open': door_open,
        'door_locked': door_locked,
        'door_blocked': door_blocked
    }, 200)


@bp.route('/door/unlock', methods=['POST'])
def unlock_door():
    try:
        Door.query.first().unlock()
    except Exception as e:
        return ({'error': str(e)}, 500)

    return ({'door_locked': False}, 200)


@bp.route('/door/lock', methods=['POST'])
def lock_door():
    try:
        Door.query.first().lock()
    except Exception as e:
        return ({'error': str(e)}, 500)

    return ({'door_locked': True}, 200)


@bp.route('/door/open', methods=['POST'])
def open_door():
    GPIO.output(26, GPIO.HIGH)
    print('Door is open!')
    return ({'door_open': True}, 200)


@bp.route('/door/close', methods=['POST'])
def close_door():
    GPIO.output(26, GPIO.LOW)
    print('Door is closed!')
    return ({'door_open': False}, 200)


@bp.route('/door/scan', methods=['POST'])
def scan():
    tag = request.get_json()
    cat = Cat.query.filter_by(rfid=tag.get('id')).first()
    cat_id = None if cat is None else cat.id
    log_entry = LogEntry(
        cat_id=cat_id,
        action='scan'
    )
    db.session.add(log_entry)
    db.session.commit()

    t = threading.Thread(target=open_door)
    t.start()
    return tag


def open_door():
    GPIO.output(26, GPIO.HIGH)
    print('Door is open!')
    time.sleep(5)
    GPIO.output(26, GPIO.LOW)
    print('Door is closed!')

