
def count_second_connections(main_city, cities):
  counted_cities = []
  count = 0
  connection_ids = main_city['connections']
  # for each connection_id, 
  for _id in connection_ids:
    # find the associated city
    city = next((item for item in cities if item['id'] == _id), None)
    # count this city's connection ids and omit the ones that are included in the main_city's connections'
    city_new_connection_count = len([con_id for con_id in city['connections'] if con_id not in connection_ids])
    count += city_new_connection_count
    counted_cities.append({
      'city_name': city['name'],
      'connection_count': city_new_connection_count
    })
  return {
    'count': count,
    'cities': counted_cities,
  }



# def count_second_connections(city, cities):
#   total = 0
#   individual = []
#   for connection_id in city['connections']:
#     connection_city = next((item for item in cities if item['id'] == connection_id), None)
#     total += len(connection_city['connections'])
#     individual.append({
#       'name': connection_city['name'],
#       'count': len(connection_city['connections']) - 1,
#     })
#   return {
#     'second_and_first_count': total,
#     'individual': individual
#   }


def get_city_connections(city, cities):
  direct_connection_count = len(city['connections'])
  connected_cities = count_second_connections(city, cities)
  return {
    'connection_count': direct_connection_count,
    'connected_cities': connected_cities,
  }


def get_city_risk(cities):
  result = []
  for city in cities:
    result.append({
      'city_name': city['name'],
      'city_id': city['id'],
      'city_connections': get_city_connections(city, cities),
    })
  # return sorted(result, reverse=True, key=lambda c: c['city_connections']['connected_cities']['second_and_first_count'])
  return sorted(result, reverse=True, key=lambda c: c['city_connections']['connected_cities']['count'])


if __name__ == '__main__':
  print("You can't just run this file :(")