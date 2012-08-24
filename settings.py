class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    LOG_TYPE = ''
    LOG_FILE_NAME = ''

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://highfashion@localhost/db'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = ''
    LOG_TYPE = 'filesystem'
    LOG_FILENAME = 'highfashion.log'
