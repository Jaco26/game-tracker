sample = {
  1: {
    8: {
      # exclude 1 because it is the direct parent value
      15: {},
      3: {},
      37: {},
      19: {},
    },
    15: {},
    36: {},
    26: {},
  }
}

def build_injectable(city):
  accum = {}
  for n in city['connections']:
    accum[n] = {}
  return accum

def simple_cities(cities):
  def small_city_dict(x):
    return {
      'id': x['id'],
      'connections': x['connections']
    }
  return [small_city_dict(city) for city in cities]

def inject_value(accum, path, val_to_inject):
  """Recurse into a dictionary along a given path and inject an item as the value associated with 
  the key that matches the last item in the path given"""
  reducable = accum # make another reference to 'accum' to recurse into
  # for each value in 'path', recurse into 'accum'
  for i, n in enumerate(path):
    if i == len(path) - 1:
      # this is the level on which to inject
      reducable[n] = val_to_inject
      return accum
    reducable = reducable[n]

def process_cities(accum, path, city, cities, count):
  if count == 2:
    print('PATH', path)
    print('ACCUM', accum)
    return accum
  new_val = build_injectable(city)
  accum = inject_value(accum, path, new_val)
  count += 1
  path.append(city['id'])
  print('count', count)
  for c_id in city['connections']:
    c = [ct for ct in cities if ct['id'] == c_id]
    # add the current city's id to the path 
    process_cities(accum, path, c[0], cities, count)

def make_go(city, cities):
  accum = {}
  path = [city['id']]
  return process_cities(accum, path, city, cities, 0)
  # city = kwargs['city']
  # path = [1, 8, 15]
  # new_val = {'message': 'we did it!'}
  # return inject_value(sample, path, city['id'], new_val)
  



def map_cities(full_cities):
  cities = simple_cities(full_cities)
  test_city = cities[0]
  result = make_go(test_city, cities)
  return {'result': result}

























# def build_ordinal_city_connections(root_city, cities, accum):
#   """Build 2D list of city ids. This will be an ordinal representation of 
#   a city's connectedness to other cities. the first list in the list will have 1
#   element––the root city's id"""
#   if len(accum) > 0:
#     # iterate through the list at the last index of accum and get t


#   # accum.append([root_city['id']]) if len(accum) == 0 else accum.append(root_city['id'])
#   for connection_id in root_city['connections']:
#     city = next((c for c in cities if c['id'] == connection_id), None)
#     if city:
      
      
#     # build_ordinal_city_connections(city, cities)
