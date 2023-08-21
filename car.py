from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tries = tires

    def needs_service(self):
        return self.engine.need_service() or self.battery.needs_service() or self.tires.needs_service()


