from flask import request
from utils import LogHandler
from highfashion import app
import json

@app.route('/')
def hello():
    # TODO:
    # check to see if logging to database.
    # query for records
    # render template
    return 'Nothing to see here....'

@app.route('/log', methods=['POST'])
def log():
    if not request.form.get('app'):
        return json.dumps({'error': 'No Application is specified'})
    else:
        app_name = request.form['app']

    if not request.form.get('message'):
        return json.dumps({'error': 'No Message is specified'})
    else:
        message = request.form['message']

    log = LogHandler(app.config['LOG_TYPE'], app_name, message)
    log.log_message()
    return json.dumps({'response': 'successful log'})
