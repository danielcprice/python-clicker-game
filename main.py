from utils import SCREEN, GameClock
import pygame, components
from sys import exit


def main():
    SCREEN.fill((30, 26, 21))
    running = True
    state = 'MENU'    
    while running:
        if state == 'MENU':
            running = True
            for clocks in GameClock.clock_list:
                clocks.start_clock()
            SCREEN.fill((30, 26, 21))
            SCREEN.blit(components.main_menu_title, (components.center_x, components.center_y - 300))
            if components.main_start_button.draw():
                print('GAME')
                state = 'GAME'
            if components.main_test_button.draw():
                print('TEST')
                state = 'TEST'
            if components.main_exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
        elif state == 'GAME':
            components.play_game()
            state = 'MENU'
        elif state == 'TEST':
            components.test_game()
            state = 'MENU'
        pygame.display.update()
main()