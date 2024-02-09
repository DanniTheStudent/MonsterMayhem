import pygame


class Bar():
    def __init__(self, width : int, height : int, x : int, y : int, color : tuple):
        self.width = width * 2
        self.max = self.width
        self.height = height
        self.x = x - ((self.width + 10) / 2)
        self.y = y - ((self.height + 10) / 2)
        self.color = color

    def update(self, data_tracked : int):
        self.width = data_tracked * 2

    def draw(self, screen : pygame.surface.SurfaceType):
        pygame.draw.rect(screen, (100, 100, 100), ((self.x - 5, self.y - 5), (self.max + 10, self.height + 10)))
        pygame.draw.rect(screen, self.color, ((self.x, self.y), (self.width, self.height)))
