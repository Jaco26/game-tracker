from flask_restful import Resource
from models.cities import Cities
from calculations.map_cities import map_cities


class CityByName(Resource):
  def get(self, name):
    cities = [city.json() for city in Cities.query.all()]
    city = next((c for c in cities if c['name'] == name), None)
    if city:
      return map_cities(city, cities)
    return { 'message': 'Sorry, but the city: {} was not found'.format(name) }
