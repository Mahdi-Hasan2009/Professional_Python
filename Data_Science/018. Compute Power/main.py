def computePower(x,y):
  # Default total is one
  result = 1
  
  while (y>0):
    # y is even
    if y%2 == 0:
      x = x * x
      y>>=1
    else:
      result = result * x
      y= y - 1
  return result
  
x = int(input("Enter the base: "))
y = int(input("Enter the power: "))

print("Total: ", computePower(x,y))
      