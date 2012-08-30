Highfashion Log (all new for girls!) (From Blammo!)
==========

Highfashion is a server for logging messages remotely via HTTP. It consists of a REST API and a web UI if configured accordingly.

Dependencies
-----------
I'm not sure. I starting building this a while ago and started with
Flask via pip as I think it installs most the pacakges below. Here is my
pip freeze output for the virtual environment I used for development: 

    Flask==0.9
    Flask-SQLAlchemy==0.16
    Jinja2==2.6
    MySQL-python==1.2.3
    SQLAlchemy==0.7.8
    Werkzeug==0.8.3
    argparse==1.2.1
    wsgiref==0.1.2

Configuration
-----------
You can config highfashion to log messages one of two ways. Either a database or
using python's standard logging library. If the application is not
configured to use either of these, it just prints to stdout. I choose the application configuration method suggested in the Flask docs for here:

[http://flask.pocoo.org/docs/config/](http://flask.pocoo.org/docs/config/)

* To log messages to the appropriate place, see and edit the `/highfashion/config.py` file (class) accordingly.
* Then edit the `/highfashion/__init.py__` file with the correct config
  class you want to use.

API
-----------
The main part of the application is a REST API. If required parameters
are not met, a error string will be returned (e.g.):

    {
        'error': 'No [parameter] is specified'
    }

When a HTTP POST is successful, a response in the following format will
be returned:

    {
        "response": "successful log"
    }

###Endpoints
**POST /log**

<table>
  <tr><th><strong>Parameters</strong></th><th>&nbsp;</th></tr>
  <tr><td>app</td><td>The name of the application logging the message.</td></tr>
  <tr><td>message</td><td>The message to be logged.</td></tr>
</table>

License
-----------
Do what ever you want with it. I don't give a shit.

