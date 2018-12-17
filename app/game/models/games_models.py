from datetime import datetime
from bson import ObjectId
import json

import requests as r
from mongoengine import Document, fields
from mongoengine.errors import DoesNotExist, MultipleObjectsReturned, FieldDoesNotExist
from mongoengine.queryset.visitor import Q
from app import app


class Games(Document):
    _id = fields.ObjectIdField()
    name_of_the_game = fields.StringField(
        required=True
    )
    team_individual = fields.StringField(
        required=True
    )
    minimum_no_of_players = fields.StringField(
        required=True
    )
    alcohol_involved = fields.StringField(
        required=True
    )
    app_to_be_downloaded = fields.StringField(
        required=True
    )
    description = fields.StringField(
        required=True
    )
    how_to_play_the_game = fields.StringField(
        required=True
    )
    example_videos = fields.StringField(
        required=True
    )
    links = fields.StringField(
        required=True
    )

    meta = {
        "collection": "games"
    }

    def get_all_games(self, result_per_page=10, page=1, querystring=None):
        """
        Get all games 

        """
        matching_query = {}

        page = 1 if page < 1 else page
        items_per_page = 1 if result_per_page < 1 else result_per_page
        offset = (page-1) * items_per_page
        if querystring:

            matching_query['name_of_the_game__icontains'] = querystring

        all_games = (self.__class__.objects(
            **matching_query).order_by('name_of_the_game').skip(offset).limit(items_per_page)
        )

        if len(all_games):
            response = {
                'code': r.codes.OK,
                'data': {
                    'games': json.loads(all_games.to_json())
                }
            }
        else:
            response = {
                'code': r.codes.NO_CONTENT,
                'data': {
                    'message': 'NOT FOUND'
                }
            }
        return response

    def get_one(self, game_oid):
        """
        Get single game matching game_oif with self._id

        Parameters
        ----------

        :type game_oid : ObjectId
            (required)

        Returns
        -------
        :type response : dict
            response dict with status code and data
        :response code : int
            http status code
        :response object : queryObject
            mongoengine queryObject, when status code is 200
        :response data : dict
            response data : dictionary

        """
        try:
            game_object = self.__class__.objects(_id=game_oid).first()

            if not game_object:
                response = {
                    'code': r.codes.NOT_FOUND,
                    'data': {
                        'message': 'Game not found'
                    }
                }
            else:
                response = {
                    'code': r.codes.OK,
                    'data': {
                        'game': json.loads(game_object.to_json())
                    }
                }

        except Exception as e:
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'SERVER_ERROR',
                    'exception': str(e)
                }
            }

        return response

    def search(self, params):
        """
        search game by number_people , team and individual
        Parameters
        ----------

        :type params : dict
            [search query parameters]
        :params search_by : str
            (required)[choice:keyword, minimum_no_of_players, team_or_individual]
        :params querystring : str
            (required)

        Return
        ------
        :type response : dict
            response dict with status code and data
        :response code : int
            http status code
        :response object : queryObject
            mongoengine queryObject, when status code is 200
        :response data : dict
            response data : dictionary

        """

        if params['search_by'].upper() == "MINIMUM_NO_OF_PLAYERS":
            game_objects = self.__class__.objects().filter(
                minimum_no_of_players__icontains=params['querystring']
            )
            response = {
                'code': r.codes.OK,
                'data': {
                    'games': json.loads(game_objects.to_json())
                }
            }
        if params['search_by'].upper() == "TEAM_OR_INDIVIDUAL":
            game_objects = self.__class__.objects().filter(
                team_individual__icontains=params['querystring'].lower()
            )
            response = {
                'code': r.codes.OK,
                'data': {
                    'games': json.loads(game_objects.to_json())
                }
            }

        else:
            game_objects = self.__class__.objects().filter(
                Q(
                    name_of_the_game__icontains=params['querystring'].lower()
                ) | Q(
                    description__icontains=params['querystring'].lower()
                ) | Q(
                    minimum_no_of_players__icontains=params['querystring']
                )
            )

            response = {
                'code': r.codes.OK,
                'data': {
                    'games': json.loads(game_objects.to_json())
                }
            }
        return response
