def power_of_2(number):
  if number == 0:
    return 0
  if (number & ~(number-1))==number:
    return 1
  return 0

n = int(input("Enter a number: "))

if power_of_2(n):
  print("\nThe number is power of two.")
else:
  print("\nThe number is not power of two.")