from flask import request
from app.blueprints.log_entries import bp
from app.extensions import db
from app.models.log_entry import LogEntry
from app.models.cat import Cat


@bp.route('/', methods=['GET'])
def index():
    limit = request.args.get('limit')

    if limit:
        log_entries = db.session.query(LogEntry).order_by(LogEntry.id.desc()).limit(limit).all()
        return {'log_entries': [log_entry.__json__() for log_entry in log_entries]}

    log_entries = db.session.query(LogEntry).all()
    return {'log_entries': [log_entry.__json__() for log_entry in log_entries]}


@bp.route('/', methods=['POST'])
def create():
    log_data = request.get_json()

    cat = db.session.query(Cat).filter_by(rfid=log_data.get('cat_id')).first()

    log_entry = LogEntry(
        cat_id=cat.id if cat else None,
        action=log_data['action']
    )
    db.session.add(log_entry)
    db.session.commit()

    return (log_entry.__json__(), 200)
