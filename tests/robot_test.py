import unittest
from src.robot import Robot
from src.position import Position
from src.uplink import Uplink

class RobotTest(unittest.TestCase):

    def test_it_can_says_name(self):
        botName = 'Robo'
        position = Position()
        bot = Robot(botName, 'identifier', position, Uplink())
        self.assertEquals(botName, bot.sayName())

    def test_it_can_turn(self):
        position = Position()
        bot = Robot('Botty', 'id', position, Uplink())
        bot.position.facing =  Position.FACING_NORTH
        bot.turn("r")
        self.assertEquals( Position.FACING_EAST, bot.position.facing)
        bot.turn("l")
        self.assertEquals( Position.FACING_NORTH, bot.position.facing)

    def test_it_can_turn_by_command_string(self):
        commandString = "left"
        position = Position()
        bot = Robot('Botty', 'id', position, Uplink())
        bot.position.facing = Position.FACING_NORTH
        bot.turn(commandString)
        self.assertEquals( Position.FACING_WEST, bot.position.facing)
    