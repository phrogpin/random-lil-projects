import pygame
import random
import math

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
DICE_SIZE = 1  # inches
DICE_SPACING = 20
FPS = 60
NUM_DICE = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rolling 2D Dice")
clock = pygame.time.Clock()

def draw_dice(value, x, y, rotation):
    # Create a six-sided dice shape
    dice_rect = pygame.Rect(x, y, DICE_SIZE * 100, DICE_SIZE * 100)

    # Draw the dice
    pygame.draw.rect(screen, WHITE, dice_rect)
    pygame.draw.circle(screen, BLACK, (x + 50, y + 50), 10)  # Center dot

    if value == 1:
        pygame.draw.circle(screen, BLACK, (x + 50, y + 50), 10)
    elif value == 2:
        pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 10)
    elif value == 3:
        pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 50, y + 50), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 10)
    elif value == 4:
        pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 30, y + 70), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 10)
    elif value == 5:
        pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 50, y + 50), 10)
        pygame.draw.circle(screen, BLACK, (x + 30, y + 70), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 10)
    elif value == 6:
        pygame.draw.circle(screen, WHITE, (x + 50, y + 50), 10)
        pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 30), 10)
        pygame.draw.circle(screen, BLACK, (x + 30, y + 50), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 50), 10)
        pygame.draw.circle(screen, BLACK, (x + 30, y + 70), 10)
        pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 10)

    # Rotate the dice
    rotated_dice = pygame.transform.rotate(screen, rotation)

    # Get the rect of the rotated dice and adjust its position
    rect = rotated_dice.get_rect()
    rect.center = (x, y) 

    # Draw the rotated dice on the screen
    screen.blit(rotated_dice, rect.topleft)

def main():
    rolling = False
    values = [1] * NUM_DICE
    dice_width = DICE_SIZE * 100
    total_width = NUM_DICE * (dice_width + DICE_SPACING) - DICE_SPACING
    x_positions = [i * (dice_width + DICE_SPACING) + (SCREEN_WIDTH - total_width) // 2 for i in range(NUM_DICE)]
    rotations = [0] * NUM_DICE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if not rolling:
                    if event.key == pygame.K_SPACE:
                        rolling = True
                        values = [random.randint(1, 6) for _ in range(NUM_DICE)]
                        rotations = [0] * NUM_DICE

        screen.fill((0, 0, 0))

        if rolling:
            for i in range(NUM_DICE):
                rotations[i] += random.randint(5, 15)
                if rotations[i] >= 360:
                    rotations[i] = 0

            if random.random() < 0.05:
                rolling = False

        for i in range(NUM_DICE):
            draw_dice(values[i], x_positions[i], 50, rotations[i])

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
