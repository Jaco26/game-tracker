from flask_restful import Resource
from models.cities import Cities
import json

pp = lambda dct: print(json.dumps(dct, indent=2))
flat = lambda lst: [item for sub_l in lst for item in sub_l]
child_has_content = lambda dct: type(dct) is dict and len(dct) > 0

def item_not_in(lst_2d, item):
  pp(lst_2d)
  for lst in lst_2d:
    if item in lst:
      return False
  return True

def get_next_level(cities, ids):
  accum = []
  for _id in ids:
    ct = next((c for c in cities if c['id'] == _id), None)
    accum.append(ct['connections'])
  # print(flat(accum))
  unique = list(set(flat(accum)))
  return unique

def process(cities, locus_city):
  # 2D list: each inner list being the unique city 
  # connections of a given level of connection to the locus_city
  levels = []
  for n in range(4):
    if n == 0:
      levels.append(locus_city['connections'])
    else:
      next_level = get_next_level(cities, levels[n - 1])
      # print(next_level)
      filtered_next_level = [_id for _id in next_level if item_not_in(levels, _id) and locus_city['id'] != _id]
      levels.append(filtered_next_level)
  return {
    'name': locus_city['name'],
    'id': locus_city['id'],
    'connections': levels,
  }

  
def map_cities(cities):
  city = cities[6]
  result = process(cities, city)
  return result


class TestResource(Resource):
  def get(self):
    cities = [city.simple_json() for city in Cities.query.order_by(Cities.id).all()]
    return map_cities(cities)


# def map_cities(cities):
#   city = cities[0]
#   accum = { city['id']: { c_id: {} for c_id in city['connections'] } }
#   result = {}
#   for n in range(5):
#     result = process(cities, city['id'], accum)
#   return result


# def recurse_build_dict(accum, prev_key, cities):
#   keys = list(dict.keys(accum))
#   for k in keys:
#     if child_has_content(accum[k]):
#       next_level = accum[k]
#       recurse_build_dict(next_level, k, cities)
#     else:
#       city = next((ct for ct in cities if ct['id'] == k))
# #       accum[k] = { c_id: {} for c_id in city['connections'] if c_id != prev_key}  

# def process(cities, prev_key, accum):
#   recurse_build_dict(accum, prev_key, cities)
#   return accum