"""
This script runs the webshop application using a development server.
"""

from englishexercises import app
from os import environ

if __name__ == '__main__':
    #app = Flask(__name__)
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
