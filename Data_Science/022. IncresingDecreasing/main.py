def IncresingDecreasing(n, num):
  if n<1 or n> num:
    return
  print(n)
  IncresingDecreasing(n-1, num)
  print(n)
  
  
n = int(input("Enter a number for IncresingDecreasing: "))
IncresingDecreasing(n, n)
  