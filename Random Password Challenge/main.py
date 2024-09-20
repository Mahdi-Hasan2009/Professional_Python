import random

# A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ' '.join(tempList)

# Main program starts here
uppercaseLatter1 = chr(random.randint(65,90))# Generate a random Uppercase letter (based on ASCII code)
uppercaseLatter2 = chr(random.randint(65,90))# Generate a random Uppercase letter (based on ASCII code)
# Generate more characters here
# .....

# Generate password using all the characters ,in random order
password = uppercaseLatter1 + uppercaseLatter2 # + .....

# Output
print(password)