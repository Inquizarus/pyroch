import sys
import argparse
from src.map import Map
from src.robot import Robot
from src.satellite import Satellite
from src.position import Position
from src.uplink import Uplink
from src.controller import Controller

parser = argparse.ArgumentParser()
parser.add_argument("--size-x", "-zx", help="Sets the size for grid on x-axis")
parser.add_argument("--size-y", "-zy", help="Sets the size for grid on y-axis")
parser.add_argument("--start-x", "-sx", help="Sets the start position for robot on x-axis")
parser.add_argument("--start-y", "-sy", help="Sets the start position for robot on x-axis")
parser.add_argument("--sequence", "-s", help="Inputs a sequence to run through robot")
parser.add_argument("--start-facing", "-sf", help="Sets the initial facing of robot")
parser.add_argument("--obstacles", "-o", help="Adding one or more obstacles by providing x and y axis positions", nargs='+')

args = parser.parse_args()
commands = args.sequence if args.sequence else []
obstacles = args.obstacles if args.obstacles else []

sizeX = int(args.size_x) if args.size_x else 10
sizeY = int(args.size_y) if args.size_y else 10

startX = int(args.start_x) if args.start_x else 0
startY = int(args.start_y) if args.start_y else 0

startFacing = args.start_facing if args.start_facing else "SOUTH"

# The map is quite vital I would say. :)
map = Map(sizeX, sizeY)

# Add any obstacles to the map which have been passed as arguments
map.add_obstacles(obstacles)

# Big brother is needed to oversee things ofc.
satellite = Satellite(map)

# Super secret robots needs an uplink to speak with secret satellites.
uplink = Uplink(satellite)

# The robot really need a way to know where the heck it is.
position = Position(startX, startY, startFacing)

# Set up the robot
robot = Robot(
    'Botty', 
    'unique_identifier_string', 
    position,
    uplink
    )

# Add robot to the created map
map.add_robot(robot)

# Plug in the controller!
controller = Controller(robot)

# Run the passed sequence
controller.input(commands)



