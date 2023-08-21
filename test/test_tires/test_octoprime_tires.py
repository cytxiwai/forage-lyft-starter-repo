import unittest
import random
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_due(self):
        tire_wear = [0] * 4
        count = 0
        while count < 3000:
            for i in range(4):
                tire_wear[i] = random.uniform(0, 1)
            tires = OctoprimeTires(tire_wear)
            if sum(tire_wear) >= 3.0:
                self.assertTrue(tires.needs_service())
            count += 1
