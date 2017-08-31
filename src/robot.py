class Robot(object):

    FACING_NORTH = 0 # Facing up on y-axis
    FACING_EAST  = 1 # Facing right on x-axis
    FACING_SOUTH = 2 # Facing down on y-axis
    FACING_WEST  = 3 # Facing left on x-axis

    position = None
    uplink = None

    def __init__(self, name, identifier, position, uplink):
        self.name = name
        self.identifier = identifier
        self.position = position
        self.uplink = uplink

    def sayName(self):
        return self.name

    def get_facing_string(self):
        return self.position.get_facing_string()

    def tellFacing(self):
        print "I am facing %s"%(self.get_facing_String())

    def turn(self, direction):
        return self.position.turn(direction)

    def move_forward(self):
        posX, posY = self.position.calculate_move_forward()
        positionClear = self.uplink.is_position_clear(posX, posY)
        positionOob = self.uplink.is_position_out_of_bounds(posX, posY)
        if  positionClear is not True:
            print "Robot: Could not move forward because of obstacle in %s,%s"%(posX, posY)
            return False
        elif positionOob is True:
            print "Robot: Could not move forward because of %s,%s being out of bounds"%(posX, posY)
            return False
        print "Robot: Moving forward to %s,%s"%(posX, posY)
        return self.position.move(posX, posY)

    def move_backwards(self):
        posX, posY = self.position.calculate_move_backwards()
        positionClear = self.uplink.is_position_clear(posX, posY)
        positionOob = self.uplink.is_position_out_of_bounds(posX, posY)
        if  positionClear is not True or positionOob is True:
            return False
        print "Robot: Moving backwards to %s,%s"%(posX, posY)
        return self.position.move(posX, posY)
