def headrec(n, num):
  # Base case: if n exceeds num, terminate the recurtion
  
  if n > num:
    return
  # Recursive call with the next value
  headrec(n + 1, num)
  # Print the current value of n after returning from the recursive call
  print(n)
  
# Prompt the user to enter the value of n
n = int(input("Enter n to print n to 1: "))

headrec(1, n)