# Create class
class Vehicle:
  # Create int method
  def __init__(self, max_speed, milage):
    # Bind the arguments
    self.max_speed = max_speed
    self.mileage = milage
# Object creation
modelX = Vehicle(240, 18)
# Access the variables inside init method
print(f"Model Max Speed: {modelX.max_speed}")
print(f"Model Mileage: {modelX.mileage}")