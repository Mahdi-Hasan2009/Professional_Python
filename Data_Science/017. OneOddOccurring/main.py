# Program to find the element not making a pair

# Function to calculate the number that is odd occurring

def OddOccurring(arr):
  # Initialize result
  res = 0
  
  # Traverse the array
  for element in arr:
    # XOR with the result
    res = res ^ element
    
  return res

# Initialize our array
arr = []

# Take array size as input
n = int(input("Enter array size: "))

# Take array element input
while(n):
  num = int(input("Enter array size: "))
  arr.append(num)
  n-=1
  
print("\n\nOdd occurring number is: ", OddOccurring(arr))