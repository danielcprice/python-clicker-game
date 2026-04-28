import pygame
from button import Button, TextButton

SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My Game")


button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .1
button_x = (SCREEN.get_width() / 2) - (button_width / 2)
button_y = (SCREEN.get_height() / 2) - (button_height / 2)
start_button = TextButton(SCREEN, (2,150,2), button_x, button_y - 50, button_height, button_width, 0, 10, "PLAY")
exit_button = TextButton(SCREEN, (150,2,2), button_x, button_y, button_height, button_width, 0, 10, "EXIT")

def game_exit():
    pass

def draw_menu(running):
    pass

def play_game():
    running = True
    SCREEN.fill((202, 228, 241))

def main():
    running = True
    state = 'MENU'    
    while running:
        if state == 'MENU':
            SCREEN.fill((5, 5, 5))
            if start_button.draw():
                print("Started")
                return 'GAME'
            if exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return running
            
            pygame.display.update()
        
        elif state == 'GAME':
            play_game()
            
        # case 'play':
        #     run = True
        #     while run:
        #         SCREEN.fill((202, 228, 241))
        #         if start_button.draw():
        #             print("Started")
        #         if exit_button.draw():
        #             print("Exited")
        #             run = False

        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 run = False

        #         pygame.display.update()
main()