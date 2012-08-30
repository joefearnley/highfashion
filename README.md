High Fashion Log (all new for girls!) (From Blammo!)
==========

High Fashion Log is server for logging messages remotely via HTTP. It consists of a REST API and a web-based UI if you configure it accordingly.

Dependencies
-----------
I'm not sure. I starting building this a while ago and started with
Flask via pip as I think it installs most of these pacakges. Here is my
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
You can config highfashion to log one of two ways. Either a database or
using python's standard logging library. If the application is not
configured to use either of these, it just prints to stdout. I choose to
used the configuration method suggested in the Flask docs for here:

[http://flask.pocoo.org/docs/config/](http://flask.pocoo.org/docs/config/)

* To messages to the appropriate place, see and/or edit the `/highfashion/config.py` file (class) accordingly.
* Then edit the `/highfashion/__init.py__ file with the correct config
  class you want to use.

API
-----------

####GET / 
The main index of the application. If you configure it to use a database
to log messages, they will be displayed here.

####POST /log


License
-----------
Do what ever you want with it. I don't give a shit.

