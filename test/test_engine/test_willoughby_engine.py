import unittest
import random
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service(self):
        current_mileage = random.randint(0,200000)
        last_service_mileage = random.randint(0,200000)
        count = 0
        while count < 3000:
            if current_mileage - last_service_mileage < 60000:
                engine = WilloughbyEngine(current_mileage, last_service_mileage)
                self.assertFalse(engine.needs_service())
            else:
                engine = WilloughbyEngine(current_mileage, last_service_mileage)
                self.assertTrue(engine.needs_service())
            count += 1