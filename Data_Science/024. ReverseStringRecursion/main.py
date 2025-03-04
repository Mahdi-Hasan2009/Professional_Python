# Program to reverse a string using recursion

def reverse_string(s):
  if  len(s) == 1:
    return s[0]
  first_car = s[0]
  return reverse_string(s[1:]) + first_car

s = input("\033[96mEnter a  string: \033[0m")
print(reverse_string(s))