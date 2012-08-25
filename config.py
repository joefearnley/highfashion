class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
    LOG_TYPE = ''
    LOG_FILE_NAME = ''

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://highfashion:password@localhost/highfashion'
    LOG_TYPE = 'database'
    LOG_FILENAME = 'highfashion.log'
