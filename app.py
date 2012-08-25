from flask import Flask, request
from models import db, Log
import logging
import json

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

"""
    TODO:
        * use app object for log configuration
        * or move config into its own directory
        * extract all logging to seperate module
        * create interface to see what is logged to db
        * sanitization?
"""

@app.route('/')
def hello():
    return 'Nothing to see here....'

@app.route('/log', methods=['POST'])
def log():

    # validate data
    if not request.form.get('app'):
        return json.dumps({'error': 'No Application is specified'})
    else:
        app_name = request.form['app']

    if not request.form.get('message'):
        return json.dumps({'error': 'No Message is specified'})
    else:
        message = request.form['message']

    # log data and message
    #log_message(app_name, message)
    log = LogHandler(app.config['LOG_TYPE'], app_name, message)
    log.log_message()
    return json.dumps({'response': 'successful log'})

class LogHandler(object):
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
        log = Log(self.app_name, self.message)
        db.session.add(log)
        db.session.commit()

    def log_to_filesystem(self):
        filename = app.config['LOG_FILENAME']
        logging.basicConfig(filename=filename, level=logging.INFO)
        logging.info('Message logged from %s: %s', app_name, message)

if __name__ == '__main__':
    app.run()
