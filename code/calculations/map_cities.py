from models.cities import Cities

pp = lambda dct: print(json.dumps(dct, indent=2))
flat = lambda lst: [item for sub_l in lst for item in sub_l]

def item_not_in(lst_2d, item):
  for lst in lst_2d:
    if item in lst:
      return False
  return True

def add_cities(levels, cities):
  accum = []
  for l in levels:
    inner = []
    for item in l:
      city = next((c for c in cities if c['id'] == item), None)
      inner.append({
        'name': city['name'],
        'id': city['id'],
      })
    accum.append(inner)
  return accum

def get_next_level(cities, ids):
  accum = []
  for _id in ids:
    ct = next((c for c in cities if c['id'] == _id), None)
    accum.append(ct['connections'])
  unique = list(set(flat(accum)))
  return unique

def process(cities, locus_city):
  levels = []
  for n in range(4):
    if n == 0:
      levels.append([_id for _id in locus_city['connections']])
    else:
      next_level = get_next_level(cities, levels[n - 1])
      filtered_next_level = [_id for _id in next_level if item_not_in(levels, _id) and locus_city['id'] != _id]
      levels.append(filtered_next_level)
  levels_with_cities = add_cities(levels, cities)
  return {
    'name': locus_city['name'],
    'id': locus_city['id'],
    'connections': levels_with_cities,
  }
 
def map_cities(city, cities):
  result = process(cities, city)
  return result

