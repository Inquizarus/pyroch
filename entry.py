import sys
import argparse
from src.map import Map
from src.robot import Robot
from src.satellite import Satellite

parser = argparse.ArgumentParser()
parser.add_argument("--size-x", help="Sets the size for grid on x-axis")
parser.add_argument("--size-y", help="Sets the size for grid on y-axis")
parser.add_argument("--start-x", help="Sets the start position for robot on x-axis")
parser.add_argument("--start-y", help="Sets the start position for robot on x-axis")
parser.add_argument("--sequence", help="Inputs a sequence to run through robot")
parser.add_argument("--start-facing", help="Sets the initial facing of robot")

args = parser.parse_args()

commands = args.sequence if args.sequence else []

sizeX = int(args.size_x) if args.size_x else 10
sizeY = int(args.size_y) if args.size_y else 10

startX = int(args.start_x) if args.start_x else 0
startY = int(args.start_y) if args.start_y else 0

startFacing = args.start_facing if args.start_facing else "SOUTH"

map = Map(sizeX, sizeY)
satellite = Satellite(map)

robot = Robot('Botty', 'unique_identifier_string')

map.add_robot(robot, startX, startY)
map.move_robot(robot, commands)

