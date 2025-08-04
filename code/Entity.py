from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.image_width = self.surf.get_width()
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass

