# Initialize dictionary 
test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Printing original dictionary
print("The original dictionary:" + str(test_dict))

# Initialize value 
K = 2

# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict: 
  if test_dict[key] == K: 
    res = res + 1

# printing result

print("Frequency of K is: " + str(res))