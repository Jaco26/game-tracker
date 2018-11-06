from flask_restful import Resource
from models.cities import Cities
from calculations.count import count
from calculations.map_city_connections import map_cities

class CitiesResource(Resource):
  def get(self):
    cities = [city.json() for city in Cities.query.all()]
    mapped_cities = map_cities(cities)
    # counted = count(cities)
    # connections = get_connections(cities)
    return { 
      # 'counted': counted,
      # 'connections': connections,
      'mapped_cities': mapped_cities,
    }
