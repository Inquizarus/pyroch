import unittest
from src.map import Map
from src.robot import Robot

class MapTest(unittest.TestCase):

    def test_robots_can_be_added(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        self.assertEquals(1, board.count_robots())

    def test_board_can_tell_specific_robot_is_playing(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        self.assertTrue(board.is_robot_playing(robot))

    def test_board_can_tell_specific_robot_position(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        self.assertEquals('0,0', board.get_robot_position(robot))

    def test_robot_can_be_placed_on_board(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        board.place_robot(robot, 0, 7)
        self.assertEquals('0,7', board.get_robot_position(robot))

    def test_robot_cant_be_placed_out_of_bounds(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        board.place_robot(robot, 0, 10)
        self.assertEquals('0,0', board.get_robot_position(robot))
    
    def test_robot_can_be_moved_forward(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        board.move_robot_forward(robot)
        self.assertEquals('0,1', board.get_robot_position(robot))

    def test_robot_can_be_moved_backwards(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        board.place_robot(robot, 0, 2)
        board.move_robot_backwards(robot)
        self.assertEquals('0,1', board.get_robot_position(robot))

    def test_robot_can_be_moved_with_expanded_commands(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        commands = ["forward", "left", "forward", "right", "backwards"]
        board.move_robot(robot, commands)
        self.assertEquals('1,0', board.get_robot_position(robot))

    def test_robot_can_be_moved_with_compact_commands(self):
        board = Map(10, 10)
        robot = Robot('Robo', 'identifier')
        board.add_robot(robot)
        commands = "flfrb"
        board.move_robot(robot, commands)
        self.assertEquals('1,0', board.get_robot_position(robot))