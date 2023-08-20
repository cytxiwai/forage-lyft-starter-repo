import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_due(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_needs_service_not_due(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

