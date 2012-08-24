from flask import Flask, request
import json
import logging

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')

@app.route('/')
def hello():
    return 'Nothing to see here....'

@app.route('/log', methods=['POST'])
def log():

    response = ''

    # validate two pieces of data
    if not request.form.get('app'):
        return json.dumps({'error': 'No Application is specified'})
    else:
        app_name = request.form['app']

    if not request.form.get('message'):
        return json.dumps({'error': 'No Message is specified'})
    else:
        message = request.form['message']

    log_message(app_name, message)
    return json.dumps({'response': 'successful log'})

def log_message(app_name, message):
    log_type = app.config['LOG_TYPE']
    if log_type == 'filesystem':
        log_to_filesystem(app_name, message)
    elif log_type == 'database':
        log_to_database(app, message)
    else:
        print 'Post request from %s: %s', app_name, message


def log_to_database(app_name, message):
    return ""

def log_to_filesystem(app_name, message):
    filename = app.config['LOG_FILENAME']
    logging.basicConfig(filename=filename, level=logging.INFO)
    logging.info('Post request from %s: %s', app_name, message)

if __name__ == '__main__':
    app.run()
