from flask import request
from flask_socketio import Namespace, emit, join_room
from calculations.map_cities import map_cities
from models.cities import Cities


class Game(Namespace):
  def on_connect(self):
    # cities = [c.json() for c in Cities.query.all()]
    # accum = []
    # for city in cities:
    #   accum.append(map_cities(city, cities))
    # emit('connected', accum, broadcast=True)
    emit('connected', 'connected', broadcast=False)

  def on_joinRoom(self, data):
    join_room(data['room'])
    emit('userJoined', request.sid, room=data['room'], include_self=False)

  def on_newMessage(self, data):
    emit('messageRecieved', data, room='myRoom', include_self=True)
