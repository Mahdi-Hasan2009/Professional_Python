def divide(ourDivided, ourDivisor):
  # Check if divisor is +ve  or -ve
  sign = (-1 if((ourDivided) < 0) ^ (ourDivisor < 0) else 1)
  
  # Make both positive
  ourDivided = abs(ourDivided)
  ourDivisor = abs(ourDivisor)
  
  quotinetNumber = 0
  tempNumber = 0
  
  # Go from 31 to 0 and accumulate all valid bits
  
  for i in range(31, -1, -1):
    if (tempNumber + (ourDivisor << i) <= ourDivided):
      tempNumber += ourDivisor << i
      quotinetNumber |= 1 << i
      
  if sign == -1:
    quotinetNumber = -quotinetNumber
  return quotinetNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print(f"Result of: {a} / {b} is {divide(a,b)}")