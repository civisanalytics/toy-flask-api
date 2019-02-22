import os
import logging
from flask import Flask
from flask_restful import Api

from server.health_check import HealthCheck
from server.url_shortener import UrlShortener
from server.url_lookup import UrlLookup
from server.url_hit_count import UrlHitCount

def create_app():
    app = Flask(__name__)
    app.debug = True

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-20s %(levelname)-6s %(message)s',
                        datefmt='%m-%d-%Y %H:%M:%S')
    return app


app = create_app()
api = Api(app, catch_all_404s=True)

api.add_resource(HealthCheck, '/healthz')
api.add_resource(UrlShortener, '/url_shorten')
api.add_resource(UrlLookup, '/url_lookup/<url_id>')
api.add_resource(UrlHitCount, '/url_hit_count/<url_id>')

if __name__ == '__main__':
    app.run()
