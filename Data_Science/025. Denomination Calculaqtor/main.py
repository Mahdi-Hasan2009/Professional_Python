""" 
==================================================
******************  Cash Breakdown  ******************
==================================================
 Soul Code: A Simple Money Breakdown System 
--------------------------------------------------
   Enter a total amount, and the program will 
   calculate how many notes of each denomination 
   are needed. 
--------------------------------------------------
total_amount = (int)(input("Enter the total amount: "))

list_of_notes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in list_of_notes:
  number_of_notes = total_amount // i
  total_amount  = total_amount % i
  if number_of_notes != 0:
    print(f"The number of notes of {i} is {number_of_notes}")
    
==================================================
"""
# Code for Stylish Output

import pygame
pygame.mixer.init()

class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    ENTER = "\n"

total_amount = int(input(f"{Colors.ENTER}{Colors.CYAN}{Colors.BOLD}Enter the total amount: {Colors.RESET}"))
pygame.mixer.music.load("cash.mp3")
pygame.mixer.music.play()

list_of_notes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print(f"{Colors.ENTER}{Colors.UNDERLINE}{Colors.HEADER}Breakdown of Notes:{Colors.RESET}{Colors.ENTER}")

for note in list_of_notes:
    number_of_notes = total_amount // note
    total_amount %= note
    if number_of_notes != 0:
        print(f"{Colors.YELLOW}{Colors.BOLD}\U0001F449 Notes of {note}: {Colors.RED}{number_of_notes}{Colors.RESET}")

print(f"\n{Colors.GREEN}{Colors.BOLD}\u2705 Calculation Complete!{Colors.RESET}")

while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(2000)