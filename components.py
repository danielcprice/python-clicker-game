import pygame
from data import Population, sugar, dew, larvae, queen, maintain_all
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
sugar_button = TextButton(SCREEN, (150,150,150), center_x, center_y - (screen_height * .15), button_height, button_width, 5, 10, "COLLECT SUGAR")
dew_button = TextButton(SCREEN, (150,150,150), center_x, center_y, button_height, button_width, 5, 10, "COLLECT DEW")
excavate_button = TextButton(SCREEN, (150,150,150), center_x, center_y + (screen_height * .15), button_height, button_width, 5, 10, "EXCAVATE")
exit_button = TextButton(SCREEN, (150,2,2), screen_width - 150, screen_height - 100, 50, 100, 5, 10, "EXIT")

# Resource Trackers

# Main Menu
main_menu_title = get_font(60).render("Ant Colony!", True, (255, 255, 255))
main_start_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .2), button_height, button_width, 5, 10, "PLAY")
main_test_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .08), button_height, button_width, 5, 10, "TEST")
main_exit_button = TextButton(SCREEN, (150,2,2), center_x, center_y + (screen_height * .1), button_height, button_width, 5, 10, "EXIT")


# Win/Loss Screens
you_lose_message = get_font(60).render("The Wasteland wasted you!", True, (255, 255, 255))

# Render Components

def clear_screen():
    SCREEN.fill((5, 5, 5))

# This should probably be moved to trackers.py under the Resource class
def render_tracker(resource, x, y):
    tracker = get_font().render((resource.name + " " + str(resource.get_amount())), True, (255, 255, 255))
    SCREEN.blit(tracker, (x, y))

def render_capacity(x, y):
    population_tracker = get_font().render(("Population " + str(Population.total_population)), True, (255, 255, 255))
    capacity_tracker = get_font().render(("Capacity " + str(Population.capacity)), True, (255, 255, 255))
    SCREEN.blit(population_tracker, (x, y))
    SCREEN.blit(capacity_tracker, (x, (y + 40)))

def render_resources():
    # if resources then for resources get tracker
    render_tracker(sugar, 5, 5)
    render_tracker(dew, 5, 45)
    render_tracker(queen, 5, 85)
    render_tracker(larvae, 5, 125)
    render_capacity(5, 165)

def render_products():
    # if products then for products get tracker
    pass

def render_population():
    pass

def render_game_buttons():
    # make a button group class for managing groups of buttons
    # then they can sorted and be pulled in easily
    # if buttons get buttons
    if sugar_button.draw():
        sugar.add_res()
    if dew_button.draw():
        dew.add_res()
    if excavate_button.draw():
        Population.increase_cap()


# Screens

def play_game():
    running = True
    dt = time.tick()
    SCREEN.fill((202, 228, 241))
    while running:
        SCREEN.fill((30, 26, 21))
        time.clock.tick(30)
        SCREEN.fill((5, 5, 5))
        # SCREEN.blit(assets.potato_tracker, (5, 5))
        render_resources()
        render_game_buttons()
        if exit_button.draw():
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
        maintain_all(dt)
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