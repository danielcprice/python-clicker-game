# For utilities

import pygame
from simple_gui.gui import SCREEN, update_scale

def initialize():
    update_scale()


screen_height = SCREEN.get_height()
screen_width = SCREEN.get_width()
button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .15
center_x = (SCREEN.get_width() / 2) - (button_width / 2)
center_y = (SCREEN.get_height() / 2) - (button_height / 2)

# Get start date of game and save to file to produce in game date
# Might change "GameClock" to just keep track of pygame timers
# I would set up pygame.time.set_timer and then use maintain_trends() to make changes

class GameClock():
    clock_list = []
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.stop_ticks = pygame.time.get_ticks()
        self.run_clock = False
        GameClock.clock_list.append(self)

    def start_clock(self):
        self.run_clock = True
        self.start_ticks = pygame.time.get_ticks() - self.stop_ticks

    def stop_clock(self):
        self.run_clock = False
        self.stop_ticks = self.get_ticks()

    def get_ticks(self):
        return pygame.time.get_ticks() - self.start_ticks
    
    def get_time(self, unit='ms'):
        if unit=='ms':
            current_time = self.get_ticks()
        if unit == 's':
            current_time = self.get_ticks() / 1000
        if unit == 'min':
            pass

        return current_time
    
class Timer(GameClock):
    timer_list = []
    def __init__(self, name, action, limit: int):
        super().__init__()
        self.name = name
        self.action = action
        self.limit = limit
        Timer.timer_list.append(self)

    def reset_timer(self):
        self.start_ticks = pygame.time.get_ticks()
    
    def check_timer(self):
        if self.get_time() >= self.limit:
            self.reset_timer()
            self.action()

def clear_screen():
    pass