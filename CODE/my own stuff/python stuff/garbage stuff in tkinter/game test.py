import pygame
import sys

# pygame initialization
pygame.init()

# window variables 
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Movement")

# character variables
character_width = 40
character_height = 40
character_x = screen_width // 2
character_y = screen_height // 2
walk_speed = 5
#jump_force = 10 
gravity = 0.5 
friction = 0.2

# clock object to control framerate
clock = pygame.time.Clock()

# character state
is_jumping = False

# game loop
running = True
velocity = [0, 0]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handles user input for character movement

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        velocity[0] = -walk_speed
    elif keys[pygame.K_d]:
        velocity[0] = walk_speed
    else:
        velocity[0] *= (1 - friction)

    if keys[pygame.K_s]:
        velocity[1] = walk_speed
    else:
        velocity[1] *= (1 - friction)
    
    # handles jumping 
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity[1] = -10
        is_jumping = True

    character_x += velocity[0]
    character_y += velocity[1]

    # clears the screen
    screen.fill((0, 0, 0))
    
    # restrict character within the screen boundaries 
    character_x = max(0, min(screen_width - character_width, character_x))
    character_y = max(0 ,min(screen_height - character_height, character_y))
    
    # gravity 
    if character_y >= screen_height - character_height:
        character_y = screen_height - character_height
        velocity[1] = 0
        is_jumping = False
        
    # apply gravity
    velocity[1] += gravity
    
    # draws the block character
    pygame.draw.rect(screen, (255, 0, 0), (character_x, character_y, character_width, character_height))

    # updates the display for the game
    pygame.display.update()

    # limits the framerate to 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()
