import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('assets/background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
  enemyImg.append(pygame.image.load('assets/enemy.png'))
  enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
  enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
  enemyX_change.append(ENEMY_SPEED_X)
  enemyY_change.append(ENEMY_SPEED_Y)
  
# Bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
