from robot import Robot
from position import Position

"""
The board have the responsibility for the following:
    1. Current playing robots
    2. Current playing robots coordinates
    3. Size of board
    4. Any obstacles coordinates
    5. Move robots backwards/forward
    6. Relay any non-board commands to robots
"""
class Map(object):

    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.robots = []
        self.obstacle_positions = []

    """
    Adds robot to the pool of currently playing robots.
    Each robot is registered under its unique identifier already
    set on the robot.
    """
    def add_robot(self, robot):
        self.robots.append(robot)

    """
    Adds an obstacle at passed coordinates to the map
    """
    def add_obstacle(self, posX, posY):
        self.obstacle_positions.append(Position(posX, posY))

    """
    Counts the currently playing robots
    """
    def count_robots(self):
        return len(self.robots)

    """
    Checks wether or not the passed robot is currently playing or not
    """
    def is_robot_playing(self, robot):
        for playingBot in self.robots:
            if playingBot.identifier == robot.identifier:
                return True
        return False
