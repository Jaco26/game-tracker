from db import db
# from calculations.map_cities import map_cities
# from app import app

class Cities(db.Model):
  __tablename__ = 'cities'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  x_rat_key = db.Column(db.Integer)
  y_rat_key = db.Column(db.Integer)
  x_rat = db.Column(db.Float(precision=2))
  y_rat = db.Column(db.Float(precision=2))
  color = db.Column(db.String)
  connections = db.Column(db.ARRAY(db.Integer))

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'x_rat_key': self.x_rat_key,
      'y_rat_key': self.y_rat_key,
      'x_rat': self.x_rat,
      'y_rat': self.y_rat,
      'color': self.color,
      'connections': self.connections
    }
  
  def simple_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'connections': self.connections
    }

  def map_cities(self, name):
    cities = [city.simple_json() for city in self.query.all()]
    city = next((c for c in cities if c['name'] == name), None)
    if city:
      return map_cities(city, cities), 200
    return { 'message': 'Sorry, but the city: {} was not found'.format(name) }, 404

