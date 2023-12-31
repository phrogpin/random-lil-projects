import pygame
import sys
import main
import settings
import how_to_play
from settings import settings_screen
from how_to_play import how_to_play_screen

# game loop 
running = True
game_active = False
settings_active = False
how_to_play_active = False

# main loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main.start_button.collidepoint(event.pos):
                # start the game button 
                print("start button pressed")
                game_active = True
            elif main.settings_button.collidepoint(event.pos):
                # settings button clicked
                print("settings button clicked")
                settings_active = True
            elif main.how_to_play_button.collidepoint(event.pos):
                # how to play button clicked 
                print("how to play button clicked")
                how_to_play_active = True
            elif main.exit_button.collidepoint(event.pos):
                # exit button clicked 
                print("exit button clicked")
                pygame.quit()
                sys.exit()
            
    # fill the screen with a color            
    main.screen.fill(main.background_color)        
            
    if game_active:
        # game logic here
        pass
    
    elif settings_active:
        # draw the settings button frame here
        for frame in main.button_frames:
            pygame.draw.rect(main.screen, main.black, frame, 9)
        
        # draw the settings screen here    
        settings_screen(main.screen, main.screen_width, main.screen_height, main.background_color)
        settings_active = False # exits settings screen and returns to main menu
    
    elif how_to_play_active:
        # draw the how to play button frame here
        for frame in main.button_frames:
            pygame.draw.rect(main.screen, main.black, frame, 9)
        
        # draw the how to play screen here
        how_to_play_screen(main.screen, main.screen_width, main.screen_height, main.background_color)
        how_to_play_active = False # exits how to play screen and returns to main menu
    
    else:        
        # main menu logic here
        
        # draw the button frames
        for frame in main.button_frames:
            pygame.draw.rect(main.screen, main.black, frame, 9)
            
        # display the buttons 
        pygame.draw.rect(main.screen, main.green, main.start_button)
        pygame.draw.rect(main.screen, main.blue, main.settings_button)
        pygame.draw.rect(main.screen, main.purple, main.how_to_play_button)
        pygame.draw.rect(main.screen, main.red, main.exit_button)
        
        # render button text
        start_text = main.font.render("Start", True, main.white)
        settings_text = main.font.render("Settings", True, main.white)
        how_to_play_text = main.font.render("How to Play", True, main.white)
        exit_text = main.font.render("Exit", True, main.white)
        
        # display button text inside of the buttons 
        main.screen.blit(start_text, (main.start_button.centerx - start_text.get_width() // 2, main.start_button.centery - start_text.get_height() // 2))
        main.screen.blit(settings_text, (main.settings_button.centerx - settings_text.get_width() // 2, main.settings_button.centery - settings_text.get_height() // 2))
        main.screen.blit(how_to_play_text, (main.how_to_play_button.centerx - how_to_play_text.get_width() // 2, main.how_to_play_button.centery - how_to_play_text.get_height() // 2))
        main.screen.blit(exit_text, (main.exit_button.centerx - exit_text.get_width() // 2, main.exit_button.centery - exit_text.get_height() // 2))
    
    # update the display
    pygame.display.flip()

    # limit the frame rate to 60 fps 
    main.clock.tick(60)

pygame.quit()
sys.quit()
