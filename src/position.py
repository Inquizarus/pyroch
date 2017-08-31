class Position(object):
    
    FACING_NORTH = 0 # Facing up on y-axis
    FACING_EAST  = 1 # Facing right on x-axis
    FACING_SOUTH = 2 # Facing down on y-axis
    FACING_WEST  = 3 # Facing left on x-axis

    facing_to_string_map = {
            FACING_NORTH: "north",
            FACING_EAST:  "east",
            FACING_SOUTH: "south",
            FACING_WEST:  "west"
    }

    string_to_facing_map = {
        "n": FACING_NORTH,
        "north": FACING_NORTH,
        "e": FACING_EAST,
        "east": FACING_EAST,
        "s": FACING_SOUTH,
        "south": FACING_SOUTH,
        "w": FACING_WEST,
        "west": FACING_WEST
    }

    facing    = None
    positionX = None
    positionY = None

    def __init__(self, positionX = 0, positionY = 0, facing = FACING_SOUTH):
        self.positionX = positionX
        self.positionY = positionY
        self.set_facing(facing)

    def set_facing(self, facing):
        if facing in [self.FACING_EAST, self.FACING_SOUTH, self.FACING_WEST, self.FACING_NORTH]:
            self.facing = facing
            return True
        for key in self.string_to_facing_map:
            if facing.lower() == key:
                self.facing = self.string_to_facing_map[key]
                return True
        return False

    def turn(self, direction):
        if direction in ["left", "l"]:
            return self.turnLeft()
        elif direction in ["right", "r"]:
            return self.turnRight()
        return False

    def turnLeft(self):
        print "Robot: Turning left"
        if self.facing == self.FACING_NORTH:
            self.facing = self.FACING_WEST
        else:
            self.facing = self.facing - 1
        return True

    def turnRight(self):
        print "Robot: Turning right"
        if self.facing == self.FACING_WEST:
            self.facing = self.FACING_NORTH
        else:
            self.facing = self.facing + 1
        return True

    def get_facing_string(self):
        return self.facing_to_string_map[self.facing].upper()

    """
    Calculates move forward and returns new coordinates
    """
    def calculate_move_forward(self):
        posX = self.positionX
        posY = self.positionY
        if self.facing == self.FACING_EAST:
            posX = posX + 1
        elif self.facing == self.FACING_WEST:
            posX = posX - 1
        elif self.facing == self.FACING_NORTH:
            posY = posY - 1
        elif self.facing == self.FACING_SOUTH:
            posY = posY + 1
        return [posX, posY]

    """
    Calculates move backwards and returns new coordinates
    """
    def calculate_move_backwards(self):
        posX = self.positionX
        posY = self.positionY
        if self.facing == self.FACING_EAST:
            posX = posX - 1
        elif self.facing == self.FACING_WEST:
            posX = posX + 1
        elif self.facing == self.FACING_NORTH:
            posY = posY + 1
        elif self.facing == self.FACING_SOUTH:
            posY = posY - 1
        return [posX, posY]

    def move(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        return True
