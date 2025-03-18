# Accept array, its size and group size
""" Output will be 84 191 45 140 74 74 17 47 12 8 """
# For [191, 84, 140, 45, 74, 74, 47, 17, 8, 12] this input
def reverse(arr, arr_size, n):
  temp = 0
  while temp < arr_size:
    start = temp
    # When arr_size/n is not divisible
    end = min(temp +  n -1, arr_size - 1)
    # Reverse the sub-array [start, end]
    while start < end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1
    temp += n
    
arr = [191, 84, 140, 45, 74, 74, 47, 17, 8, 12]
arr_size = len(arr)
n = 2
reverse(arr, arr_size, n)

for i in range(0, arr_size):
  print(arr[i], end = " ")