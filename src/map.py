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
        self.robot_positions = {}
        self.obstacle_positions = []

    """
    Adds robot to the pool of currently playing robots.
    Each robot is registered under its unique identifier already
    set on the robot.
    """
    def add_robot(self, robot, posX=0, posY=0):
        self.robots.append(robot)
        # If adding multiple robots. Make sure to calculate
        # wether or not starting space is already occupied and adjust
        self.robot_positions[robot.identifier] = Position(posX, posY)

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
    
    """
    Get a string representation of passed robots current
    position on the board
    """
    def get_robot_position(self, robot):
        if self.is_robot_playing(robot):
            posX = self.robot_positions[robot.identifier].positionX
            posY = self.robot_positions[robot.identifier].positionY
            return "%s,%s"%(posX,posY)
    
    """
    Runs the passed commands by doing board or robot
    actions correlated to each command
    """
    def move_robot(self, robot, commands):
        for command in commands:
            if command in ["left", "right", "l", "r"]:
                result = robot.turn(command)
            elif command in ["forward", "f"]:
                result = self.move_robot_forward(robot)
            elif command in ["backwards", "b"]:
                result = self.move_robot_backwards(robot)
            else:
                print "Command %s is not valid"%(command)
                continue
            if 'result' in locals() and result is not True:
                print "Robot could not be moved"
                print "Stopped as position %s"%(self.get_robot_position(robot))
                return result
        robotFacing = robot.get_facing_string()
        robotPosition = self.get_robot_position(robot)
        print "Sequence completed successfully. %s idle at %s facing %s"%(robot.name, robotPosition, robotFacing)

    """
    Moves passed robot forward, also validates if move is possible
    """
    def move_robot_forward(self, robot):
        posX = self.robot_positions[robot.identifier].positionX
        posY = self.robot_positions[robot.identifier].positionY
        if robot.currentFacing == Robot.FACING_EAST:
            posX = posX + 1
        elif robot.currentFacing == Robot.FACING_WEST:
            posX = posX - 1
        elif robot.currentFacing == Robot.FACING_NORTH:
            posY = posY - 1
        elif robot.currentFacing == Robot.FACING_SOUTH:
            posY = posY + 1
        return self.place_robot(robot, posX, posY)

    """
    Moves passed robot backwards, also validates if move is possible
    """
    def move_robot_backwards(self, robot):
        posX = self.robot_positions[robot.identifier].positionX
        posY = self.robot_positions[robot.identifier].positionY
        if robot.currentFacing == Robot.FACING_EAST:
            posX = posX - 1
        elif robot.currentFacing == Robot.FACING_WEST:
            posX = posX + 1
        elif robot.currentFacing == Robot.FACING_NORTH:
            posY = posY + 1
        elif robot.currentFacing == Robot.FACING_SOUTH:
            posY = posY - 1
        return self.place_robot(robot, posX, posY)

    """
    Picks up and places passed robot in passed position,
    also validates if the placement is possible.
    If placement is not valid the robot remain on original
    position
    """
    def place_robot(self, robot, posX, posY):
        if self.is_placement_possible(posX, posY) is True:
            self.robot_positions[robot.identifier].positionX = posX
            self.robot_positions[robot.identifier].positionY = posY
            print "Board: %s moved to %s!"%(robot.name, self.get_robot_position(robot))
            return True
        return False

    """
    Validates if passed coordinates is a valid position, takes
    other robots, obstacles and grid borders into consideration
    """
    def is_placement_possible(self, posX, posY):
        occupied = self.is_position_occupied(posX, posY)
        out_of_bounds = self.is_position_out_of_bounds(posX, posY)
        if occupied is True or out_of_bounds is True:
            return False
        return True
    
    """
    Checks wether or not an obstacle or robot is in the target location
    """
    def is_position_occupied(self, posX, posY):
        for obstacle_position in self.obstacle_positions:
            collideX = obstacle_position.positionX == posX
            collideY = obstacle_position.positionY == posY
            if collideX is True and collideY is True:
                return True
        for key in self.robot_positions:
            collideX = self.robot_positions[key].positionX == posX
            collideY = self.robot_positions[key] == posY
            if collideX is True and collideY is True:
                return True
        return False
    
    """
    Checks if passed position coordinates are outside of current
    board grid
    """
    def is_position_out_of_bounds(self, posX, posY):
        oob_posX = posX < 0 or posX > (self.sizeX-1)
        oob_posY = posY < 0 or posY > (self.sizeY-1)
        if oob_posX is True or oob_posY is True:
            return True
        return False