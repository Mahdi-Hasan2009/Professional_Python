import array as arr
# Create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: " + str(array_num))

# Count number of occurrence
print(f"Number of occurrences of the number 3 in said array: {str(array_num.count(3))}")

# Reverse the array
array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))