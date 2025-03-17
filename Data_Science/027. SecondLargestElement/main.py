def print2LArgest(a, arr_size):
  largest = secondLargest = -21515551515512200
  for i in range(arr_size):
    if a[i]>largest:
      secondLargest = largest
      largest = a[i]
    elif a[i]>secondLargest and a[i] != largest:
      secondLargest = a[i]
  
  print(secondLargest)

arr = [191, 84, 140, 45, 74, 74, 47, 17, 8, 12]
arr_size = len(arr)

print2LArgest(arr, arr_size)