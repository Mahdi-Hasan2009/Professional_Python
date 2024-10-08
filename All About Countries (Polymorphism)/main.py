# Class 1
class Bangladesh():
  def  capital(self):
    print("Dhaka is the capital of Bangladesh.")
    
  def  language(self):
    print("Bangla is most widely spoken language of Bangladesh.")
    
  def  type(self):
    print("Bangladesh will be a developed country.")
    
# Class 2
class USA():
  def  capital(self):
    print("Washington, D.C is the capital of USA.")
    
  def  language(self):
    print("English is most widely spoken language of USA.")
    
  def  type(self):
    print("USA is a self-centered country.")
    
# Object Creation
odj_bangla = Bangladesh()
obj_usa = USA()

# Common Interface
for country in (odj_bangla, obj_usa):
  country.capital()
  country.language()
  country.type()