from flask import Flask, request
import json
import logging

app = Flask(__name__)

# config
LOG_TYPE = 'FS' # FS or DB
DB_URI = ''

@app.route('/')
def hello():
    return 'Nothing to see here....'

@app.route('/log', methods=['POST'])
def log():

    response = ''

    # validate two pieces of data
    if not request.form.get('app'):
        return json.dumps({'error': 'No App is specified'})
    else:
        app = request.form['app']

    if not request.form.get('message'):
        return json.dumps({'error': 'No Message is specified'})
    else:
        message = request.form['message']

    if LOG_TYPE == 'FS':
        log_to_filesystem(app, message)
    elif LOG_TYPE == 'DB':
        log_to_database(app, message)
    else:
        print 'logging to stdout'

    return json.dumps({'response', 'successful log'})

def log_to_database(app_name, message):
    return ""

def log_to_filesystem(app_name, message):
    logging.basicConfig(filename='highfashion.log', level=logging.INFO)
    logging.info('Post request from %s: %s', app_name, message)

if __name__ == '__main__':
    app.debug = True
    app.run()
