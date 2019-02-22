import json
from flask import make_response, jsonify
from flask_restful import Resource
from redis import Redis


class UrlHitCount(Resource):

	def __init__(self):
		self.r = Redis()

	def get(self, url_id):
		data = self._get_url_hits(url_id)
		return make_response(json.dumps(data))

	def _get_url_hits(self, url_id):
		url = self.r.get('url-target:' + url_id)

		if url is None:
			return make_response('Not Found', 404)

		click_count = int(self.r.get('click-count:' + url_id) or 0)
		return {'url_id': url_id, 'click_count': click_count, 'url': url.decode("utf-8")}
