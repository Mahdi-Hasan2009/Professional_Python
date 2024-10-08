# Import necessary Modules
from abc import ABC, abstractmethod

# Create base class
class Absclass(ABC):
  # Function to print a value
  def print(self,x):
    print("Passed value {}".format(x))
  
  # Abstract Method
  @abstractmethod
  def task(self):
    print("We are inside Absclass task")
    
# Create sub class
class test_class(Absclass):
  def task(self):
    print("We are inside test_class task")
    
# Object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)