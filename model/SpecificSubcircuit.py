class SpecificSubcircuit():

    def __init__(self, subcircuit_template_id, is_black_box, circuit_id, connect, rotate, position, current, circle, elementDOM, port_identifiers):
        self.subcircuit_template_id = subcircuit_template_id
        self.is_black_box = is_black_box
        self.circuit_id = circuit_id
        self.connect = connect
        self.rotate = rotate
        self.position = position
        self.current = current
        self.circle = circle
        self.elementDOM = elementDOM
        self.port_identifiers = port_identifiers

    def to_dict(self):
        specific_subcircuit_dict = {
            "subcircuit_template_id": self.subcircuit_template_id,
            "is_black_box": self.is_black_box,
            "circuit_id": self.circuit_id,
            "connect": self.connect,
            "rotate": self.rotate,
            "position": self.position,
            "current": self.current,
            "circle": self.circle,
            "elementDOM": self.elementDOM,
            "port_identifiers": self.port_identifiers
        }
        return specific_subcircuit_dict

    @staticmethod
    def from_dict(source):
        specific_subcircuit = SpecificSubcircuit(
            source["subcircuit_template_id"],
            source["is_black_box"],
            source["circuit_id"],
            source["connect"],
            source["rotate"],
            source["position"],
            source["current"],
            source["circle"],
            source["elementDOM"],
            source["port_identifiers"]
            )
        return specific_subcircuit

    def __repr__(self) -> str:
        return f"SpecificSubcircuit(subcircuit_template_id={self.subcircuit_template_id}, is_black_box={self.is_black_box}, circuit_id={self.circuit_id}, \
        connect={self.connect}, rotate={self.rotate}, position={self.position}, current={self.current}, circle={self.circle}, elementDOM={self.elementDOM}, port_identifiers={self.port_identifiers})"