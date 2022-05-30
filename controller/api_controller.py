from flasgger import LazyString, Swagger, swag_from, LazyJSONEncoder
from flask import request
from app import app

# from chatbot_controller import ChatBot

app.json_encoder = LazyJSONEncoder

swagger_template = {'info': {
    'title': LazyString(lambda: 'My first Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a Swagger UI document and implements Chatbot '
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


@swag_from("../api_description/generative_chatbot_api.yml", "yml", None, ['GET'])
@app.route('/start_chat_bot')
def start_chat():
    # chatbot = ChatBot()
    # chatbot.start_chat()
    return 'Starting chatbot...'


@swag_from("../api_description/generative_chatbot_api.yml", "yml", None, ['GET'])
@app.route('/send/<input>')
def get_response(input):
    # chatbot = ChatBot()
    # response = chatbot.generate_response(input)
    return 'Chatbot: '  # + response
