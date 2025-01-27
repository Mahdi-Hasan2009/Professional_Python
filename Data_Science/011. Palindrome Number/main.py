# Take input from the user
number = int(input("Enter your number: "))

# Store the original number for comparison later
original_number, reversed_number = number, 0

#  Reverse the Number
while number > 0:
  digit = number % 10
  reversed_number = reversed_number * 10 + digit
  number //= 10
  
# Check if the original number and the reversed number are same
if original_number == reversed_number:
  print(f'\'{original_number}\' is a palindrome')
else:
  print(f'\'{original_number}\' is not a palindrome')