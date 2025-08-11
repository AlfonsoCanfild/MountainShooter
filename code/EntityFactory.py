from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH, MARGIN
from code.Explosion import Explosion
from code.Player import Player
from code.Enemy import Enemy
from code.Boss import Boss
import pygame
import random


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':  # LEVEL 1
                list_bg = []
                for layer in range(4):
                    img = pygame.image.load(f'./assets/Level1BG{layer}.png').convert_alpha()
                    image_width = img.get_width()
                    for i in range(2):  # duas cópias do fundo
                        x = i * image_width
                        list_bg.append(Background(f'Level1BG{layer}', (x, 0)))
                return list_bg

            case 'Level2BG':  # LEVEL 2
                list_bg = []
                for layer in range(4):
                    img = pygame.image.load(f'./assets/Level2BG{layer}.png').convert_alpha()
                    image_width = img.get_width()
                    for i in range(2):  # duas cópias do fundo
                        x = i * image_width
                        list_bg.append(Background(f'Level2BG{layer}', (x, 0)))
                return list_bg

            case 'Level3BG':  # LEVEL 3
                list_bg = []
                for layer in range(3):
                    img = pygame.image.load(f'./assets/Level3BG{layer}.png').convert_alpha()
                    image_width = img.get_width()
                    for i in range(2):  # duas cópias do fundo
                        x = i * image_width
                        list_bg.append(Background(f'Level3BG{layer}', (x, 0)))
                return list_bg

            case 'Ship_Player1':
                return [Player('Ship_Player1', (MARGIN, 90))]

            case 'Ship_Player2':
                return [Player('Ship_Player2', (MARGIN, 160))]

            case 'Ship_Enemy1':
                # Cria uma instância temporária só pra pegar a altura da imagem
                temp_enemy = Enemy('Ship_Enemy1', (0, 0))
                enemy_height = temp_enemy.rect.height
                y = random.randint(MARGIN, WIN_HEIGHT - enemy_height - MARGIN)
                return [Enemy('Ship_Enemy1', (WIN_WIDTH, y))]

            case 'Ship_Enemy2':
                # Cria uma instância temporária só pra pegar a altura da imagem
                temp_enemy = Enemy('Ship_Enemy2', (0, 0))
                enemy_height = temp_enemy.rect.height
                y = random.randint(MARGIN, WIN_HEIGHT - enemy_height - MARGIN)
                return [Enemy('Ship_Enemy2', (WIN_WIDTH, y))]

            case 'Ship_EnemyBoss':  # Inimigo especial da fase 3, o Boss final
                return [Boss()]

    @staticmethod
    def get_explosion(position: tuple):
        frames = []
        for i in range(1, 6):
            frame = pygame.image.load(f'./assets/explosion/explosion{i}.png').convert_alpha()
            frames.append(frame)
        return Explosion(position, frames)
