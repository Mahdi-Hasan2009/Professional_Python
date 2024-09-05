def multiple_tuple(nums):
  temp = list(nums)
  product = 1
  for x in temp:
    product *= x
  return product
nums = (4, 3, 2, 2, -1, 18)
print("Original Tuple: ")
print(nums)
print(f"Product - multiplying all the numbers of the said tuple: {multiple_tuple}")

nums = (2,4,8,8,3,2,9)
print("\nOriginal Tuple: ")
print(nums)
print(f"Product - multiplying all the numbers of the said tuple: {multiple_tuple}")