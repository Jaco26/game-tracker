from db import db

class Games(db.Model):
  __tablename__ = 'games'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40))
  turns = db.relationship('Turns', lazy='dynamic')
  players = db.relationship('Players', lazy='dynamic')