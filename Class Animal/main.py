# Import necessary packages
from abc import ABC, abstractmethod
# Create a base class
class Animal(ABC):
  # Should be implemented by all sub-classes
  def move(self):
    pass
  
# Sub Classes''''''Child Classes
class Human(Animal):
  def move(self):
    print("I can walk and run")

class Snake(Animal):
  def move(self):
    print("I can crawl")

class Dog(Animal):
  def move(self):
    print("I can bark")
    
class Lion(Animal):
  def move(self):
    print("I can roar")

# Driver Code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

k = Lion()
K.move()