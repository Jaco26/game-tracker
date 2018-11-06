from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from resources.cities import CitiesResource


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)

api.add_resource(CitiesResource, '/api/citycards')

@app.route('/')
def index():
  return '<h1>Hello</h1>'

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(host='0.0.0.0')