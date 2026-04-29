import pygame, assets
from trackers import potatoes

SCREEN = assets.SCREEN

def start_game():
    running = True
    SCREEN.fill((202, 228, 241))

    while running:
        SCREEN.fill((5, 5, 5))
        # SCREEN.blit(assets.potato_tracker, (5, 5))
        assets.get_tracker(potatoes)
        if assets.potato_button.draw():
             print("POTATO")
             potatoes.add_res()
        if assets.exit_button.draw():
                print("Exited")
                running = False
                assets.clear_screen()
                return running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
        pygame.display.update()