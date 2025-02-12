def powerOf4(number):
  count = 0
  if (number&~(number-1))==number:
    while number > 1:
      number >>= 1
      count += 1
    if count % 2 == 0:
      print("4^", count//2)
      return True
    else:
      return False
  
n = int(input("Enter a number: "))

if powerOf4(n):
  print("\nThe number is power of 4.")
else:
  print("\nThe number is not power of 4.")