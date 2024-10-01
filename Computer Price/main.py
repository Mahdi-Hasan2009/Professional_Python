class Computer:
  def __init__(self):
    self.__max_price = 900
    
  def sell(self):
    print("Selling Price: {}".format(self.__max_price))
    
  def setMaxPrice(self, price):
    self.__max_price = price
    
c = Computer()
c.sell()

# Change the price in wrong way
c.__max_price = 1000
c.sell()

# Using setter function
c.setMaxPrice(1000)
c.sell()