import PySpice.Logging.Logging as Logging
from PySpice.Spice.Library import SpiceLibrary 
from PySpice.Spice.Netlist import Circuit, SubCircuit
from PySpice.Unit import *
from PySpice.Tools.Path import parent_directory_of
import os
import sys

def get_node_label(node):
    return "n" + str(node)
    
# This is a class that breaks down a JSON and creates a Subcircuit netlist.
# This class uses PySpice to create the netlist. This class can be used to be used for simulations.
# There should be a database query in here.
class SubCkt(SubCircuit):

    # Change constructor to take in name as parameter
    # Remove line 15 that searches for components. Components will now be directly passed in as a value to the constructor
    def __init__(self, subcircuit_name, subcircuit_components, circuit):
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

        python_file = os.path.abspath(sys.argv[0])
        examples_root = parent_directory_of(python_file)
        libraries_path = os.path.join(examples_root, 'libraries')

        spice_library = SpiceLibrary(libraries_path)

        # build netlist
        for element in elements:
            if element == "R":
                for resistor in elements["R"]:
                    self.R(resistor["id"], 
                        self.gnd if resistor["node1"] == "gnd" else get_node_label(resistor["node1"]), 
                        self.gnd if resistor["node2"] == "gnd" else get_node_label(resistor["node2"]), 
                        resistor["value"]@u_Ohm)

            elif element == "L":
                for inductor in elements["L"]:
                    self.L(inductor["id"],
                        self.gnd if inductor["node1"] == "gnd" else get_node_label(inductor["node1"]),
                        self.gnd if inductor["node2"] == "gnd" else get_node_label(inductor["node2"]), 
                        inductor["value"]@u_H)

            elif element == "C":
                for capacitor in elements["C"]:
                    self.C(capacitor["id"], 
                        self.gnd if capacitor["node1"] == "gnd" else get_node_label(capacitor["node1"]), 
                        self.gnd if capacitor["node2"] == "gnd" else get_node_label(capacitor["node2"]), 
                        capacitor["value"]@u_F)

            elif element == "D":
                for diode in elements["D"]:
                    try:
                        model = str(diode["modelType"]).upper()
                        circuit.include(spice_library[model])
                        self.X(diode["id"], model,
                            self.gnd if diode["node1"] == "gnd" else get_node_label(diode["node1"]),
                            self.gnd if diode["node2"] == "gnd" else get_node_label(diode["node2"]))
                    except KeyError as e:
                        print(f"Error creating diode element in subcircuit generator: {str(e)}")

            elif element == "nBJT":
                for nBJT in elements["nBJT"]:
                    try:
                        model = str(nBJT["modelType"]).upper()
                        circuit.include(spice_library[nBJT["modelType"]])
                        self.BJT(nBJT["id"],
                            self.gnd if nBJT["node1"] == "gnd" else get_node_label(nBJT["node1"]), 
                            self.gnd if nBJT["node2"] == "gnd" else get_node_label(nBJT["node2"]), 
                            self.gnd if nBJT["node3"] == "gnd" else get_node_label(nBJT["node3"]), 
                            model=model)
                    except KeyError as e:
                        print(f"Error creating nBJT element in subcircuit generator: {str(e)}")
            
            elif element == "pBJT":
                for pBJT in elements["pBJT"]:
                    try:
                        model = str(pBJT["modelType"]).upper()
                        circuit.include(spice_library[pBJT["modelType"]])
                        self.BJT(pBJT["id"],
                            self.gnd if pBJT["node3"] == "gnd" else get_node_label(pBJT["node3"]),
                            self.gnd if pBJT["node2"] == "gnd" else get_node_label(pBJT["node2"]),
                            self.gnd if pBJT["node1"] == "gnd" else get_node_label(pBJT["node1"]),
                            model=model)
                    except KeyError as e:
                        print(f"Error creating pBJT element in subcircuit generator: {str(e)}")

            elif element == "NMOS":
                for nmos in elements["NMOS"]:
                    try:
                        model = str(nmos["modelType"]).upper()
                        circuit.include(spice_library[nmos["modelType"]])
                        self.MOSFET(nmos["id"],
                            self.gnd if nmos["node4"] == "gnd" else get_node_label(nmos["node4"]),
                            self.gnd if nmos["node2"] == "gnd" else get_node_label(nmos["node2"]),
                            self.gnd if nmos["node3"] == "gnd" else get_node_label(nmos["node3"]),
                            self.gnd if nmos["node1"] == "gnd" else get_node_label(nmos["node1"]),
                            model=model)
                    except KeyError as e:
                        print(f"Error creating nmos element in subcircuit generator: {str(e)}")

            elif element == "PMOS":
                for pmos in elements["PMOS"]:
                    try:
                        model = str(pmos["modelType"]).upper()
                        circuit.include(spice_library[pmos["modelType"]])
                        self.MOSFET(pmos["id"],
                            self.gnd if pmos["node1"] == "gnd" else get_node_label(pmos["node1"]),
                            self.gnd if pmos["node2"] == "gnd" else get_node_label(pmos["node2"]),
                            self.gnd if pmos["node3"] == "gnd" else get_node_label(pmos["node3"]),
                            self.gnd if pmos["node4"] == "gnd" else get_node_label(pmos["node4"]), 
                            model=model)
                    except KeyError as e:
                        print(f"Error creating pmos element in subcircuit generator: {str(e)}")