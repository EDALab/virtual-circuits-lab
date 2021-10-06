import PySpice.Logging.Logging as Logging
logger =  Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit, SubCircuit, SubCircuitFactory
from PySpice.Unit import *

class ParallelResistor(SubCircuitFactory):
    # __name__ = 'parallel_resistor'
    # __nodes__ = ('n1', 'n2')
    def __init__(self, name, nodes):
        self.__name__ = name
        self.__nodes__ = nodes
        # __nodes__ = nodes
        super().__init__()
        self.R(1, 'n1', 'n2', R1)
        self.R(2, 'n1', 'n2', R2)

class ParallelResistor2(SubCircuit):
    __nodes__ = ['n1', 'n2']
    def __init__(self, name):
        # self.__nodes__ = nodes
        SubCircuit.__init__(self, name, *self.__nodes__)
        self.R(1, 'n1', 'n2', 1@u_kOhm)
        self.R(2, 'n1', 'n2', 1@u_kOhm)
        self.R(3, 'n1', 'n2', 1@u_kOhm)

# circuit = Circuit("Test")

# circuit.subcircuit(ParallelResistor("parallel_resistor", ["n1", "n2"]))
# circuit.X('1', 'parallel_resistor', 1, circuit.gnd)

# print(circuit)

# circuit = Circuit('Test2')
# circuit.subcircuit(ParallelResistor2('pr1', ["n1", "n2"]))
# circuit.X('1', 'pr1', 1, circuit.gnd)
# circuit.subcircuit(ParallelResistor2('pr2', ("n1", "n2")))
# circuit.X('2', 'pr2', 1, circuit.gnd)

# print(circuit)
# exit()
# # Create circuit
# circuit = Circuit("PSpice experiment in PySpice - NO SUBCIRCUIT")
# # Build the circuit
# circuit.V("source", "in_1", circuit.gnd, 10@u_V)
# circuit.R(1, "in_1", "a", 1@u_kOhm)
# circuit.R(2, "in_1", "a", 1@u_kOhm)
# circuit.R(3, "in_1", "a", 1@u_kOhm)
# circuit.R(4, "a", "out", 1@u_kOhm)
# circuit.R(5, "a", "out", 1@u_kOhm)
# circuit.R(6, "a", "out", 1@u_kOhm)
# circuit.R(7, "out", circuit.gnd, 1@u_kOhm)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# print(simulator)
# analysis = simulator.operating_point()
# print("\nV_out at resistor R7 is {:.2f}V".format(float(analysis.nodes["out"])))

# Same test using PySpice Subcircuit module
# circuit = Circuit("PSpice experient in PySpice - PySpice Subcircuit module")
# circuit.V("source", "in_1", circuit.gnd, 10@u_V)
# circuit.subcircuit(ParallelResistor2("3_parallel_resistors"))
# circuit.X("1", "3_parallel_resistors", "in_1", "a")
# circuit.X("2", "3_parallel_resistors", "a", "out")
# circuit.R(1, "out", circuit.gnd, 1@u_kOhm)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# analysis = simulator.operating_point()
# print(simulator)
# print("\nV_out at resistor R1 is {:.2f}V".format(float(analysis.nodes["out"])))


subcircuit_input = {
    "name": "3_parallel_resistors",
    "nodes": ["n1", "n2"],
    "subcircuit": {
        "R" : [
            {"id": "1", "name": "R1", "value": 1, "node1": "n1", "node2": "n2"},
            {"id": "2", "name": "R2", "value": 1, "node1": "n1", "node2": "n2"},
            {"id": "3", "name": "R3", "value": 1, "node1": "n1", "node2": "n2"}
        ]
    }
}

subcircuit_input_2 = {
    "name": "resistor",
    "nodes": ["n1", "n2"],
    "subcircuit": {
        "R" : [
            {"id": "1", "name": "R1", "value": 1, "node1": "n1", "node2": "n2"}
        ]
    }
}

subcircuit_input_3 = {
    "name": "series_resistor",
    "nodes": ["n1", "n3"],
    "subcircuit": {
        "R" : [
            {"id": "1", "name": "R1", "value": 1, "node1": "n1", "node2": "n2"},
            {"id": "2", "name": "R2", "value": 1, "node1": "n2", "node2": "n3"}
        ]
    }
}

subcircuit_input_4 = {
    "name": "4-port-resistor-network",
    "nodes": ["n1", "n2", "n3", "n4"],
    "subcircuit": {
        "R": [
            {"id": "1", "name": "R1", "value": 100, "node1": "n1", "node2": "n5"},
            {"id": "2", "name": "R2", "value": 100, "node1": "n5", "node2": "n2"},
            {"id": "3", "name": "R3", "value": 100, "node1": "n6", "node2": "n3"},
            {"id": "4", "name": "R4", "value": 100, "node1": "n5", "node2": "n4"},
            
        ],
        "C": [
            {"id": "1", "name": "C1", "value": 100, "node1": "n5", "node2": "n6"}
        ]
    }
}

