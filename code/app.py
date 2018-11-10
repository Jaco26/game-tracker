import socket
from flask import Flask, request
from flask_restful import Api
from flask_socketio import SocketIO, Namespace, emit, join_room, rooms
from resources.cities import CityByName

from namespaces.game import Game

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)
socketio = SocketIO(app)

api.add_resource(CityByName, '/city/<string:name>')

socketio.on_namespace(Game('/'))


if __name__ == '__main__':
  from db import db
  db.init_app(app)
  host = socket.gethostname()
  IPAddr = socket.gethostbyname(host)
  port = app.config['PORT']
  print("Server is callable at http://{}:{}/".format(IPAddr, port))
  socketio.run(app, host='0.0.0.0')
 
