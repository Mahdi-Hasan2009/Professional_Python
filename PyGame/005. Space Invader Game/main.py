import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_Height = 500
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_Height))

# Background
background = pygame.image.load('assets/background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('assets/')