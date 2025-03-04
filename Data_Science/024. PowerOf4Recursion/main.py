# Program to sand if a number power of 4 or not

# Take input
n = (int)(input("\033[96mEnter a number: \033[0m"))

def power_of_4(n):
  if n <= 0:
    return False
  elif n == 1:
    return True
  elif n % 4 == 0:
    return power_of_4(n / 4)
  else:
    return False

if power_of_4(n):
  print("\033[32mPower of 4\033[0m")
else:
  print("\033[31mNot Power of 4\033[0m")