"""
The satellite have the ability to scan the map
for obstacles and robots occupying space.
"""
class Satellite(object):
    
    def __init__(self, map):
        self.map = map
    
    def is_coordinates_occupied(self, posX, posY):
        for obstacle_position in self.map.obstacle_positions:
            collideX = obstacle_position.positionX == posX
            collideY = obstacle_position.positionY == posY
            if collideX is True and collideY is True:
                return True
        for robot in self.map.robots:
            collideX = robot.position.positionX == posX
            collideY = robot.position.positionY == posY
            if collideX is True and collideY is True:
                return True
        return False

    """
    Checks if passed position coordinates are outside of current
    board grid
    """
    def is_coordinates_out_of_bounds(self, posX, posY):
        oob_posX = posX < 0 or posX > (self.map.sizeX-1)
        oob_posY = posY < 0 or posY > (self.map.sizeY-1)
        if oob_posX is True or oob_posY is True:
            return True
        return False