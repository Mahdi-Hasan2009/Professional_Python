# Programme to find reverse a number using recursion

def reverse_number(num):
  if num > 0:
    last = num % 10
    if num // 10 > 0:
      current_number = reverse_number((int)(num // 10))
      return last * pow(10, len(str(current_number))) + current_number
    return num
  
n = (int)(input("Enter a number: "))
print(f"Reverse of {n} is {reverse_number(n)}")