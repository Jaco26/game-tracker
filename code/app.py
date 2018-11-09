import socket
from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, Namespace, emit, disconnect
from resources.cities import CityByName

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)
socketio = SocketIO(app)

api.add_resource(CityByName, '/city/<string:name>')

@socketio.on('connect')
def connected():
  emit('connect', { 'hello': 'welcome' })

@socketio.on('userMessage')
def recieve_message(msg):
  print(msg)
  if msg.lower() == 'fuck':
    disconnect()

# @app.route('/cities/<string:name>')
# def hihi(name):
#   from calculations.map_cities import map_cities
#   return map_cities(name)

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  host = socket.gethostname()
  IPAddr = socket.gethostbyname(host)
  port = app.config['PORT']
  print("Server is callable at http://{}:{}/".format(IPAddr, port))
  socketio.run(app, host='0.0.0.0')
 
