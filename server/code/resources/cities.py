from flask_restful import Resource
from models.city_cards import CityCards
from calculations.city_risk import get_city_risk

class CityCardResource(Resource):
  def get(self):
    cities = [city_card.json() for city_card in CityCards.query.all()]
    return get_city_risk(cities)

