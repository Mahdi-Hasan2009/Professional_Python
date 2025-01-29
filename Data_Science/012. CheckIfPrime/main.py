from math import sqrt

number = int(input("Enter a Number: "))

if number > 1:
  for i in range(2, int(sqrt(number))+1):
    if number % i == 0:
      print(f"{number} is not a prime number.")
      break
  else:
    print(f"{number} is a prime number.")
else:
  print(f"{number} is not a prime number.")