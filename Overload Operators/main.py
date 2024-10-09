class A:
  def __init__(self, a):
    self.a = a
  def __lt__(self, other):
    if(self.a < other.a):
      return "ob1 is less than ob2"
    else:
      return "ob2 is less than ob1"
  def __eq__(self, other):
    if(self.a == other.a):
      return "Both are equal"
    else:
      return "Not equal"
    
ob1 = A(2)
ob2 = A(3)
print("Passed Values: {}, {}".format(ob1.a, ob2.a))
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values: {}, {}".format(ob3.a, ob4.a))
print(ob3 == ob4)