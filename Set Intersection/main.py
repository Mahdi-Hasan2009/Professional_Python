setX = {"green", "blue"}
setY = {"blue", "yellow"}
print("Original set elements:")
print(setX)
print(setY)

print("\nIntersection of two said sets: ")
setZ = setX.intersection(setY)
print(setZ)

print("\nUnion of two said sets: ")
setZ = setX.union(setY)
print(setZ)

print("\nDifference of two said sets: ")
setZ = setX.difference(setY)
print(setZ)

print("\nDifference of two said sets: ")
setZ = setY.difference(setX)
print(setZ)

print("\nSymmetric Difference of two said sets: ")
setZ = setX.symmetric_difference(setY)
print(setZ)