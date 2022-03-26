import pygame

class MouseSlider (pygame.sprite.Sprite):
    def __init__(self, window, size, direction, pos, color, minmaxPos):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.direction = direction
        self.color = color
        self.window = window
        self.minmaxPos = minmaxPos

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos)

        self.draw()

    def draw(self):
        self.image.fill(self.color)
        self.window.blit(self.image, self.rect)

    def update(self):
        mousePos = pygame.mouse.get_pos()

        newPos = self.rect
        if (self.direction[0] > 0):
            newPos[0] = mousePos[0]
            newPos[0] = min(max(newPos[0], self.minmaxPos[0]), self.minmaxPos[1])
            newPos[0] -= self.rect.width / 2
        if (self.direction[1] > 0):
            newPos[1] = mousePos[1]
            newPos[1] = min(max(newPos[1], self.minmaxPos[0]), self.minmaxPos[1])

        self.rect = newPos
        self.draw()

class SimpleSlider (pygame.sprite.Sprite):
    def __init__(self, window, size, direction, pos, color, minmaxPos):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.direction = direction
        self.color = color
        self.window = window
        self.minmaxPos = minmaxPos

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos)

        self.draw()

    def draw(self):
        self.image.fill(self.color)
        self.window.blit(self.image, self.rect)

    def update(self):
        self.draw()

    def moveRight(self):
        self.rect = self.rect.move(self.direction)

    def moveLeft(self):
        self.rect = self.rect.move([-self.direction[0], -self.direction[1]])
