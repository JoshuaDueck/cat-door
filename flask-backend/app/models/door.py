from app.extensions import db


class Door(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    locked = db.Column(db.Boolean, default=False)
    open = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)

    def unlock(self):
        self.locked = False
        db.session.commit()

    def lock(self):
        self.locked = True
        db.session.commit()

    def __json__(self):
        return {
            'id': self.id,
            'locked': self.locked,
            'open': self.open,
            'blocked': self.blocked
        }

    def __repr__(self):
        return '<Door %r>' % self.name
