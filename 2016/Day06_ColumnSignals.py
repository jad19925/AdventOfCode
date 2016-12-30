import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--signalFile', type=str)
args = parser.parse_args()

signalFile = open(args.signalFile, 'r')

corruptedSignals = [line.rstrip("\r\n") for line in signalFile]
letterCount = [{'a':0}] * len(corruptedSignals[0])

# for signal in corruptedSignals:
# 	edges = [int(edge) for edge in triangle.split()]
# 	edges.sort()
# 	sumSmall = edges[0] + edges[1]
# 	# print(edges)
# 	if sumSmall > edges[2]:
# 		triangleCount += 1

print(letterCount)