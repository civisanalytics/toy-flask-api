from flask import make_response
from flask_restful import Resource
from redis import Redis


class UrlLookup(Resource):

	def __init__(self):
		self.r = Redis()

	def get(self, url_id):
		url = self._lookup_url(url_id)
		return make_response(url)

	def _lookup_url(self, url_id):
		link_target = self.r.get('url-target:' + url_id)
		if link_target is None:
			return make_response('Not found', 404)
		self.r.incr('click-count:' + url_id)
		return link_target
