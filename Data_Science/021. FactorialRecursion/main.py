# Program to find factorial of any number with recursion

def fac(n):
  # Base Class
  if (n == 0 or n == 1):
    return 1
  # Factorial of n = n*(n-1)*(n-2)*.....*1
  return n*fac(n-1)

n = int(input("Enter your number: "))
print(f"Factorial of {n} is: {fac(n)}")