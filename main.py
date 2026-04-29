import pygame, game, assets

SCREEN = assets.SCREEN
pygame.display.set_caption("My Game")

def game_exit():
    pass

def draw_menu(running):
    pass

def main():
    SCREEN.fill((5, 5, 5))
    running = True
    state = 'MENU'    
    while running:
        if state == 'MENU':
            SCREEN.blit(assets.main_menu_title, (5, 5))
            if assets.start_button.draw():
                state = 'GAME'
            if assets.exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return running
            pygame.display.update()
        
        elif state == 'GAME':
            game.start_game()
            state = 'MENU'
            
main()