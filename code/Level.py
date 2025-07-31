import pygame.display

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            for bg in self.entity_list:
                bg.move()

            # reposiciona fundos que saíram da tela, colando depois do último fundo
            for bg in self.entity_list:
                if bg.rect.right <= 0:
                    rightmost = max(self.entity_list, key=lambda b: b.rect.right)
                    bg.rect.left = rightmost.rect.right

            for bg in self.entity_list:
                self.window.blit(bg.surf, bg.rect)

            pygame.display.update()
            clock.tick(60)

