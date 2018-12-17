from flask_restful import Api
from app.game.resources.games_resources import GameSingleResource, GamesResource, GameSearchResource
from app import app

api = Api(app)
# api for get single game by mataching game id
api.add_resource(
    GameSingleResource, '/api/game/<game_id>', endpoint='game_single_resource'
)
# Api for get all game

api.add_resource(
    GamesResource, '/api/games', endpoint='games_resource'
)


# search api for all the games

api.add_resource(
    GameSearchResource, '/api/gamesearch', endpoint='game_search_resource'
)
