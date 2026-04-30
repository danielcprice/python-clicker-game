import pygame, assets
from utils import GameClock, Timer
from sys import exit
from trackers import potatoes, population

SCREEN = assets.SCREEN
time = GameClock()

def maintain_trends():
    for timer in Timer.timer_list:
        timer.check_timer()
    

def render_resources():
    # if resources then for resources get tracker
    assets.get_tracker(potatoes, 5, 5)
    assets.get_tracker(population, 5, 45)

def render_products():
    # if products then for products get tracker
    pass

def render_population():
    pass

def render_game_buttons():
    if assets.potato_button.draw():
         potatoes.add_res()
    if assets.population_button.draw():
         population.add_res()
         potatoes.remove_res()


def play_game():
    running = True
    for clocks in GameClock.clock_list:
        clocks.start_clock()
    SCREEN.fill((202, 228, 241))
    while running:
        maintain_trends()
        time.clock.tick(30)
        SCREEN.fill((5, 5, 5))
        # SCREEN.blit(assets.potato_tracker, (5, 5))
        render_resources()
        render_game_buttons()
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
        pygame.display.update()