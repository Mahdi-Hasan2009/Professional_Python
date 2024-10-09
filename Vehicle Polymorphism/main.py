class Ferrari:
  def fuel_type(self):
    print("Petrol")
  
  def max_speed(self):
    print("Max speed 350")
    
class BMW:
  def fuel_type(self):
    print("Diesel")
  
  def max_speed(self):
    print("Max speed 240")
    
ferrari = Ferrari()
bmw = BMW()

# Iterate objects of same type
for car in (ferrari, bmw):
  car.fuel_type()# Call methods without checking class of object
  car.max_speed()# Call methods without checking class of object