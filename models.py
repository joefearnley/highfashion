from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(50))
    message = db.Column(db.String(250))
    created = db.DateTime()

    def __init__(self, app, message):
        self.app_name = app
        self.message = message
        self.created = datetime.now()
