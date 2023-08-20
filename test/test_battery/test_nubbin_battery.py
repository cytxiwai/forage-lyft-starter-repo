import unittest
from datetime import date
from battery.nubbin_battery import Nubbin_battery

class TestNubbin_battery(unittest.TestCase):
    def test_needs_service_due(self):
        current_date = date.fromisoformat("2023-08-19")
        last_service_date = date.fromisoformat("2019-08-18")
        battery = Nubbin_battery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    
    def test_needs_service_not_due(self):
        current_date = date.fromisoformat("2023-08-19")
        last_service_date = date.fromisoformat("2020-08-19")
        battery = Nubbin_battery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


