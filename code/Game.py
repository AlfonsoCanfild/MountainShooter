import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, FONT_TYPE, C_WHITE
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def show_phase_text(self, text):
        # Carrega a imagem de fundo
        background = pygame.image.load("assets/tela_2_fase.png").convert()
        background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

        # Desenha a imagem de fundo
        self.window.blit(background, (0, 0))
        pygame.display.update()

        pygame.time.delay(2000)  # Espera  segundo

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu()
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # lista com Player1 e Player2
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                # 2° Fase
                if level_return:
                    self.show_phase_text("2ª Fase")
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:

                pass
