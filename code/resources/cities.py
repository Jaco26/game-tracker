from flask_restful import Resource
from models.city_cards import CityCards
from calculations.city_connections import count_connections

class CityCardResource(Resource):
  def get(self):
    cities = [city_card.json() for city_card in CityCards.query.all()]
    return count_connections(cities)

