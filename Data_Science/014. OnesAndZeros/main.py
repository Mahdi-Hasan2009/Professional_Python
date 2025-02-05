def OnesAndZeros(n):
  ones = 0
  zeros = 0
  
  while (n):
    if n&1==1:
      ones+=1
    else:
      zeros+=1
    n>>=1
  print(f"Ones: {ones}\nZeros = {zeros}")

number = int(input("Enter a Number: "))
OnesAndZeros(number)
