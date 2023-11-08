import pygame 
import sys
import main

def how_to_play_screen(screen, screenwidth, screen_height, background_color):
    
    # define button texts
    button1_text = "Button 1 Button 1 Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1"
    button2_text = "Button 2Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1"
    button3_text = "Button 3Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1Button 1"
    
    # define button positions
    button_positions = []
    for i in range (3):
        x = (screenwidth - (main.button_width * 3 + main.button_padding * 2)) / 2 + (main.button_width + main.button_padding) * i
        y = 10
        button_positions.append((x, y))
    
    # define button labels and text
    button_labels = ["Button 1", "Button 2", "Button 3"]
    button_texts = [button1_text, button2_text, button3_text]
    current_text = button_texts[0]
    
    # create buttons
    buttons = []
    # create button rects 
    for i in range (3):
        button_rect = pygame.Rect(button_positions[i][0], button_positions[i][1], main.button_width, main.button_height)
        button = pygame.draw.rect(main.screen, main.button_color, button_rect)
        buttons.append(button)
        label = main.button_font.render(button_labels[i], True, main.button_text_color)
        label_rect = label.get_rect(center=button.center)
        main.screen.blit(label, label_rect)
        
    # create text
    text = main.font.render(current_text, True, main.text_color)
    text_rect = text.get_rect(center=(screenwidth/2, screen_height/2))
    main.screen.blit(text, text_rect)
    
    # main how to play loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                # check if the user pressed the 'esc' key to go back to the main menu
                if event.key == pygame.K_ESCAPE:
                    # go back to the main menu 
                    return
                # check if the user pressed the 'f' key to toggle fullscreen
                elif event.key == pygame.K_f:
                    main.fullscreen = not main.fullscreen
                    # toggle fullscreen mode
                    if main.fullscreen:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height), pygame.FULLSCREEN)
                    # toggle windowed mode
                    else:
                        main.screen = pygame.display.set_mode((main.screen_width, main.screen_height))
            
            # check for mouse button presses
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range (3):
                    if buttons[i].collidepoint(event.pos):
                        # clear the screen
                        main.screen.fill((0, 0, 0))
                        # change text
                        current_text = button_texts[i]
                        # create text
                        text = main.font.render(current_text, True, main.text_color)
                        text_rect = text.get_rect(center=(screenwidth/2, screen_height/2))
                        main.screen.blit(text, text_rect)
            
        # highlight button if mouse is over it
        for i in range (3):
            if buttons[i].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(main.screen, main.button_highlight_color, buttons[i])
                label = main.button_font.render(button_labels[i], True, main.button_highlight_text_color)
                label_rect = label.get_rect(center=buttons[i].center)
                main.screen.blit(label, label_rect)
            else:
                pygame.draw.rect(main.screen, main.button_color, buttons[i])
                label = main.button_font.render(button_labels[i], True, main.button_text_color)
                label_rect = label.get_rect(center=buttons[i].center)
                main.screen.blit(label, label_rect)
       
        # update the display 
        pygame.display.update()