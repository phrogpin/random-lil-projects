import pygame
import sys
import main

def settings_screen(screen, screen_width, screen_height):
    # initialize settings variables 
    fullscreen = False
    background_color = main.green
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height), pygame.FULLSCREEN)
                    else:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height))
                elif event.key == pygame.K_c:
                    if background_color == main.green:
                        background_color = main.blue
                    else:
                        background_color = main.green
                        
        # clear the screen 
        main.screen.fill(main.white)
        
        # draw the settings screen
        pygame.draw.rect(main.screen, background_color, (0, 0, main.screen_width, main.screen_height))
        settings_text = main.font.render("Settings", True, main.white)
        fullscreen_text = main.font.render("toggle fullscreen (press 'F')", True, main.white)
        color_text = main.font.render("change color (press 'C')", True, main.white)
        back_text = main.font.render("back to menu (press 'esc')", True, main.white)
        main.screen.blit(settings_text, (10, 10))
        main.screen.blit(fullscreen_text, (10, 60))
        main.screen.blit(color_text, (10, 110))
        main.screen.blit(back_text, (10, 160))
        
        pygame.display.flip()
