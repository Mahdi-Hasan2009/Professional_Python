# Program to find HCF/GCD

# Enter 2 numbers
numberLargest, numberSmallest = int(input("Enter the Largest Number: ")), int(input("Enter the Smallest Number: "))

# Using Eucliden Algorithm
def hcf(numberSmallest, numberLargest):
  while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest  = numberLargest % numberSmallest
    numberLargest = numberStore
  return numberLargest

lcm = int((numberSmallest / hcf(numberSmallest, numberLargest))*numberLargest)
print("LCM is: ", lcm)