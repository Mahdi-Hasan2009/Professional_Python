# Program to reverse  all bits of a number

def reverseBits(number):
  # Below variable will  hold the reversed bit number
  reversed = 0
  
  # While number is not 0
  while(number > 0):
    
    # Shift reversed number to left
    reversed <<= 1
    
   # Check if last bit is 0 or 1
   # If 1 add it using OR operator else leave
    if (number & 1 == 1):
      reversed ^= 1
     
    # Right shift to the original number
    number >>= 1
    
  return reversed 

number = int(input("Enter your number: "))       
print("Number with reversed bits: ", reverseBits(number))
