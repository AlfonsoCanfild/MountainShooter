import pygame.display

from code.Const import LEVEL_SOUND
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
        pygame.mixer.music.stop()  # para a música do menu
        # CARREGA a nova música da fase
        pygame.mixer.music.load(LEVEL_SOUND)  # troque pelo nome da sua música
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 para repetir

        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            for bg in self.entity_list:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

                # Desenha a segunda cópia da imagem, lado a lado
                second_rect = bg.rect.copy()
                second_rect.x += bg.image_width
                self.window.blit(bg.surf, second_rect)

            pygame.display.update()
            clock.tick(60)

