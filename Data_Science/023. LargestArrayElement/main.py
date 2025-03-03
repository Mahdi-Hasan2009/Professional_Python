# Programme to find the largest number of the array

def LargestArrayElement(a):
  length = len(a)
  
  if length == 1:
    return a[0]
  return max(a[0], LargestArrayElement(a[1:]))

a = []
length = int(input("Enter the length of the array: "))

for i in range(length):
  b = int(input("Enter the Element: "))
  a.append(b)
  
print("The largest number of the array is: ", LargestArrayElement(a))