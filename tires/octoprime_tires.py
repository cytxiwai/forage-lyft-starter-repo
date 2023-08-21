from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wire = tire_wear

    def needs_service(self):
        if sum(self.tire_wire) >= 3.0:
            return True
        else:
            return False
