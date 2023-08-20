import unittest
import random

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):


    def test_needs_service_not_due(self):
        current_mileage = random.randint(0,200000)
        last_service_mileage = random.randint(0,200000)
        count = 0
        while count < 3000:
            if current_mileage - last_service_mileage < 30000:
                engine = CapuletEngine(current_mileage, last_service_mileage)
                self.assertFalse(engine.needs_service())
            else:
                engine = CapuletEngine(current_mileage, last_service_mileage)
                self.assertTrue(engine.needs_service())
            count += 1



