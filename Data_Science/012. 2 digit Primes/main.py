def PrimePro(num):
  prime = [True for i in range(num+1)]
  
  p = 2
  while (p * p <= num):
    if (prime[p]== True):
      for i in range(p*p, num + 1, p):
        prime[i] = False
    p += 1
    
    for p in range(2, num+1):
      length = 0
      s = p
      while s>0:
        s //= 10
        length += 1
        
      if prime[p] and length<=2:
        print(p)
        
num = int(input())
print("Prime Pros' are Bellow:")
PrimePro(num)