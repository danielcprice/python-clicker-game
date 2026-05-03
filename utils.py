import pygame
from simple_gui.gui import SCREEN, update_scale

def initialize():
    update_scale()

def clear_screen():
    pass

pygame.display.set_caption("Ant Colony!")
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
        self.dt = 0
        self.run_clock = False
        GameClock.clock_list.append(self)

    def start_clock(self):
        self.run_clock = True
        self.start_ticks = pygame.time.get_ticks() - self.stop_ticks

    def stop_clock(self):
        self.run_clock = False
        self.stop_ticks = self.get_ticks()

    def pause_time(self):
        pass

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
    
    def tick(self, fps=60):
        if self.run_clock:
            self.dt = self.clock.tick(fps)
        else:
            self.clock.tick(fps)
            self.dt = 0
        return self.dt

time = GameClock()