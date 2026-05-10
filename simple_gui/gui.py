import pygame

pygame.font.init()

def get_font(size=30):
    font = pygame.font.Font('./assets/pixeloid.sans-bold.ttf', size)
    return font

SCREEN = pygame.display.set_mode((1500, 750))
current_screen_mode='Windowed'
screen_scale = {'screen_height': SCREEN.get_height(), 'screen_width': SCREEN.get_width(), 'button_height': (SCREEN.get_height() * .1), 'button_width': (SCREEN.get_width() * .15), 'center_x': ((SCREEN.get_width() / 2) - ((SCREEN.get_width() * .15) / 2)), 'center_y': ((SCREEN.get_height() / 2) - ((SCREEN.get_height() * .1) / 2))}

button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .15

def update_scale():
    for property in screen_scale:
        property = screen_scale[property]
    return screen_scale

def change_screen(width=1500, height=750, mode='windowed'):
    if mode == 'fullscreen':
        SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        current_screen_mode='Fullscreen'
        return SCREEN, current_screen_mode
    else:
        SCREEN = pygame.display.set_mode((width, height))
        current_screen_mode='Windowed'
        return SCREEN, current_screen_mode
    


class NavBar():
    def __init__(self, items, position):
        pass

class Popup():
    def __init__(self, label, close_button=True):
        pass

class TabMenu():
    pass

class GridMenu():
    pass