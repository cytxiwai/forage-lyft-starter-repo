from battery.battery import Battery
from estimated_service_date import estimated_service_date

class SpindlerBattery(Battery):
    def _init_(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def need_service(self):
        service_due_date = estimated_service_date(self.last_service_date, 2)
        if service_due_date < self.current_date:
            return True
        else:
            return False
    