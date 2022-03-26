import pygame

class Sliders (pygame.sprite.Group):
    def __init__(self, window):
        pygame.sprite.Group.__init__(self)

        self.window = window

    def update(self):
        self.draw(self.window)
        super().update()
