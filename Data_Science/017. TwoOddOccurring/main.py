def printTwoOdd(arr, size):
  xor_of_2 = arr[0]
  
  x, y = 0,0 
  
  # This will hold the rightmost set bot from xor_of_2 Set bit = 0
  
  for i in range(1, size):
    xor_of_2 ^= arr[i]
    
  set_bit = xor_of_2 & ~(xor_of_2 - 1)
  
  for i in range(size):
    if (arr[i] & set_bit):
      x = x ^ arr[i]
    else:
      y ^= arr[i]
  
  print("The two ODD elements are ", x , "&", y)
  
# Create an empty array
arr = []

arr_size = int(input("Enter the size of the array: "))
for i in range(0, arr_size):
  z = int(input("Enter element: "))
  arr.append(z)
  
printTwoOdd(arr, arr_size)