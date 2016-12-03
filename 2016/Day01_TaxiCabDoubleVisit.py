from enum import IntEnum
import argparse

class Direction(IntEnum):
	North = 0
	East = 1
	South = 2
	West = 3
	MaxDirections = 4

print('Get Directions!')

currentDirection = Direction.North

parser = argparse.ArgumentParser()
parser.add_argument('--turns', type=str, nargs='+')
args = parser.parse_args()

pointsVisited = {}
currentNS = 0
currentEW = 0

for turn in args.turns:
	turn = turn.replace(',','')
	# print(turn)
	turnDirection = turn[0]
	distance = int(turn[1:])
	if turnDirection == 'L':
		currentDirection = (currentDirection - 1) % Direction.MaxDirections
	else:
		currentDirection = (currentDirection + 1) % Direction.MaxDirections
	for x in range(1,distance):
		# check if tuple in pointsVisited
		# if yes break out and calculate distance from tuple
		# if no add tuple to pointsVisited