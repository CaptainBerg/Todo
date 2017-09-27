from . import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64))
    time = db.Column(db.DateTime(), default=datetime.utcnow)
    status =  db.Column(db.Boolean, default=False)



