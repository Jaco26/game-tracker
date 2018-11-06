"""
{
  1: {
      8: {
        15: {
          
        },
        3: {

        },
        37: {

        },
        19: {

        }
      },
      15: {
        8: {

        },
        1: {

        },
        30: {

        },
        32: {

        },
        3: {

        }
      },
      36: {

      },
      26: {

      },
  }
 
}

Need to know:
  - city_id <int>
  - city_connection_ids <int[]>

"""
flatten = lambda l: [item for sublist in l for item in sublist]

def simple_cities(cities):
  def small_city_dict(x):
    return {
      # 'name': x['name'],
      'id': x['id'],
      'connections': x['connections']
    }
  return [small_city_dict(city) for city in cities]

def get_ids_to_exclude(*args):
  ids_to_exclude = []
  for arg in args:
    if type(arg) is dict:
      ids_to_exclude.append(arg['id'])
    elif type(arg) is list:
      for a in arg:
        ids_to_exclude.append(a['id'])
  return ids_to_exclude

def get_next_ring(already_counted, accum, city, cities):
  print('already counted', already_counted)
  if len(already_counted) == 20:
    return accum
  connections = city['connections']
  accum.append(connections)
  for con in connections:
    already_counted.append(con)
  unique_already_counted = list(set(already_counted))
  next_cities = [c for c in cities if c['id'] in connections and c['id'] not in unique_already_counted]
  print(accum)
  for c in next_cities:
    get_next_ring(unique_already_counted, accum, c, cities)



def get_connections(input_cities):
  cities = simple_cities(input_cities)
  final = []
  for city in cities:
    if city['id'] == 1:
      already_counted = []
      accum = []
      result = get_next_ring(already_counted, accum, city, cities)
      final.append(result)
  return final,








# def get_connections(input_cities):

#   def find_rings(city_connections, city, cities):

#     def recursor(city_connections, city, cities):
#       inner_result = []
#       if len(city_connections) < 5:
#         for id_item in city['connections']:
#           city_list = [ct for ct in cities if ct['id'] == id_item]
#           for c in city_list:
#             inner_result.append({
#               'id': c['id'],
#               'name': c['name'],
#               'connections': c['connections'],
#             })
#         city_connections.append(inner_result)

#         recursor(city_connections, city, cities)
#       return city_connections


#     return recursor(city_connections, city, cities)
    


#   def main(input_cities):
#     # return a list of dictionaries with a city_id as key and a dict with city name and 2D list of conenctions
#     result = [] 
#     cities = reduce_cities(input_cities)
#     for city in cities:
#       city_connections = [] # recursively populate with lists of city connection ids
#       result.append({
#         'id': city['id'],
#         'name': city['name'],
#         'connections': find_rings(city_connections, city, cities),
#       })
#     return result
  
#   return main(input_cities)
    

