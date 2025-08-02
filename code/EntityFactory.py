import random

import pygame

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for layer in range(4):
                    img = pygame.image.load(f'./assets/Level1BG{layer}.png').convert_alpha()
                    image_width = img.get_width()
                    for i in range(2):  # duas cópias do fundo
                        x = i * image_width
                        list_bg.append(Background(f'Level1BG{layer}', (x, 0)))
                return list_bg
            case 'Ship_Player1':
                return [Player('Ship_Player1', (20, 90))]
            case 'Ship_Player2':
                return [Player('Ship_Player2', (20, 160))]
            case 'Ship_Enemy1':
                return [Enemy('Ship_Enemy1', (WIN_WIDTH, random.randint(0, WIN_HEIGHT)))]
            case 'Ship_Enemy2':
                return [Enemy('Ship_Enemy2', (WIN_WIDTH, random.randint(0, WIN_HEIGHT)))]

