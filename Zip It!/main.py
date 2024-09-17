# Zip elements of two lists
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

# Zip elements of two lists
# Print elements one by one, but elements of 2nd list will be reverse in order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
  print(x, y)
  
# Zip into dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))