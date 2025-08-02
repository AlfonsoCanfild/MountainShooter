import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Background import Background
from code.Const import LEVEL_SOUND, COLOR_WHITE, WIN_HEIGHT, FONT_TYPE, MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.extend(EntityFactory.get_entity('Ship_Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.extend(EntityFactory.get_entity('Ship_Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 3000)

    def run(self):
        pygame.mixer.music.stop()  # para a música do menu
        # CARREGA a nova música da fase
        pygame.mixer.music.load(LEVEL_SOUND)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 para repetir

        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            # Desenha só os backgrounds com duplicação para paralaxe
            for bg in self.entity_list:
                if isinstance(bg, Background):
                    bg.move()
                    self.window.blit(bg.surf, bg.rect)

                    second_rect = bg.rect.copy()
                    second_rect.x += bg.image_width
                    self.window.blit(bg.surf, second_rect)

            # Agora desenha as outras entidades (ex: jogador)
            for ent in self.entity_list:
                if not isinstance(ent, Background):
                    ent.move()
                    self.window.blit(ent.surf, ent.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Ship_Enemy1', 'Ship_Enemy1', 'Ship_Enemy2'))
                    self.entity_list.extend(EntityFactory.get_entity(choice))

            # printando o texto na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                            COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list) - 8}', COLOR_WHITE, (10,
                                                                                     WIN_HEIGHT -
                                                                                     20))

            pygame.display.update()
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name=FONT_TYPE, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)