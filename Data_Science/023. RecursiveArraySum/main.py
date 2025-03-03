# Programme to find the sum of all elements in an array using recursion

def sum_array(a):
  length = len(a)
  
  if length == 1:
    return a[0]
  else:
    return a[0] + sum_array(a[1:])
  
length = int(input("Enter the length of the array: "))
a= []

for i in range(length):
  a.append(int(input("Enter the element: ")))
  
print("Array total sum: %d" % sum_array(a))