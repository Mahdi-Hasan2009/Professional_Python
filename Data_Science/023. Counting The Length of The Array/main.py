# Programme to find the length of the array recursively

def length_of_array(a):
  if not a:
    return 0
  return 1 + length_of_array(a[1::2]) + length_of_array(a[2::2])

length = int(input("Enter the length of the array: "))
a = []
b = 1

def make_array(length, b):
  if length == 0:
    return
  a.append(int(input(f"Enter the element of {b} position: ")))
  make_array(length - 1, b + 1)

make_array(length, b)
print(f"Your array is: {a}\nLength of the array is:  {length_of_array(a)}")