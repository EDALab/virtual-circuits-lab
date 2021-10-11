class SubcircuitTemplate():
    
    def __init__(self, subcircuit_name, part_type, is_black_box, components, connect, student_id=None, lab_id=None):
        self.subcircuit_name = subcircuit_name
        self.part_type = part_type
        self.is_black_box = is_black_box
        self.components = components
        self.connect = connect
        self.student_id = student_id
        self.lab_id = lab_id

    def to_dict(self):
        subcircuit_dict = {
            "subcircuit_name": self.subcircuit_name,
            "part_type": self.part_type,
            "is_black_box": self.is_black_box,
            "components": self.components,
            "connect": self.connect,
            "student_id": self.student_id,
            "lab_id": self.lab_id
        }
        return subcircuit_dict

    @staticmethod
    def from_dict(source):
        subcircuit_template = SubcircuitTemplate(
            source["subcircuit_name"], 
            source["part_type"], 
            source["is_black_box"], 
            source["components"], 
            source["connect"],
            )
        return subcircuit_template
    
    def __repr__(self):
        return f"SubcircuitTemplate(subcircuit_name={self.subcircuit_name}, part_type={self.part_type}, is_black_box={self.is_black_box}, \
            components={self.components}, connect={self.connect}, student_id={self.student_id}, lab_id={self.lab_id})"