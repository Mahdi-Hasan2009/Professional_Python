# Parent class

class Bird:
  def __init__(self):
    print("Bird is ready")
    
  def who_is_this(self):
    print("Bird")
    
  def swim(self):
    print("Swim faster")
    
# Child class

class Penguin(Bird):
  def __init__(self):
    super().__init__()
    print("Penguin is ready")
  
  def who_is_this(self):
    print("Penguin")
    
  def run(self):
    print("Run faster")
  
# Object creation

peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()