import unittest
from src.map import Map
from src.satellite import Satellite

class SatelliteTest(unittest.TestCase):

    def test_is_coordinates_occupied_return_false_if_not_occupied(self):
        map = Map(10, 10)
        satellite = Satellite(map)
        self.assertFalse(satellite.is_coordinates_occupied(5, 5))

    def test_is_coordinates_occupied_return_true_if_occupied(self):
        map = Map(10, 10)
        map.add_obstacle(5, 5)
        satellite = Satellite(map)
        self.assertTrue(satellite.is_coordinates_occupied(5, 5))