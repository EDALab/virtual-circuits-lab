import PySpice.Logging.Logging as Logging 
from PySpice.Spice.Netlist import Circuit, SubCircuit
from PySpice.Unit import *

def get_node_label(node):
    return "n" + str(node)
    
# This is a class that breaks down a JSON and creates a Subcircuit netlist.
# This class uses PySpice to create the netlist. This class can be used to be used for simulations.
# There should be a database query in here.
class SubCkt(SubCircuit):

    # Change constructor to take in name as parameter
    # Remove line 15 that searches for components. Components will now be directly passed in as a value to the constructor
    def __init__(self, subcircuit_name, subcircuit_components):
        self.__name__ = subcircuit_name
        # Get components that make up subcircuit 
        elements = subcircuit_components
        # Extract input and output nodes of subcircuit
        ports = elements.pop('P')
        nodes = []
        for port in ports:
            if port["node1"] == "gnd":
                nodes.append(get_node_label(port["node2"]))
            elif port["node2"] == "gnd":
                nodes.append(get_node_label(port["node1"]))

        # self.__nodes__ = nodes[::-1]
        self.__nodes__ = nodes
        # Initialize subcircuit netlist using PySpice SubCircuit module
        SubCircuit.__init__(self, self.__name__, *self.__nodes__)
        # build netlist
        for element in elements:
            if element == "R":
                for resistor in elements["R"]:
                    self.R(resistor["id"], get_node_label(resistor["node1"]), get_node_label(resistor["node2"]), resistor["value"]@u_Ohm)

            elif element == "L":
                for inductor in elements["L"]:
                    self.L(inductor["id"], get_node_label(inductor["node1"]), get_node_label(inductor["node2"]), inductor["value"]@u_H)

            elif element == "C":
                for capacitor in elements["C"]:
                    self.C(capacitor["id"], get_node_label(capacitor["node1"]), get_node_label(capacitor["node2"]), capacitor["value"]@u_F)

    
