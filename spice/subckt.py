import PySpice.Logging.Logging as Logging 
from PySpice.Spice.Netlist import Circuit, SubCircuit
from PySpice.Unit import *

class SubCkt(SubCircuit):

    def __init__(self, subcircuit_json):
        self.__name__ = subcircuit_json["name"]
        # Get components that make up subcircuit 
        elements = subcircuit_json["components"]
        # Extract input and output nodes of subcircuit
        ports = elements.pop('P')
        nodes = []
        for port in ports:
            if port["node1"] == "gnd":
                nodes.append(port["node2"])
            elif port["node2"] == "gnd":
                nodes.append(port["node1"])

        self.__nodes__ = nodes[::-1]
        # Initialize subcircuit netlist using PySpice SubCircuit module
        SubCircuit.__init__(self, self.__name__, *self.__nodes__)
        # build netlist
        for element in elements:
            if element == "R":
                for resistor in elements["R"]:
                    self.R(resistor["id"], resistor["node1"], resistor["node2"], resistor["value"] @u_Ohm)

            elif element == "L":
                for inductor in elements["L"]:
                    self.L(inductor["id"], inductor["node1"], inductor["node2"], inductor["value"] @u_H)

            elif element == "C":
                for capacitor in elements["C"]:
                    self.C(capacitor["id"], capacitor["node1"], capacitor["node2"], capacitor["value"] @u_F)
