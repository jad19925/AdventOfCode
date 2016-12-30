import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('--doorID', type=str)
args = parser.parse_args()

def passDoor1(doorID):
	foundLetters = 0
	loopCount = 0
	password = ''
	passwordSize = 8

	while foundLetters < passwordSize:
		hashVal = hashlib.md5(bytes(doorID + str(loopCount), encoding='utf-8'))
		if hashVal.hexdigest().startswith('00000'):
			password += hashVal.hexdigest()[5]
			print(hashVal.hexdigest())
			foundLetters += 1
		loopCount += 1
	return password

def passDoor2(doorID):
	foundLetters = 0
	loopCount = 0
	passwordSize = 8
	password = [None] * passwordSize

	while foundLetters < passwordSize:
		hashVal = hashlib.md5(bytes(doorID + str(loopCount), encoding='utf-8'))
		if hashVal.hexdigest().startswith('00000'):
			if int(hashVal.hexdigest()[5], 16) < passwordSize and password[int(hashVal.hexdigest()[5], 16)] == None:
				password[int(hashVal.hexdigest()[5], 16)] = hashVal.hexdigest()[6]
				print(hashVal.hexdigest())
				foundLetters += 1
		loopCount += 1
	return ''.join(password)

print('Door 1 Password: ' + passDoor1(args.doorID))
print('Door 2 Password: ' + passDoor2(args.doorID))