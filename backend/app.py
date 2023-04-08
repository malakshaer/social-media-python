from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from authAPI import auth
from userAPI import user

app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)

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
