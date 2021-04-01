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
                for capacitor in circuit_lab["C"]:
                    self.C(capacitor["id"], capacitor["node1"], capacitor["node2"], capacitor["value"] @u_F)


circuit = Circuit("PSpice experiment in PySpice - General Subcircuit Class")
circuit.V("source", "in_1", circuit.gnd, 10@u_V)
circuit.subcircuit(SubCkt(subcircuit_input))
circuit.X(1, "3_parallel_resistors", "in_1", "a")
circuit.X(2, "3_parallel_resistors", "a", "out")
circuit.subcircuit(SubCkt(subcircuit_input_2))
circuit.X(3, "resistor", "out", circuit.gnd)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()
print(simulator)
print("\nV_out at resistor R1 is {:.2f}V".format(float(analysis.nodes["out"])))

# circuit = Circuit("PSpice experiment in PySpice - General Subcircuit Class")
# circuit.V("source", "in_1", circuit.gnd, 10@u_V)
# circuit.subcircuit(SubCkt(subcircuit_input_3))
# circuit.X(1, "series_resistor", "in_1", "out")
# circuit.subcircuit(SubCkt(subcircuit_input_2))
# circuit.X(2, "resistor", "out", circuit.gnd)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25)
# analysis = simulator.operating_point()
# print(simulator)
# print("\nV_out at resistor R1 is {:.2f}V".format(float(analysis.nodes["out"])))
