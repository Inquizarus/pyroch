import unittest
from src.map import Map
from src.robot import Robot
from src.position import Position
from src.uplink import Uplink

class MapTest(unittest.TestCase):

    def test_robots_can_be_added(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier', Position(), Uplink())
        board.add_robot(robot)
        self.assertEquals(1, board.count_robots())

    def test_board_can_tell_specific_robot_is_playing(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier', Position(), Uplink())
        board.add_robot(robot)
        self.assertTrue(board.is_robot_playing(robot))