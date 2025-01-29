a = 3000
for num in range(1, a+1):
  c = 0
  rev = 0
  temp = num
  for i in range(1, temp+1):
    if temp % i == 0:
      c+=1
  if c==2:
    while temp > 0:
      rev = rev*10+(temp%10)
      temp //= 10
    if rev == num:
      print(num)