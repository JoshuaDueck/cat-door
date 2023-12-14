from flask import request
from app.blueprints.log_entries import bp
from app.extensions import db
from app.models.log_entry import LogEntry


@bp.route('/', methods=['GET'])
def index():
    # Returns a list of all log entries
    log_entries = db.session.query(LogEntry).all()
    return {'log_entries': [log_entry.__json__() for log_entry in log_entries]}


@bp.route('/', methods=['POST'])
def create():
    log_data = request.get_json()
    log_entry = LogEntry(
        cat_id=log_data.get('cat_id'),
        action=log_data.get('action')
    )
    db.session.add(log_entry)
    db.session.commit()

    return ('Success', 200)
