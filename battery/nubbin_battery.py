from battery import Battery
from estimated_service_date import estimated_service_date

class Nubbin_battery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date;
        self.last_service_date = last_service_date;

    def needs_service(self):
        service_due_date = estimated_service_date(self.last_service_date, 4)
        if service_due_date < self.current_date:
            return True
        else:
            return False
       