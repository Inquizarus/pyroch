class Satellite(object):
    
    def __init__(self, map):
        self.map = map
    
    def is_coordinates_occupied(self, posX, posY):
        for obstacle_position in self.map.obstacle_positions:
            collideX = obstacle_position.positionX == posX
            collideY = obstacle_position.positionY == posY
            if collideX is True and collideY is True:
                return True
        for key in self.map.robot_positions:
            collideX = self.map.robot_positions[key].positionX == posX
            collideY = self.map.robot_positions[key] == posY
            if collideX is True and collideY is True:
                return True
        return False