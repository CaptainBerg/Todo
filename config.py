import os
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = "abcde"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# MONGODB_SETTINGS = {'DB': 'todo'}
WTF_CSRF_ENABLED = False
DEBUG=True
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
