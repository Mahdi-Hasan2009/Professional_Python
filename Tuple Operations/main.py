tuple1 = ("tuple", False, 3.2, 1)
print(tuple1)

# Create a Tuple
tuple1 = (4, 6, 2, 8, 3, 1)
print(tuple1)
# Tuples are immutable so you can't ad new elements
# Using merge of tuples with + operators you can add an element and it will create a new tuple
tuple1 = tuple1 + (9,)
print(tuple1)

# Counts the numbers of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(850))

# Create a tuple
tuple1 = (2 ,4 ,3 , 5 , 4 , 6 , 7 , 8 , 6, 1)
# Used tuple[start:stop] the start index is inclusive and the stop index is exclusive 
_slice = tuple1[3:5]
print(_slice)
# If the start index isn't defined, is taken from beg inning of the tuple
_slice = tuple1[:6]
print(_slice)