# Program to find the numbers from 1 to 10 using recursive function

def print1to10(n, m):
  # Base Class
  if (n>m):
    return
  print(n)
  
  print1to10(n+1, m)
  
n = int(input("From which number you want: "))
m = int(input("Till which number you want: "))

print1to10(n, m)