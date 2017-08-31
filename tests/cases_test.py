import unittest
from src.map import Map
from src.robot import Robot
from src.satellite import Satellite
from src.position import Position
from src.uplink import Uplink
from src.controller import Controller

"""
Simple way of just running tests to cover challenge objectives
"""
class CasesTest(unittest.TestCase):

    """
    100x100 grid
    Robot starts at 0,0 facing SOUTH
    Commands given are fflff
    Robot should end at 2,2
    """
    def test_scenario_one(self):
        map = Map(100,100)
        satellite = Satellite(map)
        uplink = Uplink(satellite)
        position = Position(0, 0, Position.FACING_SOUTH)
        robot = Robot('Botty', 'id', position, uplink)
        controller = Controller(robot)
        controller.input("fflff")
        self.assertEquals(2, position.positionX)
        self.assertEquals(2, position.positionY)

    """
    50x50 grid
    Robot starts at 1,1 facing NORTH
    Commands given are fflff
    Robot should end at 1,0
    """
    def test_scenario_two(self):
        map = Map(100,100)
        satellite = Satellite(map)
        uplink = Uplink(satellite)
        position = Position(1, 1, Position.FACING_NORTH)
        robot = Robot('Botty', 'id', position, uplink)
        controller = Controller(robot)
        controller.input("fflff")
        self.assertEquals(1, position.positionX)
        self.assertEquals(0, position.positionY)

    """
    100x100 grid
    Robot starts at 50,50 facing NORTH
    Commands given are fflffrbb
    Robot should end at 1,0
    """
    def test_scenario_three(self):
        map = Map(100,100)
        map.add_obstacle(48,50)
        satellite = Satellite(map)
        uplink = Uplink(satellite)
        position = Position(50, 50, Position.FACING_NORTH)
        robot = Robot('Botty', 'id', position, uplink)
        controller = Controller(robot)
        controller.input("fflffrbb")
        self.assertEquals(48, position.positionX)
        self.assertEquals(49, position.positionY)
