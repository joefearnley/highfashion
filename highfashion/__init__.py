from flask import Flask
app = Flask(__name__)
app.config.from_object('highfashion.config.DevelopmentConfig')

import highfashion.views
