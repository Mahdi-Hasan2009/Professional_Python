def checkIfSame(number1, number2):
  if (number1 ^ number2) !=0 :
    print("The numbers are not equal")
  else:
    print("The numbers are equal")
    
num1 = int(input("Enter the first number to compare: "))
num2 = int(input("Enter the second number to compare: "))
checkIfSame(num1, num2)