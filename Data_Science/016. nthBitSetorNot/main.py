def nthBitSetorNot(number, n):
  if  number & (1<<(n-1)):
    print("\nSET")
  else:
    print("\nNOT SET")
    
number = int(input("Enter Number: "))
n = int(input("Enter bit number: "))
nthBitSetorNot(number, n)