class Robot(object):

    FACING_NORTH = 0 # Facing up on y-axis
    FACING_EAST  = 1 # Facing right on x-axis
    FACING_SOUTH = 2 # Facing down on y-axis
    FACING_WEST  = 3 # Facing left on x-axis

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.currentFacing = self.FACING_SOUTH
        self.facingMap = {
            self.FACING_NORTH: "up",
            self.FACING_EAST:  "right",
            self.FACING_SOUTH: "down",
            self.FACING_WEST:  "left"
        }
        self.facing_string_map = {
            self.FACING_NORTH: "north",
            self.FACING_EAST:  "east",
            self.FACING_SOUTH: "south",
            self.FACING_WEST:  "west"
        }

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

