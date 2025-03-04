# Program to fin power of 2 or not
import pygame
pygame.mixer.init()

n =  int(input("\033[96mEnter a number: \033[0m"))

def check_if_power_of_2(n):
  if n <= 0:
    return False
  if n == 1:
    return True
  if n % 2 == 0:
    return check_if_power_of_2(n/2)
  return False

if check_if_power_of_2(n):
  print("\033[32mWow!! We have a power of 2.\033[0m")
  pygame.mixer.music.load("correct-choice-43861.mp3")
else:
  print("\033[31mOops!! Not a power of 2.\033[0m")
  pygame.mixer.music.load("error-4-199275.mp3")
  
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(10) # Check in every 10ms