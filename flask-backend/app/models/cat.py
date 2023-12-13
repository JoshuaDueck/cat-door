class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rfid = db.Column(db.String(80), nullable=False)

    def __json__(self):
        return {'id': self.id, 'name': self.name, 'rfid': self.rfid}

    def __repr__(self):
        return '<Cat %r>' % self.name
