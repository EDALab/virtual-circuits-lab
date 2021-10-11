import pymongo

# Connect to local MongoDB server at default config port 27017
connection_str = "mongodb://localhost:27017/"
client = pymongo.MongoClient(connection_str, serverSelectionTimeoutMS=5000)
db = client.virtualCircuitLab

# Subcircuit collection ref
subcircuit_templates_collection = db["subcircuitTemplates"]