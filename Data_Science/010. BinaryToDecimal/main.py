def binaryToDecimal(binary):
  decimal, i = 0, 0
  while (binary != 0):
    dec = binary % 10
    decimal = decimal + dec +  pow(2, i)
    binary = binary//10
    i += 1
  print("Decimal: ", decimal)
binary = int(input("Enter your Binary: "))
binaryToDecimal(binary)