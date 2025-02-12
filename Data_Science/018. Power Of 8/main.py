def powerOf8(number):
  bitPosition =  0
  mask = 0
  
  while bitPosition <= 63:
    mask  <<= bitPosition
    mask = 1
    
    if mask == number:
      return True
    bitPosition += 3
    mask = 1
  return False


number = int(input("Enter your number: "))

if powerOf8(number):
  print(f"Yes, {number} is power of 8")
else:
  print(f"No, {number} is not power of 8")