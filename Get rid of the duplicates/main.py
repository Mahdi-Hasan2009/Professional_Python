# Initialize dictionary
test_dictionary = {'Codingal' : 2, 'is' : 2, 'for': 2, 'Coding' : 1}

# Printing original dictionary
print(f"The original dictionary :{str(test_dictionary)}")

# Initialize value
K = 2

# Using loop
# Selective key values in dictionary
res = 0
for key in test_dictionary:
  if test_dictionary[key] == K:
    res = res + 1
    
# Printing result
print(f"Frequency of K is : {str(res)}")