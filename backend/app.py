import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from authAPI import auth
from userAPI import user
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger

app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)
swagger = Swagger(app)

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Social Book"
    },
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.config["MONGO_URI"] = "mongodb://localhost:27017/social-media"
mongo = PyMongo(app)

app.secret_key = 'secret key'
app.config['JWT_SECRET_KEY'] = 'this-is-the-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=120)


app.register_blueprint(auth)
app.register_blueprint(user)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)
