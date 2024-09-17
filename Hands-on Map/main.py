# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x,y: x + y, numbers1, numbers2)
print("Addition of two lists: ")
print(list(result))

# Using map
nums = [1, 2, 3, 4, 5]
def sq(n):
  return n*n #or n**2
square = list(map(sq, nums))
print("Squares of numbers in list: ")
print(square)