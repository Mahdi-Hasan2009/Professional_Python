# Class creation
class myClass:
  # Private variable
  __privateVar = 27
  # Private method
  def __privMeth(self):
    print("I'am inside class myClass")
  # Function to print value of private variable
  def hello(self):
    print("Private Variable value: ",myClass.__privateVar)
      
# Object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth