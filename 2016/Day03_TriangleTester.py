import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--triFile', type=str)
args = parser.parse_args()

triangleFile = open(args.triFile, 'r')

testTriangles = triangleFile.readlines()
triangleCount = 0

for triangle in testTriangles:
	edges = [int(edge) for edge in triangle.split()]
	edges.sort()
	sumSmall = edges[0] + edges[1]
	# print(edges)
	if sumSmall > edges[2]:
		triangleCount += 1

print('Total Triangles = ' + str(triangleCount))