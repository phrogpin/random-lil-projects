# something for the gambling dice game with drinking idk
import random
import math
import time 

import pygame
import sys

# initialize pygame
pygame.init()

# colors 
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
pink = (255, 0, 255)
purple = (128, 0, 128)
orange = (255, 165, 0)
yellow = (255, 255, 0)

# initializing the background color variable 
background_color = [0, 0, 255]

# screen settings 
screen_width = 1300
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Gambling Dice Game")

# button dimensions 
button_width = 200 
button_height = 50

# fonts 
font = pygame.font.Font(None, 36)

# create button rects 
start_button = pygame.Rect(screen_width // 2 - button_width // 2, 200, button_width, button_height)
settings_button = pygame.Rect(screen_width // 2 - button_width // 2, 300, button_width, button_height)
how_to_play_button = pygame.Rect(screen_width // 2 - button_width // 2, 400, button_width, button_height)
exit_button = pygame.Rect(screen_width // 2 - button_width // 2, 500, button_width, button_height)

# creating frames for the buttons
button_frames = [pygame.Rect(button.left - 10, button.top - 10, button.width + 20, button.height + 20) for button in [start_button, settings_button, how_to_play_button, exit_button]]

# dice settings
dice_width = 40 
dice_height = 40
dice_x = screen_width // 2
dice_y = screen_height // 2

# create a clock object to control the frame rate
clock = pygame.time.Clock()