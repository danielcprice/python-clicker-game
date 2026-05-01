import pygame, assets
from utils import SCREEN, GameClock
from trackers import maintain_trends, maintain_all, potatoes, population
time = GameClock()

# Format for screens should be:
# Screen Fill
# Graphics
# buttons - create button groups

def play_game():
    running = True
    for clocks in GameClock.clock_list:
        clocks.start_clock()
    SCREEN.fill((202, 228, 241))
    while running:
        time.clock.tick(30)
        SCREEN.fill((5, 5, 5))
        # SCREEN.blit(assets.potato_tracker, (5, 5))
        assets.render_resources()
        assets.render_game_buttons()
        if assets.main_exit_button.draw():
            # Exit should eventually clear the game stats and save to file
            for clocks in GameClock.clock_list:
                clocks.stop_clock()
            running = False
            assets.clear_screen()
            return running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        maintain_all()
        pygame.display.update()

def test_game():
    running = True
    for clocks in GameClock.clock_list:
        clocks.start_clock()
    SCREEN.fill((202, 228, 241))
    while running:
        maintain_trends()
        time.clock.tick(30)
        SCREEN.fill((5, 5, 5))
        SCREEN.blit(assets.test_screen_message, (assets.center_x + 20, assets.screen_height - (assets.screen_height - 40)))
        assets.get_tracker(potatoes, (assets.center_x - 200), (assets.center_y - 100))
        assets.get_tracker(population, (assets.center_x + 200), (assets.center_y - 100))
        if assets.test_potato_button.draw():
            potatoes.add_res()
        if assets.test_population_button.draw():
            population.add_res()
            potatoes.remove_res()
        if assets.test_exit_button.draw():
            # Exit should eventually clear the game stats and save to file
            for clocks in GameClock.clock_list:
                clocks.stop_clock()
            running = False
            assets.clear_screen()
            return running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def research_screen():
    pass

def info_screen():
    pass

def escape_menu():
    pass

def lose_screen():
    SCREEN.fill((30, 26, 21))
    running = True
    state = 'MENU'    
    while running:
            SCREEN.blit(assets.you_lose_message, (assets.center_x, assets.center_y - 200))
            if assets.main_exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()