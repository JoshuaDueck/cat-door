from app.extensions import db
import time


class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.current_timestamp()
        )
    cat_id = db.Column(db.Integer, db.ForeignKey("cat.id"), nullable=False)
    action = db.Column(db.String(80), nullable=False)

    def __json__(self):
        return {
            'id': self.id,
            'timestamp': int(time.mktime(self.timestamp.timetuple())),
            'cat_id': self.cat_id,
            'action': self.action
        }

    def __repr__(self):
        return '<LogEntry %r>' % self.action
