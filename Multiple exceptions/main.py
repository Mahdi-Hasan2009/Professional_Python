try:
  num1, num2 = eval(input("Enter Two Numbers, Separated by Comma: "))
  result = num1 / num2
  print(f"Result is {result}")
#Using Multiple Except Block For Different type of error

except ZeroDivisionError:
  print("Division by 0 is Error !!")
  
except SyntaxError:
  print("Comma is missing. Enter The Number separated by comma like this 1,2") 
  
except:
  print('Wrong Input')
  
else:
  ("No Exceptions")

finally:
  print("This will execute no matter what")