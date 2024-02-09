import pygame
import os
import numpy as np


# Daniel K. - Button template
class Button(pygame.sprite.Sprite):
    def __init__(self, name : str, coordinates : tuple, sprite_width : int, sprite_height : int) -> None:
        super().__init__()
        self.name = name
        self.state = False

        self.image = pygame.surface.Surface((sprite_width, sprite_height))
        self.states = []
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

    def get_animations_png(self) -> None:
        for frame in os.listdir(f"sprites/{self.name}"):
            frame = pygame.image.load(f"sprites/{self.name}/{frame}").convert_alpha()
            self.states.append(frame)

    def draw(self, screen : pygame.surface.SurfaceType) -> None:
        screen.blit(self.image, self.rect)

    def check_for_cursor(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        if self.check_for_cursor():
            self.image = self.states[1]
        elif self.state is True:
            self.image = self.states[-1]
        else:
            self.image = self.states[0]
