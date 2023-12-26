from flask import request
from app.blueprints.main import bp
from app.models.log_entry import LogEntry
from app.models.cat import Cat
from app.extensions import db
import threading

import RPi.GPIO as GPIO
import time

@bp.route('/')
def index():
    return "Main Blueprint Root Path"


@bp.route('/door', methods=['GET'])
def get_door():
    door_pin_status = GPIO.input(26)
    door_open = (door_pin_status == GPIO.HIGH)

    return ({'door_open': door_open}, 200)


@bp.route('/door/unlock', methods=['POST'])
def unlock_door():
    return "Main Blueprint Door Unlock Path"


@bp.route('/door/lock', methods=['POST'])
def lock_door():
    return "Main Blueprint Door Lock Path"


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

    # Find the cat by rfid, with the tag id
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

