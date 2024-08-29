import random
#Importing Module
playing = True
number = str(random.randint(0,9))

print("I will generate a random number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
#Initiate loop till the condition is true
while playing:
  guess = input("Give me you best guess! \n")
  if number == guess:
    print("You win the game")
    print(f"The number was {number}")
    break
  
  else:
    print("Your guess isn't right. Try again. \n")