import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Background import Background
from code.Const import LEVEL_SOUND, C_WHITE, WIN_HEIGHT, FONT_TYPE, MENU_OPTION, EVENT_ENEMY, \
    C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Explosion import Explosion
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))
        player_list = EntityFactory.get_entity('Ship_Player1')
        player = player_list[0]
        player.score = player_score[0]
        self.entity_list.extend(player_list)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player_list = EntityFactory.get_entity('Ship_Player2')
            player = player_list[0]
            player.score = player_score[1]
            self.entity_list.extend(player_list)
        pygame.time.set_timer(EVENT_ENEMY, 2000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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
            for ent in self.entity_list[:]:  # cópia da lista para poder remover
                if isinstance(ent, Background):
                    continue

                ent.move()  # move tudo que não for background

                if isinstance(ent, Explosion) and ent.finished:
                    self.entity_list.remove(ent)
                    continue

                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)

                # Se saiu da tela pela esquerda, remove da lista
                if ent.rect.right <= 0:
                    self.entity_list.remove(ent)
                    continue

                # Mostrar a vida dos jogadores
                if ent.name == 'Ship_Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}',
                                    C_GREEN, (10, 30))
                if ent.name == 'Ship_Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}',
                                    C_GREEN, (10, 45))

                self.window.blit(ent.surf, ent.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Ship_Enemy1', 'Ship_Enemy1', 'Ship_Enemy2'))
                    self.entity_list.extend(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Ship_Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Ship_Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # printando o texto na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                            C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list) - 8}', C_WHITE, (10,
                                                                                     WIN_HEIGHT -
                                                                                     20))
            # verificar as colisões
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_healthy(entity_list=self.entity_list)

            pygame.display.update()
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name=FONT_TYPE, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
