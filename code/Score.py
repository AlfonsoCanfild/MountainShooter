import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_SOUND, FONT_TYPE, C_ORANGE, SCORE_POS, \
    MENU_OPTION, C_WHITE
from code.DBProxy import DBProxy
from code.Logger import Logger


class Score:

    def __init__(self, window):
        self.logger = Logger()
        self.logger.info("Inicializando sistema de pontuação")
        
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Mountain Shooter - by Alfonso")
        self.clock = pygame.time.Clock()

        self.background = pygame.transform.scale(
            pygame.image.load("assets/tela_inicial_sem_titulo.png"),
            self.window_size
        )
        
        self.logger.debug("Sistema de pontuação inicializado com sucesso")

    def save(self, game_mode: str, player_score: list[int]):
        self.logger.info(f"Salvando pontuação: modo={game_mode}, pontuação={player_score}")
        pygame.mixer.music.load(MENU_SOUND)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(self.background, (0, 0))  # ← limpa a tela
            self.score_text(45, 'YOU WIN!!!!', C_ORANGE, SCORE_POS['Title'])

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter your name (4 chars):'
            elif game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 chars):'
            elif game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter your name (4 chars):'
                else:
                    score = player_score[1]
                    text = 'Enter your name (4 chars):'

            self.score_text(25, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(32, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            self.clock.tick(60)

    def show(self):
        self.logger.info("Exibindo tela de pontuações")
        pygame.mixer.music.load(MENU_SOUND)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.window.blit(self.background, (0, 0))
        self.score_text(32, '*** Top 10 Score ***', C_ORANGE, SCORE_POS['Title'])

        # Cabeçalho fixo com alinhamento por espaçamento
        self.score_text(20, f"{' NAME':<10} {' SCORE':<8} {'  DATE':<10}", C_WHITE, SCORE_POS[
            'Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            line = f"{name:<10} {int(score):05d}   {date}"
            self.score_text(20, line, C_WHITE, SCORE_POS[i])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
            pygame.display.flip()
            self.clock.tick(60)

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name=FONT_TYPE, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    return datetime.now().strftime("%d/%m/%y")
