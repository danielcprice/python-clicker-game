import pygame
from data import Population, food, larvae, queen, nursery, tunneller, forager, soldier, win_loss_check, maintain_all, time
from simple_gui.gui import SCREEN
from simple_gui.button import TextButton, get_font
from simple_gui.status_bar import StatusBar

# Colors
BROWN = (30, 26, 21)

# Screen Positions
screen_height = SCREEN.get_height()
screen_width = SCREEN.get_width()
button_height = SCREEN.get_height() * .08
button_width = SCREEN.get_width() * .15
center_x = (SCREEN.get_width() / 2) - (button_width / 2)
center_y = (SCREEN.get_height() / 2) - (button_height / 2)

# Game Buttons
food_button = TextButton(SCREEN, (150,150,150), center_x, center_y - (screen_height * .15), button_height, button_width, 5, 10, "GET FOOD")
excavate_button = TextButton(SCREEN, (150,150,150), center_x, center_y + (screen_height * .15), button_height, button_width, 5, 10, "DIG TUNNEL")
play_pause_button = TextButton(SCREEN, (150,2,2), screen_width - 180, screen_height - 170, 50, 150, 5, 10, "|| / |>")
pause_button = TextButton(SCREEN, (150,2,2), screen_width - 150, screen_height - 200, 50, 100, 5, 10, "pause")
exit_button = TextButton(SCREEN, (150,2,2), screen_width - 180, screen_height - 100, 50, 150, 5, 10, "exit")

# Main Menu
main_menu_title = get_font(60).render("Ant Colony!", True, (255, 255, 255))
main_start_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .2), button_height, button_width, 5, 10, "play")
main_test_button = TextButton(SCREEN, (2,150,2), center_x, center_y - (screen_height * .08), button_height, button_width, 5, 10, "test")
main_exit_button = TextButton(SCREEN, (150,2,2), center_x, center_y + (screen_height * .1), button_height, button_width, 5, 10, "exit")

# Status Bars
queen_status_bar = StatusBar(SCREEN, (255,255,150), (2,150,2), 50, 50, 100, 10)
larvae_status_bar = StatusBar(SCREEN, (255,255,150), (2,150,2), 100, 100, 100, 10)

# Win/Loss Screens
you_win_message = get_font(60).render("You win!", True, (255, 255, 255))
you_lose_message = get_font(60).render("You lost the QUEEN!", True, (255, 255, 255))

# Render Components

def clear_screen():
    SCREEN.fill((5, 5, 5))

# This should probably be moved to trackers.py under the Resource class
def render_tracker(resource, x, y):
    tracker = get_font().render((resource.name + " " + str(resource.get_amount())), True, (255, 255, 255))
    SCREEN.blit(tracker, (x, y))

def render_capacity(x, y):
    capacity_tracker = get_font().render(("Capacity " + str(Population.total_population) + " / " + str(Population.capacity)), True, (255, 255, 255))
    SCREEN.blit(capacity_tracker, (x, y))

def render_resources():
    render_tracker(food, 5, 5)
    render_tracker(queen, 5, 85)
    render_tracker(larvae, 5, 125)
    render_tracker(forager, 5, 205)
    render_tracker(nursery, 5, 165)
    render_tracker(soldier, 5, 285)
    render_tracker(tunneller, 5, 245)
    render_capacity(5, 325)

def render_game_graphics():
    if food_button.draw():
        food.add_res()
    if excavate_button.draw():
        Population.increase_cap()
    if play_pause_button.draw():
        if time.run_clock == True:
            time.stop_clock()
        elif time.run_clock == False:
            time.start_clock()
    # Queen Larvae Production
    queen_status_bar.draw(percent = (larvae.amount % 1))
    # Larvae time to convert into other Ant Type
    larvae_status_bar.draw(percent = (larvae.maturation % 1))
    # Tunneller time to dig





# Screens

def play_game():
    running = True
    # time.start_clock()
    # dt = time.tick() / 1000
    while running:
        dt = time.tick(30) / 1000
        maintain_all(dt, time.run_clock)
        SCREEN.fill(BROWN)
        render_resources()
        render_game_graphics()
        if win_loss_check() == 'lose':
            running = lose_screen()
        elif win_loss_check() == 'win':
            running = win_screen()
        if exit_button.draw():
            # Exit should eventually clear the game stats and save to file
            time.stop_clock()
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

def win_screen():
    SCREEN.fill(BROWN)
    running = True
    state = 'MENU'    
    while running:
            SCREEN.blit(you_win_message, (center_x - 100, center_y - 200))
            if main_exit_button.draw():
                print("Exited")
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
    return running

def lose_screen():
    SCREEN.fill(BROWN)
    running = True
    state = 'MENU'    
    while running:
            SCREEN.blit(you_lose_message, (center_x - 200, center_y - 200))
            if main_exit_button.draw():
                print("Exited")
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
    return running