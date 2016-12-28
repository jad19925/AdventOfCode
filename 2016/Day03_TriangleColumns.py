import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--triFile', type=str)
args = parser.parse_args()

triangleFile = open(args.triFile, 'r')

testTriangles = triangleFile.readlines()
triangleCount = 0

triangleMod = 0
newTriangleA = []
newTriangleB = []
newTriangleC = []

for triangle in testTriangles:
	edges = [int(edge) for edge in triangle.split()]
	
	newTriangleA.append(edges[0])
	newTriangleB.append(edges[1])
	newTriangleC.append(edges[2])

	# edges.sort()
	# sumSmall = edges[0] + edges[1]
	# print(edges)
	# if sumSmall > edges[2]:
	# 	triangleCount += 1

	if triangleMod == 2:
		# print(newTriangleA)
		# print(newTriangleB)
		# print(newTriangleC)

		newTriangleA.sort()
		sumSmall = newTriangleA[0] + newTriangleA[1]
		if sumSmall > newTriangleA[2]:
			triangleCount += 1
		newTriangleB.sort()
		sumSmall = newTriangleB[0] + newTriangleB[1]
		if sumSmall > newTriangleB[2]:
			triangleCount += 1
		newTriangleC.sort()
		sumSmall = newTriangleC[0] + newTriangleC[1]
		if sumSmall > newTriangleC[2]:
			triangleCount += 1

		newTriangleA = []
		newTriangleB = []
		newTriangleC = []
	triangleMod = (triangleMod + 1) % 3

print('Total Triangles = ' + str(triangleCount))