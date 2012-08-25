from flask import Flask, request
from models import db, Log
import logging
import json

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

"""
    TODO:
        * use app object for configuration
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
    log_message(app_name, message)
    return json.dumps({'response': 'successful log'})

def log_message(app_name, message):
    log_type = app.config['LOG_TYPE']
    if log_type == 'filesystem':
        log_to_filesystem(app_name, message)
    elif log_type == 'database':
        log_to_database(app_name, message)
    else:
        print 'Message logged from %s: %s', app_name, message

def log_to_database(app_name, message):
    log = Log(app_name, message)
    db.session.add(log)
    db.session.commit()

def log_to_filesystem(app_name, message):
    filename = app.config['LOG_FILENAME']
    logging.basicConfig(filename=filename, level=logging.INFO)
    logging.info('Message logged from %s: %s', app_name, message)

if __name__ == '__main__':
    app.run()
