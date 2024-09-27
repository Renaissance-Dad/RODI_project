import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'ce4ea7ff8704fab7762fae559e4072ba' 
    WTF_CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing

config = {
    'development': Config,
    'testing': TestingConfig,
    'default': Config
}