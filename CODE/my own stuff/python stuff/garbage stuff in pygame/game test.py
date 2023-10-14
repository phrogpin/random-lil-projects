import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Movement")

# Character settings
character_width = 40
character_height = 40
character_x = screen_width // 2
character_y = screen_height // 2
walk_speed = 5
friction = 0.2

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
velocity = [0, 0]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        velocity[0] = -walk_speed
    elif keys[pygame.K_d]:
        velocity[0] = walk_speed
    else:
        velocity[0] *= (1 - friction)

    if keys[pygame.K_w]:
        velocity[1] = -walk_speed
    elif keys[pygame.K_s]:
        velocity[1] = walk_speed
    else:
        velocity[1] *= (1 - friction)

    character_x += velocity[0]
    character_y += velocity[1]

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # restrict character within the screen boundaries 
    character_x = max(0, min(screen_width - character_width, character_x))
    character_y = max(0 ,min(screen_height - character_height, character_y))

    # Draw the character
    pygame.draw.rect(screen, (255, 0, 0), (character_x, character_y, character_width, character_height))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
