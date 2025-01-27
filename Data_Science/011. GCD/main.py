# Program to find HCF/GCD

# Enter 2 numbers
numberLargest, numberSmallest = int(input("Enter the Largest Number: ")), int(input("Enter the Smallest Number: "))

# Using Eucliden Algorithm
while(numberSmallest):
  numberStore = numberSmallest
  numberSmallest  = numberLargest % numberSmallest
  numberLargest = numberStore

print(f"HCF is: {numberLargest}")