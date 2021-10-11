from flask_restful import Resource
from flask import request
from model.SubcircuitTemplate import SubcircuitTemplate
from MongoConnection import subcircuit_templates_collection

# This class is what is connected to the endpoint (subcircuit). This will be used to store the subcircuit in
# the database. It will also be used to retrieve a subcircuit based on "name."
class SubCktGenerator(Resource):

    @classmethod
    def post(cls):
        subcircuit_json = request.get_json()

        # Check for duplicate subcircuit
        if subcircuit_templates_collection.find({"subcircuit_name": subcircuit_json["name"]}).count():
            return f"Subcircuit with name {subcircuit_json['name']} already exists", 400

        # Create subcircuit template to persist in database
        subcircuit_template = SubcircuitTemplate(
            subcircuit_json["name"], subcircuit_json["partType"], subcircuit_json["isBlackBox"], subcircuit_json["components"], subcircuit_json["connect"])
        
        # Save subcircuit template to database
        subcircuit_templates_collection.insert_one(subcircuit_template.to_dict())

        return f"Subcircuit {subcircuit_json['name']} successfully created.", 201

