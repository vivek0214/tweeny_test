
import os
import pymongo
from flask import Flask
from mongoengine import connect
# from werkzeug.contrib.fixer import ProxyFix

""" initialize flask app """
app = Flask(__name__)

environment = os.environ.get('game_env', 'development')

""" Setting up the environment from mainconf """
if environment == "production":
    app.config.from_object('conf.mainconf.ProductionConfig')
else:
    app.config.from_object('conf.mainconf.DevelopmentConfig')

""" initialize the logger """

logger = app.logger
logger.setLevel('DEBUG')

""" initialize mongo db object """

try:
    db = connect(
        host="mongodb://{0}:{1}@localhost:27017/{2}".format(
            app.config.get('MONGODB_USERNAME'),
            app.config.get('MONGODB_PASSWORD'),
            app.config.get('MONGODB_DATABASE')
        )
    )
    dbnames = db.database_names()
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)

# import the dependencies
from app.game.routes.games_routes import *
