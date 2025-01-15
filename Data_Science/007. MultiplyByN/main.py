# Programme to find multiple with 1 and N iteration
# F or 1 iteration simply multiply
def o1(n, m):
  total = n * m
  print(f'Result is: {total}\n1 iteration: 1')
  
# For N iteration run a loop
def oN(n,m):
  total = 0
  for i in range(1, n + 1):
    total +=m
  print(f'N iteration: {n}')
  
m = int(input('Enter \'a\' for a*b : '))
n = int(input('Enter \'b\' for a*b : '))

o1(m,n)
oN(m,n)