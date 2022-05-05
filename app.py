from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from markupsafe import escape

import chatbot

app = Flask(__name__)


app.json_encoder = LazyJSONEncoder

swagger_template = {'info': {
    'title': LazyString(lambda: 'My first Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a sample Swagger UI document and implements Hello World '
                                      'functionality after executing GET.'),
}, 'host': LazyString(lambda: request.host)}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'hello_world',
            "route": '/generative_chatbot_api.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}

swagger = Swagger(app, swagger_config, swagger_template)


@swag_from("generative_chatbot_api.yml", "yml", None, ['GET'])
@app.route('/hello')
def hello_world():
    return 'Hello World!'


@swag_from("generative_chatbot_api.yml", "yml", None, ['GET'])
@app.route('/get')
def get_response():
    # output_message = chatbot.get_output()
    # return output_message
    return 'Chatbot: ' + 'Generated message...'


@swag_from("generative_chatbot_api.yml", "yml", None, ['GET'])
@app.route('/send/<input>')
def send_message(input):
    return f'User: {escape(input)}'


if __name__ == '__main__':
    app.run()
