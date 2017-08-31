class Robot(object):

    FACING_NORTH = 0 # Facing up on y-axis
    FACING_EAST  = 1 # Facing right on x-axis
    FACING_SOUTH = 2 # Facing down on y-axis
    FACING_WEST  = 3 # Facing left on x-axis

    position = None

    facingMap = {
            FACING_NORTH: "up",
            FACING_EAST:  "right",
            FACING_SOUTH: "down",
            FACING_WEST:  "left"
        }

    facing_string_map = {
            FACING_NORTH: "north",
            FACING_EAST:  "east",
            FACING_SOUTH: "south",
            FACING_WEST:  "west"
    }


    def __init__(self, name, identifier, position):
        self.name = name
        self.identifier = identifier
        self.currentFacing = self.FACING_SOUTH
        self.position = position

    def sayName(self):
        return self.name

    def get_facing_string(self):
        return self.facing_string_map[self.currentFacing].upper()

    def tellFacing(self):
        print "I am facing %s"%(self.get_facing_String())

    def turn(self, direction):
        if direction in ["left", "l"]:
            return self.turnLeft()
        elif direction in ["right", "r"]:
            return self.turnRight()
        print "%s: Could not turn!"%(self.name)
        return False

    def turnLeft(self):
        print "%s: Turning left!"%(self.name)
        if self.currentFacing == self.FACING_NORTH:
            self.currentFacing = self.FACING_WEST
        else:
            self.currentFacing = self.currentFacing - 1
        return True

    def turnRight(self):
        print "%s: Turning right!"%(self.name)
        if self.currentFacing == self.FACING_WEST:
            self.currentFacing = self.FACING_NORTH
        else:
            self.currentFacing = self.currentFacing + 1
        return True

