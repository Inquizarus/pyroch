import unittest
from src.robot import Robot

class RobotTest(unittest.TestCase):

    def test_it_can_says_name(self):
        botName = 'Robo'
        bot = Robot(botName, 'identifier')
        self.assertEquals(botName, bot.sayName())

    def test_it_can_turn(self):
        bot = Robot('Botty', 'id')
        bot.currentFacing = Robot.FACING_NORTH
        bot.turnRight()
        self.assertEquals(Robot.FACING_EAST, bot.currentFacing)
        bot.turnLeft()
        self.assertEquals(Robot.FACING_NORTH, bot.currentFacing)

    def test_it_can_turn_by_command_string(self):
        commandString = "left"
        bot = Robot('Botty', 'id')
        bot.currentFacing = Robot.FACING_NORTH
        bot.turn(commandString)
        self.assertEquals(Robot.FACING_WEST, bot.currentFacing)
    