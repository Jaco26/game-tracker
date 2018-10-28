from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from resources.city_cards import CityCardResource

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)

api.add_resource(CityCardResource, '/api/citycards')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run()