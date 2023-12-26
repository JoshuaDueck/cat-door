from flask import request
from app.blueprints.main import bp
from app.models.log_entry import LogEntry
from app.extensions import db


@bp.route('/')
def index():
    return "Main Blueprint Root Path"


@bp.route('/door', methods=['GET'])
def get_door():
    return "Main Blueprint Door Path"


@bp.route('/door/unlock', methods=['POST'])
def unlock_door():
    return "Main Blueprint Door Unlock Path"


@bp.route('/door/lock', methods=['POST'])
def lock_door():
    return "Main Blueprint Door Lock Path"


@bp.route('/door/scan', methods=['POST'])
def scan():
    tag = request.get_json()

    log_entry = LogEntry(
        cat_id=tag.get('id'),
        action='scan'
    )
    db.session.add(log_entry)
    db.session.commit()

    return tag
