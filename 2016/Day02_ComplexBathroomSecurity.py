import argparse

print('Get to the Bathroom!')

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=str)
parser.add_argument('--moves', type=str)
args = parser.parse_args()

keypadLocVal = {(2,0):'1',(1,1):'2',(2,1):'3',(3,1):'4',(0,2):'5',(1,2):'6',(2,2):'7',(3,2):'8',(4,2):'9',(1,3):'A',(2,3):'B',(3,3):'C',(2,4):'D'}
keypadValLoc = {'1':(2,0),'2':(1,1),'3':(2,1),'4':(3,1),'5':(0,2),'6':(1,2),'7':(2,2),'8':(3,2),'9':(4,2),'A':(1,3),'B':(2,3),'C':(3,3),'D':(2,4)}
validUp = ['3','6','7','8','A','B','C','D']
validDown = ['1','2','3','4','6','7','8','B']
validLeft = ['3','4','6','7','8','9','B','C']
validRight = ['2','3','5','6','7','8','A','B']

xLoc = keypadValLoc[args.start][0]
yLoc = keypadValLoc[args.start][1]

for c in args.moves:
	# print(c)
	if c == 'U':
		if keypadLocVal[(xLoc,yLoc)] in validUp:
			yLoc -= 1
	if c == 'D':
		if keypadLocVal[(xLoc,yLoc)] in validDown:
			yLoc += 1
	if c == 'L':
		if keypadLocVal[(xLoc,yLoc)] in validLeft:
			xLoc -= 1
	if c == 'R':
		if keypadLocVal[(xLoc,yLoc)] in validRight:
			xLoc += 1

print('Key = ' + str(keypadLocVal[(xLoc,yLoc)]))

#57DD8