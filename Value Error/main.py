# Using a Try and Except
try:
  number = int(input("Enter A Number: "))
  print(f'The Number Entered is {number}')
# Using Value Error
except ValueError as ex:
  print(f"Exception {ex}")