subcircuit_input_5 = {
    "name": "18-port-network",
    "nodes": ["n1", "n2", "n5", "n6", "n7", "n8", "n9", "n10", "n11", "n12", "n13", "n14", "n15", "n16", "n17", "n18", "n19", "n20"],
    "subcircuit": {
        "R": [
            {"id": "1", "name": "R1", "value": 100, "node1": "n1", "node2": "n3"},
            {"id": "2", "name": "R2", "value": 100, "node1": "n2", "node2": "n3"},
            {"id": "3", "name": "R3", "value": 100, "node1": "n3", "node2": "n4"},
            {"id": "4", "name": "R4", "value": 100, "node1": "n4", "node2": "n5"},
            {"id": "5", "name": "R5", "value": 100, "node1": "n4", "node2": "n6"},
            {"id": "6", "name": "R6", "value": 100, "node1": "n4", "node2": "n7"},
            {"id": "7", "name": "R7", "value": 100, "node1": "n4", "node2": "n8"},
            {"id": "8", "name": "R8", "value": 100, "node1": "n4", "node2": "n9"},
            {"id": "9", "name": "R9", "value": 100, "node1": "n4", "node2": "n10"},
            {"id": "10", "name": "R10", "value": 100, "node1": "n4", "node2": "n11"},
            {"id": "11", "name": "R11", "value": 100, "node1": "n4", "node2": "n12"},
            {"id": "12", "name": "R12", "value": 100, "node1": "n4", "node2": "n13"},
            {"id": "13", "name": "R13", "value": 100, "node1": "n4", "node2": "n14"},
            {"id": "15", "name": "R14", "value": 100, "node1": "n4", "node2": "n15"},
            {"id": "16", "name": "R15", "value": 100, "node1": "n4", "node2": "n16"},
            {"id": "17", "name": "R16", "value": 100, "node1": "n4", "node2": "n17"},
            {"id": "18", "name": "R17", "value": 100, "node1": "n4", "node2": "n18"},
            {"id": "19", "name": "R18", "value": 100, "node1": "n4", "node2": "n19"},
            {"id": "20", "name": "R19", "value": 100, "node1": "n4", "node2": "n20"}    
        ]
    }
}


class SubCkt(SubCircuit):

    def __init__(self, subcircuit_input):
        self.__name__ = subcircuit_input["name"]
        self.__nodes__ = subcircuit_input["nodes"]
        SubCircuit.__init__(self, self.__name__, *self.__nodes__)
        subcircuit = subcircuit_input["subcircuit"]
        for element in subcircuit:
            if element == "R":
                for resistor in subcircuit["R"]:
                    self.R(resistor["id"], resistor["node1"], resistor["node2"], resistor["value"] @u_Ohm)

            elif element == "L":
                for inductor in subcircuit["L"]:
                    self.L(inductor["id"], inductor["node1"], inductor["node2"], inductor["value"] @u_H)

            elif element == "C":
                for capacitor in subcircuit["C"]:
                    self.C(capacitor["id"], capacitor["node1"], capacitor["node2"], capacitor["value"] @u_F)


# circuit = Circuit("PSpice experiment in PySpice - General Subcircuit Class")
# circuit.V("source", "in_1", circuit.gnd, 10@u_V)
# circuit.subcircuit(SubCkt(subcircuit_input))
# circuit.X(1, "3_parallel_resistors", "in_1", "a")
# circuit.X(2, "3_parallel_resistors", "a", "out")
# circuit.subcircuit(SubCkt(subcircuit_input_2))
# circuit.X(3, "resistor", "out", circuit.gnd)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# analysis = simulator.operating_point()
# print(simulator)
# print("\nV_out at resistor R1 is {:.2f}V".format(float(analysis.nodes["out"])))
# print("")

# 4-port subcircuit experiment
# circuit = Circuit("Testing subcircuit with more than two ports")

# circuit.V("source", "a", circuit.gnd, 10@u_V)

# circuit.subcircuit(SubCkt(subcircuit_input_4))
# circuit.X(1, "4-port-resistor-network", "a", "b", "c", "d")
# circuit.R(1, "b", "c", 100@u_Ohm)
# circuit.R(2, "c", "d", 100@u_Ohm)
# circuit.R(3, "d", circuit.gnd, 100@u_Ohm)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# print(simulator)
# analysis = simulator.operating_point()
# print("\nV_out at resistor is {:.5f}V".format(float(analysis.nodes["c"])))
# print("")

# 18 - port subcircuit experiment
circuit = Circuit("Testing subcircuit with more than two ports")

circuit.V("source1", "a", circuit.gnd, 10@u_V)
circuit.V("source2", "b", circuit.gnd, 20@u_V)

circuit.subcircuit(SubCkt(subcircuit_input_5))
circuit.X(1, "18-port-network", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r")

circuit.R(1, "c", "join", 100@u_Ohm)
circuit.R(2, "d", "join", 100@u_Ohm)
circuit.R(3, "e", "join", 100@u_Ohm)
circuit.R(4, "f", "join", 100@u_Ohm)
circuit.R(5, "g", "join", 100@u_Ohm)
circuit.R(6, "h", "join", 100@u_Ohm)
circuit.R(7, "i", "join", 100@u_Ohm)
circuit.R(8, "j", "join", 100@u_Ohm)
circuit.R(9, "k", "join", 100@u_Ohm)
circuit.R(10, "l", "join", 100@u_Ohm)
circuit.R(11, "m", "join", 100@u_Ohm)
circuit.R(12, "n", "join", 100@u_Ohm)
circuit.R(13, "o", "join", 100@u_Ohm)
circuit.R(14, "p", "join", 100@u_Ohm)
circuit.R(15, "q", "join", 100@u_Ohm)
circuit.R(16, "r", "join", 100@u_Ohm)
circuit.R(17, "join", circuit.gnd, 100@u_Ohm)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
print(simulator)
analysis = simulator.operating_point()
print("\nV_out at resistor is {:.5f}V".format(float(analysis.nodes["m"])))
print("")