import unittest
from src.controller import Controller
from src.robot import Robot
from src.position import Position
from src.uplink import Uplink

class ControllerTest(unittest.TestCase):

    def test_it_interprets_input(self):
        position = Position()
        uplink = Uplink()
        uplink.override_missing_satellite = True
        robot = Robot('Botty', 'id', position, uplink)
        controller = Controller(robot)
        controller.input("lffrffb")
        self.assertTrue(Position.FACING_WEST, position.facing)
        self.assertEquals(2,position.positionX)
        self.assertEquals(1,position.positionY)