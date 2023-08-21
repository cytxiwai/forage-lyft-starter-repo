import unittest
import random
from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_due(self):
        tire_wear = [0] * 4
        count = 0
        while count < 3000:
            for i in range(4):
                tire_wear[i]= random.uniform(0, 1)
            tires = CarriganTires(tire_wear)
            for item in tire_wear:
                if item >= 0.9:
                    self.assertTrue(tires.needs_service())
            count += 1

