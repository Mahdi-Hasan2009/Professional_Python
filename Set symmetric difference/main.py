def symmetric_difference(set1, set2):
  print("\nOriginal sets: ")
  print(set1)
  print(set2)
  result = set1.symmetric_difference(set2)
  print("Symmetric difference of setC1 - setC2: ")
  return result

setB1 = set([1, 1, 2, 3, 4, 5])
setB2 = set([1, 5, 6, 7, 8, 9])

print("Result of B Sets: ")
print(setB1, setB2)