# Programme to find the length of the array recursively

def length_of_array(a):
  if not a:
    return 0
  return 1 + length_of_array(a[1::2]) + length_of_array(a[2::2])

length = int(input("\033[96mEnter the length of the array: \033[0m"))
a = []
b = 1

def make_array(length, b):
  if length == 0:
    return
  a.append(int(input(f"\033[31mEnter the element of {b} position: \033[0m")))
  make_array(length - 1, b + 1)

make_array(length, b)
print(f"\033[33mYour array is: {a}\033[0m\n\033[32mLength of the array is:  {length_of_array(a)}\033[0m")