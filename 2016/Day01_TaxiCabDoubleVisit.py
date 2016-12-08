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

pointsVisited = {(0,0):1}
currentNS = 0
currentEW = 0
foundIt = False

for turn in args.turns:
	turn = turn.replace(',','')
	# print(turn)
	turnDirection = turn[0]
	distance = int(turn[1:])
	if turnDirection == 'L':
		currentDirection = (currentDirection - 1) % Direction.MaxDirections
	else:
		currentDirection = (currentDirection + 1) % Direction.MaxDirections
	for x in range(0,distance):
		# Add/Subtract 1 in direction of travel
		if currentDirection == Direction.North:
			currentNS += 1
			# print('Going North')
		elif currentDirection == Direction.South:
			currentNS -= 1
			# print('Going South')
		elif currentDirection == Direction.East:
			currentEW += 1
			# print('Going East')
		elif currentDirection == Direction.West:
			currentEW -= 1
			# print('Going West')
		# check if tuple in pointsVisited
		if (currentEW,currentNS) in pointsVisited:
			print("Found it at E/W:" + str(currentEW) + " N/S:" + str(currentNS))
			# if yes break out and calculate distance from tuple
			foundIt = True
			break
		# if no add tuple to pointsVisited
		else:
			pointsVisited[currentEW,currentNS] = 1
	if foundIt:
		break

print('Total Distance to HQ: ' + str(abs(currentNS) + abs(currentEW)))
# print(pointsVisited)