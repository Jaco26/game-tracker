from db import db

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
