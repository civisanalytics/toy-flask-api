import string
import short_url
from flask import request, make_response
from flask_restful import Resource
import urllib.parse as urlparse
from redis import Redis


class UrlShortener(Resource):

	def __init__(self):
		self.r = Redis()

	def post(self):
		url = request.form.get('url', None)
		if not url:
			return make_response('You must submit a url!', 400)

		self._validate_url(url)
		url_id = self._shorten_url(url)
		return make_response(url_id)

	@staticmethod
	def _validate_url(url):
		parts = urlparse.urlparse(url)
		if not parts.scheme in ('http', 'https'):
			return make_response('Please enter valid url!', 400)

	def _shorten_url(self, url):
		url_id = self.r.get('reverse-url:' + url)
		if url_id is not None:
			return url_id
		url_num = self.r.incr('last-url-id')
		url_id = short_url.encode_url(url_num)
		self.r.set('url-target:' + url_id, url)
		self.r.set('reverse-url:' + url, url_id)
		return url_id
