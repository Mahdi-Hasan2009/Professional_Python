'''==================
Parent class is also known as Super Class
and 
Child Class is also known as sub-class
============='''
class Person(object):
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber
  def display(self):
    print(self.name)
    print(self.idnumber)
    
class Employee( Person ):
  def __init__(self, name, idnumber, salary, post):
    self.salary = salary
    self.post = post
    # Invoking the __init__of the parent class
    Person.__init__(self, name, idnumber)
a = Employee("Rahul", 886012, 200000, "Intern")
a.display()