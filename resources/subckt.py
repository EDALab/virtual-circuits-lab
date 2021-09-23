from flask_restful import Resource
from flask import request
from spice.subckt import SubCkt

# Makeshift database.
subcircuit_objects = []

# This class is what is connected to the endpoint (subcircuit). This will be used to store the subcircuit in
# the database. It will also be used to retrieve a subcircuit based on "name."
class SubCktGenerator(Resource):

    @classmethod
    def post(cls):
        subcircuit_json = request.get_json()
        # Create subcircuit creates a subcircuit python object with necessary information
        subcircuit_obj = SubCktObject(subcircuit_json)
        
        global subcircuit_objects
        subcircuit_objects.add(subcircuit_obj)

        print("Method called from SubCktGenerator in Resources")
        return "Successful", 200

    # What do we need to store of a subcircuit?
    # - Name
    # - JSON (in the case of NoSQL db)

class SubCktObject():

    def __init__(self, subcircuit_json):
        self._name = subcircuit_json["name"]
        self._part_type = subcircuit_json["partType"]
        self._is_black_box = subcircuit_json["isBlackBox"]
        self._subcircuit_components = subcircuit_json["components"]
        self._connect = subcircuit_json["connect"]
    
    @property
    def name(self):
        return self._name

    @property
    def part_type(self):
        return self._part_type

    @property
    def is_black_box(self):
        return self._is_black_box

    @property
    def subcircuit_components(self):
        return self._subcircuit_components
    
    @property
    def connect(self):
        return self._connect
    

    # {'name': 'Test1', 
    # 'partType': 'subcircuitTwoPort', 
    # 'isBlackBox': False, 
    # 'components': {'P': [{'id': 'P_2', 'name': 'P_2', 'value': 0, 'node1': '1', 
    # 'node2': 'gnd'}, {'id': 'P_1', 'name': 'P_1', 'value': 0, 'node1': '5', 'node2': 'gnd'}], 
    # 'R': [{'id': 'R_2', 'name': 'R_2', 'value': 10000, 'node1': '3', 'node2': '1'}, {'id': 'R_1', 
    # 'name': 'R_1', 'value': 10000, 'node1': '5', 'node2': '4'}], 'C': [{'id': 'C_1', 'name': 'C_1',
    #  'value': 0.0001, 'node1': '4', 'node2': '3'}]}, 
    #  'connect': ['', '']}