def powerSetStringSize(set, setSize):
  powerSetSize = 2 ** setSize
  outer, inner = 0, 0
  
  for outer in range(0, powerSetSize):
    for inner in range(0, setSize):
      if (outer & (1 << inner)) > 0:
        print(set[inner], end="")
    print("")
    
size = int(input("Enter array size: "))
set = []
for i in range(0, size):
  str = input("Enter element: ")
  set.append(str)
  
powerSetStringSize(set, len(set))