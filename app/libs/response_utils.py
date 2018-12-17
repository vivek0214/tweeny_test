import json

import requests
from flask import Response
from app import app


class ResponseUtil:
    def __init__(self, code=None):
        self.code = code

    def json_response(self, data={}):
        if self.code is None:
            self.code = requests.codes.OK

        try:
            json_response = json.dumps(data)
        except Exception as e:
            app.logger.debug("ResponseUtil.json_response error{}".format(e))
            json_response = json.dumps({})
        http_response = Response(
            response=json_response,
            status=self.code,
            mimetype='application/json'
        )
        return http_response
