import pygame

pygame.init()
# Create a display surface object of specific dimension
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
GREEN = (0, 255, 0)
# Draw solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)# 300, 300 co ordinates and 50 radius
# Draw outlined circle
pygame.draw.circle(window, (255, 0, 255), (300, 300), 50, 3)# 3 is border for this it is hollow means without fill
# Draws the surface object to the screen
pygame.display.update()
# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
      
# Quit pygame
pygame.quit()