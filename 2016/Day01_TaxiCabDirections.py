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

distances = [0] * 4
# print(distances)

parser = argparse.ArgumentParser()
parser.add_argument('--turns', type=str, nargs='+')
args = parser.parse_args()

for turn in args.turns:
	turn = turn.replace(',','')
	# print(turn)
	turnDirection = turn[0]
	distance = int(turn[1:])
	if turnDirection == 'L':
		currentDirection = (currentDirection - 1) % Direction.MaxDirections
	else:
		currentDirection = (currentDirection + 1) % Direction.MaxDirections
	distances[currentDirection] += distance

print(distances)

totalDistance = abs(distances[Direction.North] - distances[Direction.South]) + abs(distances[Direction.East] - distances[Direction.West])

print(totalDistance)