import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_due(self):
      current_date = date.fromisoformat("2023-08-19")
      last_service_date = date.fromisoformat("2020-08-18")
      battery = SpindlerBattery(current_date, last_service_date)
      self.assertTrue(battery.needs_service())


    def test_needs_service_not_due(self):
       current_date = date.fromisoformat("2023-08-19")
       last_service_date = date.fromisoformat("2020-08-20")
       battery = SpindlerBattery(current_date, last_service_date)
       self.assertFalse(battery.needs_service()) 
