import math

def printPowerSize(set, setSize):
  PowerSetSize = (int) (math.pow(2, setSize))
  outer, inner = 0, 0
  
  for outer in range(0, PowerSetSize):
    for inner in range(0, setSize):
      if (outer & (1 << inner)) > 0:
        print(set[inner], end="")
    print("")

size =  int(input("Enter array size: "))

set = []
for i in range(0, size):
  n = int(input("Enter element: "))
  set.append(n)
  
printPowerSize(set, len(set))