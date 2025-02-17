# Program to swap two numbers without using third variable
def swap1(a,b):
  a = a ^ b
  b = b ^ a
  a = a ^ b
  print("After Swapping: a= ", a, "b= ",b)
  
def swap2(a,b):
  a = (a & b) + (a | b)
  b = a + (~b) + 1
  a = a + (~b) + 1
  print("After Swapping: a= ", a, "b= ",b)
  
def swap3(a,b):
  a = a + b
  b = a - b
  a = a - b
  print("After Swapping: a= ", a, "b= ",b)
  
swap1(1,2)
swap2(1,2)
swap3(1,2)