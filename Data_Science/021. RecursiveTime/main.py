def fac(n):
  if (n==0 or n==1):
    return 1
  return n*fac(n-1)

n = int(input("Enter your number: "))
def echo(a):
  print(a)
  
echo(f"Factorial of {n} is: {fac(n)}")
echo("The Time Complexity of this program is O(nlogn).")