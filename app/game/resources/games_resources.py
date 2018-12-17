import json
from bson import ObjectId

import requests as r
from flask import request
from flask_restful import Resource, reqparse
from app.game.models.games_models import Games
from app import app
from app.libs.response_utils import ResponseUtil


class GamesResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        """
        Get all games
        """

        self.parser.add_argument(
            'limit', required=False, type=int, location='args'
        )
        self.parser.add_argument(
            'page', required=False, type=int, location='args'
        )
        self.parser.add_argument(
            'querystring', required=False, type=str, location='args'
        )

        self.args = self.parser.parse_args()
        response = Games().get_all_games(
            self.args['limit'], self.args['page'], self.args['querystring'])

        return ResponseUtil(response['code']).json_response(response['data'])


class GameSearchResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):

        _search_by = [
            'keyword',
            'minimum_no_of_players',
            'team_or_individual'
        ]

        self.parser.add_argument(
            'search_by', required=False, type=str, choices=_search_by, location='args'
        )
        self.parser.add_argument(
            'querystring', required=False, type=str, location='args'
        )
        self.args = self.parser.parse_args()

        response = Games().search(self.args)
        return ResponseUtil(response['code']).json_response(response['data'])


class GameSingleResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, game_id):
        """ 
        Get single game by game_id
        :game_id : str

        """

        if not ObjectId.is_valid(game_id):
            response = {
                'code': r.codes.BAD_REQUEST,
                'data': {
                    'message': 'game game_id is not a valid objectId'
                }
            }
        else:
            response = Games().get_one(ObjectId(game_id))

        return ResponseUtil(response['code']).json_response(response['data'])
