'''
Default configuration
'''
from os import getenv, path

basedir = path.abspath(path.dirname(__file__))
basedir = "/".join(basedir.split("/")[:-2])

class Config(object):
    ENV = getenv('FLASK_ENV')
    DEBUG = ENV == 'development'
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
