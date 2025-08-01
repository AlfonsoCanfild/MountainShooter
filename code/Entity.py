from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.image_width = self.surf.get_width()
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

