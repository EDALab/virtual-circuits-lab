from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS 

from resources.simulate import StaticSimulator, TransientSimulator

app = Flask(__name__)
CORS(app)

# ----------------------------create app----------------------------
api = Api(app)

api.add_resource(StaticSimulator, "/static_simulator/<string:name>")
api.add_resource(TransientSimulator, "/transient_simulator/<string:name>")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
