from flask_restful import Resource
from models.city_cards import CityCards

class CityCardResource(Resource):
  def get(self):
    return [city_card.json() for city_card in CityCards.query.all()]