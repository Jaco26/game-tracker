
# flatten = lambda l: [item for sublist in l for item in sublist]

def flatten(l):
  flattened = []
  for lst in l:
    for item in lst:
      flattened.append(item)
  return flattened

def get_unique_second_ring(city, cities, first_ring):
  exclude_ids = [city['id'], *[x['id'] for x in first_ring]]
  print(exclude_ids)
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
  first_ring = get_first_ring(city, cities)
  unique_second_ring = get_unique_second_ring(city, cities, first_ring)
  return {
    'city_name': city['name'],
    'first_ring': first_ring,
    'second_ring': unique_second_ring,
  }
