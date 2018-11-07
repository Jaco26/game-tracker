from flask_restful import Resource
from models.cities import Cities
import json

pp = lambda dct: print(json.dumps(dct, indent=2))
child_has_content = lambda dct: type(dct) is dict and len(dct) > 0

def process(city, cities, accum):
  pp(accum)  

def map_cities(cities):
  city = cities[0]
  accum = { city['id']: {c_id: {} for c_id in city['connections'] } }
  return process(city, cities, accum)


class TestResource(Resource):
  def get(self):
    cities = [city.simple_json() for city in Cities.query.all()]
    return map_cities(cities)