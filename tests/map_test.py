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

    def test_obstacle_can_be_added(self):
        map = Map(10,10)
        map.add_obstacle(5,5)
        self.assertIsInstance(map.obstacle_positions[0], Position)
        self.assertEquals(5, map.obstacle_positions[0].positionX)
        self.assertEquals(5, map.obstacle_positions[0].positionY)

    def test_obstacles_can_be_added(self):
        map = Map(10,10)
        map.add_obstacles(["5,5", "6,6"])
        self.assertIsInstance(map.obstacle_positions[0], Position)
        self.assertEquals(5, map.obstacle_positions[0].positionX)
        self.assertEquals(5, map.obstacle_positions[0].positionY)
        self.assertIsInstance(map.obstacle_positions[1], Position)
        self.assertEquals(6, map.obstacle_positions[1].positionX)
        self.assertEquals(6, map.obstacle_positions[1].positionY)