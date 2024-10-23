import pygame
import random

from pygame.sprite import _Group

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400 
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize pygame
pygame.init()

# Load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))


# Load fonts once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
  def __init__(self, color, height, width):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(pygame.Color('dodgerblue')) # Background color of sprite
    pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
    self.rect = self.image.get_rect()
    
def move(self, x_change, y_change):
  self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH -self.rect.width), 0)
  self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT -self.rect.height), 0)
  
# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

# Create sprites
sprite1 = Sprite(pygame.Color('white'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('aqua'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

# Game loop control variable
running, won = True, False
clock = pygame.time.Clock()

# Main game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
      running = False
          
  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
    sprite1.move(x_change, y_change)
    
    if sprite1.rect.colliderect(sprite2.rect):
      all_sprites.remove(sprite2)
      won = True
      
  # Drawing
  screen.blit(background_image, (0, 0))
  all_sprites.draw(screen)
  
  # Display win message
  if won:
    win_text = font.render("You win!", True, pygame.Color('black'))
    screen.blit(win_text, ((SCREEN_WIDTH - win_text)))