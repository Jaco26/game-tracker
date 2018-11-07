from flask_restful import Resource
from models.cities import Cities
import json

pp = lambda dct: print(json.dumps(dct, indent=2))
child_has_content = lambda dct: type(dct) is dict and len(dct) > 0

def recurse(accum, prev_key, cities):
  keys = list(dict.keys(accum))
  for k in keys:
    if child_has_content(accum[k]):
      next_level = accum[k]
      recurse(next_level, k, cities)
    else:
      city = next((ct for ct in cities if ct['id'] == k))
      accum[k] = { c_id: {} for c_id in city['connections'] if c_id != prev_key}  

def process(cities, prev_key, accum):
  recurse(accum, prev_key, cities)
  return accum

def map_cities(cities):
  city = cities[0]
  accum = { city['id']: {c_id: {} for c_id in city['connections'] } }
  result = {}
  for n in range(5):
    result = process(cities, city['id'], accum)
  return result


class TestResource(Resource):
  def get(self):
    cities = [city.simple_json() for city in Cities.query.all()]
    return map_cities(cities)