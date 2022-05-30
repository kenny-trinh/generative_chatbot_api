from flask import Flask
from controller import api_controller

app = Flask(__name__)

if __name__ == '__main__':
    api_controller.app.run()

