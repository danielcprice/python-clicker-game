import pygame, screens, assets
from simple_gui.gui import SCREEN, change_screen, update_scale
from sys import exit

pygame.display.set_caption("Bunker!")

def main():
    SCREEN.fill((30, 26, 21))
    running = True
    state = 'MENU'    
    while running:
        if state == 'MENU':
            SCREEN.blit(assets.main_menu_title, (assets.center_x, assets.center_y - 300))
            if assets.main_start_button.draw():
                print('GAME')
                state = 'GAME'
            if assets.main_test_button.draw():
                print('TEST')
                state = 'TEST'
            if assets.main_exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
        
        elif state == 'GAME':
            screens.play_game()
            state = 'MENU'
        elif state == 'TEST':
            screens.test_game()
            state = 'MENU'

            
main()