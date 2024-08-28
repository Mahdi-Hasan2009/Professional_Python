valid = False
while not valid: #using nested while loop 
  try:
    n = int(input("Enter A Number: "))
    #Enter A Even Number
    while n%2==0:
      print("Bye")
    valid = True
  except ValueError:
    print("Invalid")