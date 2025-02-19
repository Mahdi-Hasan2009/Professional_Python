def totalFlips(number1, number2):
  flips = 00
  while number1 > 0 or number2 > 0:
    t1 = number1 & 1
    t2 = number2 & 1
    if t1 != t2:
      flips += 1
      
    number1 >>= 1
    number2 >>= 1
    
  return flips

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Number of flips needed: ", totalFlips(number1, number2))