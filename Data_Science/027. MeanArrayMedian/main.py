# Mean of an array = sum of the array/length of the array

def mean_of_array(arr, arr_size):
  total_sum = 0
  for i in range(0, arr_size):
    total_sum += arr[i]
  return float(total_sum/arr_size)

# Median for a sorted array depends on odd and even

def median_of_array(arr, arr_size):
  sorted(arr)
  
  if arr_size % 2 != 0:
    return float(arr[int(arr_size/2)])
  return float((arr[int(arr_size/2)]+arr[int(arr_size-1)/2])/2.0)

arr = [191, 84, 140, 45, 74, 74, 47, 17, 8, 12]
arr_size = len(arr)

print(f"Mean of the array is : {mean_of_array(arr, arr_size)}")
print(f"Median of the array is: {median_of_array(arr, arr_size)}")