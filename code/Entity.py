from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.image_width = self.surf.get_width()
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):
        pass

