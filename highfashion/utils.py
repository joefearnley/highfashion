from models import db
from models import Message
import logging
from highfashion import app

db.init_app(app)

class MessageHandler(object):
    def __init__(self, log_type, app_name, message):
        self.log_type = log_type
        self.app_name = app_name
        self.message = message
        # self.file_name = filename??

    def log_message(self):
        if self.log_type == 'filesystem':
            self.log_to_filesystem()
        elif self.log_type == 'database':
            self.log_to_database()
        else:
            print 'Message logged from %s: %s', app_name, message

    def log_to_database(self):
        log = Message(self.app_name, self.message)
        db.session.add(log)
        db.session.commit()

    def log_to_filesystem(self):
        filename = app.config['LOG_FILENAME']
        logging.basicConfig(filename=filename, level=logging.INFO)
        logging.info('Message logged from %s: %s', self.app_name, self.message)
