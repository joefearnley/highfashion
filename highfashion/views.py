from flask import request, render_template
from utils import MessageHandler
from models import Message
from highfashion import app
import json

@app.route('/', methods=['GET'])
def index():
    # TODO:
    # use sqlalchemy to create database and tables.....
    #
    messages = Message.query.order_by(Message.id.desc())
    return render_template('show_messages.html', messages=messages)

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

    message_handler = MessageHandler(app.config['LOG_TYPE'], app_name, message)
    message_handler.log_message()
    return json.dumps({'response': 'successful log'})
