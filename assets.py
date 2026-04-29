import pygame
from button import TextButton
from trackers import potatoes
pygame.font.init()

# Screen Positions
SCREEN = pygame.display.set_mode((1000, 500))
screen_height = SCREEN.get_height()
screen_width = SCREEN.get_width()
button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .1
center_x = (SCREEN.get_width() / 2) - (button_width / 2)
center_y = (SCREEN.get_height() / 2) - (button_height / 2)

def get_font(size=30):
    font = pygame.font.Font('./assets/ARCADECLASSIC.TTF', size)
    return font

def clear_screen():
    SCREEN.fill((5, 5, 5))

def get_tracker(resource):
    tracker = get_font().render((resource.name + ": " + str(resource.get_amount())), True, (255, 255, 255))
    SCREEN.blit(tracker, (5, 5))

# Resource Buttons
potato_button = TextButton(SCREEN, (150,150,150), center_x, center_y - 50, button_height, button_width, 5, 10, "POTATO")

# Resource Trackers
# potato_tracker = get_font().render(("POTATOES: " + str(potatoes.get_res())), True, (255, 255, 255))

# Main Menu
main_menu_title = get_font().render("Title!", True, (255, 255, 255))
start_button = TextButton(SCREEN, (2,150,2), center_x, center_y - 50, button_height, button_width, 5, 10, "PLAY")
exit_button = TextButton(SCREEN, (150,2,2), center_x, center_y, button_height, button_width, 5, 10, "EXIT")

