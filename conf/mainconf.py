import os
from flask import Config


class DevelopmentConfig(Config):
    MONGODB_DATABASE = "mydb"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = "game_user"
    MONGODB_PASSWORD = "game_user"


class ProductionConfig(Config):
    MONGODB_DATABASE = "mydb"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = "game_user"
    MONGODB_PASSWORD = "game_user"
