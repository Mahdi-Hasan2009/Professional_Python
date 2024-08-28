def EnterAge(age):
  
#Define Function to Take Input as Natural Number
  if age < 0:
    raise ValueError("Only Positive Integers are Allowed")
  if age % 0 == 0:
    print("Age is Even")
  else:
    print("Age is Odd")
    
try:
  num = int(input("Enter your Age: "))
  EnterAge(num)
  
#Handles Value Error Exception
except ValueError:
  print("Only Positive Integers are Allowed")
  
except:
  print("Something is Wrong")