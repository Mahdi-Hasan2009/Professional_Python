# Program to check if the user entered number is odd or even using only bitwise operator

# Returns true if n in=s even, else odd
def  isEvenOdd(n):
  # XOR with 1 equals n+1
  if (n^1 == n+1):
    return True
  else:
    return False
  
number = int(input("Enter your number: "))

if isEvenOdd(number):
  print(f"{number} is Even")
else:
  print(f"{number} is Odd")