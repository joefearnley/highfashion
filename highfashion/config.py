class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = '' # dbtype://user@localhost/foo
    LOG_TYPE = ''                # filesystem or database
    LOG_FILE_NAME = ''           # path/to/highfashion.log

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://highfashion:password@localhost/highfashion'
    LOG_TYPE = 'database'
    LOG_FILENAME = 'highfashion.log'
