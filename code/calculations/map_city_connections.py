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

def simple_cities(cities):
  def small_city_dict(x):
    return {
      'id': x['id'],
      'connections': x['connections']
    }
  return [small_city_dict(city) for city in cities]

def inject_value(**kwargs):

  path = kwargs['path']
  dct = kwargs['dct']
  parent_val = kwargs['parent_val']
  val_to_inject = kwargs['new_val']
  reducable = dct # make another reference to 'dct' to recurse into
  # for each value in 'path', recurse into 'dct'
  for i, n in enumerate(path):
    if i == len(path) - 1:
      # this is the level on which to inject
      reducable[n] = val_to_inject
      return dct
    reducable = reducable[n]

  # print(dct)


def make_go(**kwargs):
  city = kwargs['city']
  path = [1, 8, 15]
  value = {'message': 'we did it!'}
  return inject_value(path=path, dct=sample, parent_val=city['id'], new_val=value)
  # return 'Hey how are ya?'


def map_cities(full_cities):
  cities = simple_cities(full_cities)
  city_ids = [city['id'] for city in cities]
  test_city = cities[0]
  result = make_go(city_ids=city_ids, cities=cities, city=test_city)
  return result