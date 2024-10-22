import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change  events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1 
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE= pygame.Color('lightblue')
DARKBLUE= pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite()):
  # Constructor method
  def __init__(self, color, height, width):
    # Call to the parent class (Sprite) constructor
    super().__init__()
    # Create the sprite's surface with dimensions and color
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    # Get the sprite's rect defining its position and size
    self.rect = self.image.get_rect()
    # Set initial velocity with random direcion
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    

# Method to update the sprite's position
def update(self):
  # Move the sprite by its velocity
  self.rect.move_ip(self.velocity)
  # Flag to track if sprite hits boundary
  boundary_hit = False
  # Check for collision with left or right boundaries and reverse direction
  if self.rect.left <=0 or self.rect.right >= 500:
    self.velocity[0] =- self.velocity[0]
    boundary_hit = True   
    
  # Check for collision with top or bottom boundaries and reverse direction
  if self.rect.top <=0 or self.rect.bottom >= 400:
    self.velocity[1] =- self.velocity[1]
    boundary_hit = True
    
  # If a boundary was hit, post events to change colors
  if boundary_hit:                        
    pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
    pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

# Method to change the sprite's color
def change_color(self):
  self.image.fill(random.choice[YELLOW, MAGENTA, ORANGE, WHITE])

# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
  

# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
