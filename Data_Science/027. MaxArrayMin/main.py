# Minimum function
def minElement(a, size):
  temp = a[0]
  for i in range(1, size):
    temp = min(temp, a[i])
  return temp

# Maximum function
def maxElement(a, size):
  temp = a[0]
  for i in range(1, size):
    temp = max(temp, a[i])
  return temp

arr = [191, 84, 140, 45, 74, 74, 47, 17, 8, 12]
size = len(arr)
print(f"Minimum: {minElement(arr, size)}\nMaximum: {maxElement(arr, size)}")