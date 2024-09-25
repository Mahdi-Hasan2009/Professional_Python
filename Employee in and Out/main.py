# Create class
class Employee:
  # Initializing
  def __init__(self):
    print("Employee created")
  # Calling constructor
  def __del__(self):
    print("Destructor called")
def Create_obj():
  print('Deleting a object...')
  obj = Employee()
  print('Function end')
  del obj# for __del__
  # return obj to call __init__
print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End...")