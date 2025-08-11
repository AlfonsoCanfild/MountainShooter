import pygame
from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, TIMEOUT_SCREEN
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def show_phase_text(self, image_file, delay=TIMEOUT_SCREEN):
        background = pygame.image.load(image_file).convert()
        background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
        self.window.blit(background, (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu()
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0, 0, 0]

                # 1ª fase
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                # 2ª fase
                if level_return is True:
                    self.show_phase_text("assets/tela_2_fase.png")
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    # 3ª fase (Boss)
                    if level_return is True:
                        self.show_phase_text("assets/tela_3_fase.png")
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)

                        if level_return == "victory":
                            self.show_phase_text("assets/tela_vitoria.png", delay=TIMEOUT_SCREEN)
                            score.save(menu_return, player_score)

                        elif level_return == "game_over":
                            self.show_phase_text("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)

                    elif level_return == "game_over":
                        self.show_phase_text("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)

                elif level_return == "game_over":
                    self.show_phase_text("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
