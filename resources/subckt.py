from flask_restful import Resource
from flask import request
from spice.subckt import SubCkt


class SubCktGenerator(Resource):

    @classmethod
    def post(cls):
        subcircuit_json = request.get_json()
        # Get subcircuit netlist
        subcircuit = SubCkt(subcircuit_json)
        print(subcircuit)

        print("Method called from SubCktGenerator in Resources")
        return "Successful", 201