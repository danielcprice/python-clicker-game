import pygame, game, assets
from sys import exit

SCREEN = assets.SCREEN
pygame.display.set_caption("TITLE!")

def main():
    SCREEN.fill((5, 5, 5))
    running = True
    state = 'MENU'    
    while running:
        if state == 'MENU':
            SCREEN.blit(assets.main_menu_title, (assets.center_x - 20, assets.center_y - 160))
            if assets.main_start_button.draw():
                state = 'GAME'
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
            game.play_game()
            state = 'MENU'
            
main()