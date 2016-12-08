import argparse

print('Get to the Bathroom!')

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int)
parser.add_argument('--moves', type=str)
args = parser.parse_args()

keypadLocVal = {(0,0):1,(0,1):2,(0,2):3,(0,1):4,(1,1):5,(2,1):6,(0,2):7,(1,2):8,(2,2):9}
keypadValLoc = {1:(0,0),2:(0,1),3:(0,2),4:(0,1),5:(1,1),6:(2,1),7:(0,2),8:(1,2),9:(2,2)}
minVal = 0
maxVal = 2

xLoc = keypadValLoc[args.start][0]
yLoc = keypadValLoc[args.start][1]

for c in args.moves:
	# print(c)
	if c == 'U':
		if yLoc > minVal:
			yLoc -= 1
	if c == 'D':
		if yLoc < maxVal:
			yLoc += 1
	if c == 'L':
		if xLoc > minVal:
			xLoc -= 1
	if c == 'R':
		if xLoc < maxVal:
			xLoc += 1

print('Number = ' + str(keypadLocVal[(xLoc,yLoc)]))

#78985