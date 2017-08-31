import unittest
from src.uplink import Uplink
from src.satellite import Satellite
from src.map import Map

class UplinkTest(unittest.TestCase):

    def test_it_returns_correct_position_clear_response(self):
        map = Map(2,2)
        map.add_obstacle(1,1)
        satellite = Satellite(map)
        uplink = Uplink(satellite)
        self.assertTrue(uplink.is_position_clear(0,0))
        self.assertFalse(uplink.is_position_clear(1,1))

    def test_it_returns_correct_oob_response(self):
        map = Map(1,1)
        satellite = Satellite(map)
        uplink = Uplink(satellite)
        self.assertTrue(uplink.is_position_out_of_bounds(1,0))
        self.assertTrue(uplink.is_position_out_of_bounds(0,1))
        self.assertTrue(uplink.is_position_out_of_bounds(1,1))
        self.assertFalse(uplink.is_position_out_of_bounds(0,0))
