import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('--roomFile', type=str)
args = parser.parse_args()

roomFile = open(args.roomFile, 'r')

testRooms = roomFile.readlines()
sectorSum = 0

def right_caeser(encodedLetter, rotate):
	startCode = string.ascii_lowercase.index(encodedLetter)
	endCode = (startCode + rotate) % 26
	return string.ascii_lowercase[endCode]

for room in testRooms:
	letterCount = {'a':0}
	validChecksum = True
	decodedName = ''

	nameChunks = room.split('-')
	sectorAndChecksum = nameChunks.pop().rstrip("\r\n")
	name = ''.join(nameChunks)
	# print(name)

	sector, checksum = sectorAndChecksum.split('[')
	checksum = checksum[:-1]
	# print(sector)
	# print(checksum)

	for c in name:
		if c in letterCount:
			letterCount[c] += 1
		else :
			letterCount[c] = 1
		decodedName += right_caeser(c,int(sector))

	# print(letterCount)
	letterSort = sorted(letterCount.items(), key = lambda x: x[0])
	letterSort = sorted(letterSort, key = lambda x: x[1], reverse=True)
	# print(letterSort)

	for i in range(0,5):
		if letterSort[i][0] != checksum[i]:
			validChecksum = False
			break

	if validChecksum:
		sectorSum += int(sector)
		if 'northpole' in decodedName:
			print('North Pole objects found in sector ' + sector)

print('sectorSum = ' + str(sectorSum))