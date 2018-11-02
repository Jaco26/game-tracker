
flatten = lambda l: [item for sublist in l for item in sublist]

# def flatten(l):
#   flattened = []
#   for sublist in l:
#     for item in sublist:
#       flattened.append(item)
#   return flattened

def exclude_ids_from(*args):
  ids_to_exclude = []
  for arg in args:
    if type(arg) is dict:
      ids_to_exclude.append(arg['id'])
    elif type(arg) is list:
      for a in arg:
        ids_to_exclude.append(a['id'])
  return ids_to_exclude

def get_unique_second_ring(city, cities, first_ring):
  exclude_ids = exclude_ids_from(city, first_ring)
  connection_ids = []
  for item in first_ring:
    item_city_connections = next(c['connections'] for c in cities if c['id'] == item['id'])
    connection_ids.append([cn_id for cn_id in item_city_connections if cn_id not in exclude_ids])
  return list(set(flatten(connection_ids)))

def get_first_ring(city, cities):
  result = []
  for connection in city['connections']:
    item = next((c for c in cities if c['id'] == connection), None)
    result.append({ 'name': item['name'], 'id': item['id'] })
  return result

def count_connections(cities):
  result = []
  city = cities[0]
  for city in cities:
    first_ring = get_first_ring(city, cities)
    unique_second_ring = get_unique_second_ring(city, cities, first_ring)
    result.append({
      'city_name': city['name'],
      'color': city['color'],
      'total': len([*first_ring, *unique_second_ring]),
      'n_first': len(first_ring),
      'n_second': len(unique_second_ring),
      # 'first_ring': first_ring,
      # 'second_ring': unique_second_ring,
    })
  return sorted(result, key=lambda x: x['total'], reverse=True)
