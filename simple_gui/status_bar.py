import pygame

class StatusBar():
    def __init__(self, surface, back_color, front_color, x, y, width, height):
        self.surface = surface
        self.back_color = back_color
        self.front_color = front_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.outer_bar = pygame.Rect(x, y, width, height)

    def draw(self, percent):
        self.inner_bar = pygame.Rect((self.x + 1), (self.y + 1), ((self.width - 2) * percent), (self.height - 2))
        pygame.draw.rect(self.surface, self.back_color, self.outer_bar)
        pygame.draw.rect(self.surface, self.front_color, self.inner_bar)