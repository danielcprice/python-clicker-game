import pygame
from data import population, potatoes, maintain_all, maintain_trends
from utils import GameClock, time
from simple_gui.gui import SCREEN
from simple_gui.button import TextButton, get_font

# Screen Positions
screen_height = SCREEN.get_height()
screen_width = SCREEN.get_width()
button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .15
center_x = (SCREEN.get_width() / 2) - (button_width / 2)
center_y = (SCREEN.get_height() / 2) - (button_height / 2)

# Game Buttons
potato_button = TextButton(SCREEN, (150,150,150), center_x, center_y - (screen_height * .1), button_height, button_width, 5, 10, "POTATO")
population_button = TextButton(SCREEN, (150,150,150), center_x, center_y - (screen_height * .2), button_height, button_width, 5, 10, "POPULATION")

# Resource Trackers
# potato_tracker = get_font().render(("POTATOES: " + str(potatoes.get_res())), True, (255, 255, 255))

# Main Menu
main_menu_title = get_font(60).render("Bunker!", True, (255, 255, 255))
main_start_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .2), button_height, button_width, 5, 10, "PLAY")
main_test_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .08), button_height, button_width, 5, 10, "TEST")
main_exit_button = TextButton(SCREEN, (150,2,2), center_x, center_y + (screen_height * .1), button_height, button_width, 5, 10, "EXIT")

# Test Screen
test_screen_message = get_font(20).render("Testing!", True, (255, 255, 255))
test_potato_button = TextButton(SCREEN, (150,150,150), center_x - 220, center_y, button_height, button_width, 5, 10, "POTATO")
test_population_button = TextButton(SCREEN, (150,150,150), center_x + 190, center_y, button_height, button_width, 5, 10, "POPULATION")
test_exit_button = TextButton(SCREEN, (150,2,2), screen_width - 150, screen_height - 100, 50, 100, 5, 10, "EXIT")

# Win/Loss Screens
you_lose_message = get_font(60).render("The Wasteland wasted you!", True, (255, 255, 255))

# Render Components

def clear_screen():
    SCREEN.fill((5, 5, 5))

# This should probably be moved to trackers.py under the Resource class
def get_tracker(resource, x, y):
    tracker = get_font().render((resource.name + " " + str(resource.get_amount())), True, (255, 255, 255))
    SCREEN.blit(tracker, (x, y))

def render_resources():
    # if resources then for resources get tracker
    get_tracker(potatoes, 5, 5)
    get_tracker(population, 5, 45)

def render_products():
    # if products then for products get tracker
    pass

def render_population():
    pass

def render_game_buttons():
    # make a button group class for managing groups of buttons
    # then they can sorted and be pulled in easily
    # if buttons get buttons
    if potato_button.draw():
         potatoes.add_res()
    if population_button.draw():
         population.add_res()
         potatoes.remove_res()


# Screens

def play_game():
    running = True
    for clocks in GameClock.clock_list:
        clocks.start_clock()
    SCREEN.fill((202, 228, 241))
    while running:
        SCREEN.fill((30, 26, 21))
        time.clock.tick(30)
        SCREEN.fill((5, 5, 5))
        # SCREEN.blit(assets.potato_tracker, (5, 5))
        render_resources()
        render_game_buttons()
        if main_exit_button.draw():
            # Exit should eventually clear the game stats and save to file
            for clocks in GameClock.clock_list:
                clocks.stop_clock()
            running = False
            clear_screen()
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
        SCREEN.blit(test_screen_message, (center_x + 20, screen_height - (screen_height - 40)))
        get_tracker(potatoes, (center_x - 200), (center_y - 100))
        get_tracker(population, (center_x + 200), (center_y - 100))
        if test_potato_button.draw():
            potatoes.add_res()
        if test_population_button.draw():
            population.add_res()
            potatoes.remove_res()
        if test_exit_button.draw():
            # Exit should eventually clear the game stats and save to file
            for clocks in GameClock.clock_list:
                clocks.stop_clock()
            running = False
            clear_screen()
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
            SCREEN.blit(you_lose_message, (center_x, center_y - 200))
            if main_exit_button.draw():
                print("Exited")
                running = False
                return running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()