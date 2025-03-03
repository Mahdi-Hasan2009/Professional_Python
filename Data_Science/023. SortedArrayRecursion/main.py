# Programme to check if a array is sorted or not

def check_sorted(a):
  # Checking length
  length = len(a)
  
  if length == 1 or length == 0:
    return 1
  return a[0] <= a[1] and check_sorted(a[1:])

a = [1, 2, 3, 4, 5, 8, 2]

if check_sorted(a):
  print("Yes the array is sorted.")
else:
  print("No the array is not sorted.")