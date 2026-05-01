import pygame
pygame.font.init()

def get_font(size=30):
    font = pygame.font.Font('./assets/font.TTF', size)
    return font

class Button():

    def __init__(self, surface, color, x, y, height, width, thickness, border_radius):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.height = self.surface
        self.width = width
        self.thickness = thickness
        self.border_radius = border_radius
        self.clicked = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        action = self.is_clicked()
        pygame.draw.rect(self.surface, self.color, self.rect, self.thickness, self.border_radius)
        return action


    def is_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action

class TextButton(Button):
    
    def __init__(self, surface, color, x, y, height, width, thickness, border_radius, text, font_size=30):
        super().__init__(surface, color, x, y, height, width, thickness, border_radius)
        self.font = get_font(font_size)
        self.text = text
        self.text_surface = self.font.render(text, True, (255, 255, 255),)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self):
        
        action = self.is_clicked()
        pygame.draw.rect(self.surface, self.color, self.rect, self.thickness, self.border_radius)
        self.surface.blit(self.text_surface, self.text_rect)
        return action
    
class IconButton(Button):
    pass