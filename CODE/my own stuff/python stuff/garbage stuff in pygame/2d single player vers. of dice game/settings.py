import pygame
import sys
import main
import random

def settings_screen(screen, screen_width, screen_height):
    # initialize settings variables 
    fullscreen = False
    background_color = main.green
    running = True
    color_picker_active = False
    
    # colors for the color picker
    colors = {
        "Blue": main.blue,
        "Green": main.green,
        "Red": main.red,
        "Yellow": main.yellow,
        "Orange": main.orange,
        "Purple": main.purple,
        "Pink": main.pink,
        "Black": main.black,
        "White": main.white,
    }
    color_buttons = []
    
    # create a list of color buttons
    for i, (color_name, color) in enumerate(colors.items()):
        # create a rect for the button
        color_button = pygame.Rect(50, 200 + i * 50, 150, 40)
        # add the button to the list of color buttons
        color_buttons.append((color_name, color, color_button))
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # check for key presses
            if event.type == pygame.KEYDOWN:
                # check if the user pressed the 'f' key to toggle fullscreen
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    # toggle fullscreen mode
                    if fullscreen:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height), pygame.FULLSCREEN)
                    # toggle windowed mode
                    else:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height))
                # check if the user pressed the 'c' key to toggle the color picker
                elif event.key == pygame.K_c:
                    color_picker_active = not color_picker_active
                # check if the user pressed the 'esc' key to go back to the main menu
                elif event.key == pygame.K_ESCAPE:
                    # go back to the main menu 
                    running = False
                    
            if color_picker_active and event.type == pygame.MOUSEBUTTONDOWN:
                for color_name, color, button in color_buttons:
                    if button.collidepoint(event.pos):
                        background_color = color
                        color_picker_active = False
                        
        # clear the screen 
        main.screen.fill(main.white)
        
        # draw the settings screen
        pygame.draw.rect(main.screen, background_color, (0, 0, main.screen_width, main.screen_height))
        settings_text = main.font.render("Settings", True, main.white)
        fullscreen_text = main.font.render("toggle fullscreen (press 'F')", True, main.white)
        color_text = main.font.render("change color (press 'C')", True, main.white)
        back_text = main.font.render("back to menu (press 'esc')", True, main.white)
        # draw the text
        main.screen.blit(settings_text, (10, 10))
        main.screen.blit(fullscreen_text, (10, 60))
        main.screen.blit(color_text, (10, 110))
        main.screen.blit(back_text, (10, 160))
        
        if color_picker_active:
            # draw color picker buttons
            for color_name, _, button in color_buttons:
                # draw the button
                pygame.draw.rect(screen, colors[color_name], button)
                # draw the color name text
                color_name_text = main.font.render(color_name, True, (0, 0, 0))
                # draw the color name text inside of the button
                main.screen.blit(color_name_text, (button.x + 5, button.y + 5))

        # update the display
        pygame.display.flip()
