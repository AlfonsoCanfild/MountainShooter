import pygame
from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, TIMEOUT_SCREEN
from code.Score import Score
from code.GameState import GameState, GameStateType
from code.Logger import Logger


# Classe principal que gerencia o fluxo do jogo
class Game:

    def __init__(self):
        self.logger = Logger()
        self.logger.info("Inicializando a classe Game...")  # log
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Sky Fighters")  # Texto da borda da tela do jogo
        self.score = Score(self.window)
        self.state = GameState()
        self.logger.info("Classe Game inicializada com sucesso...")  # log

    # Exibe uma tela de transição entre fases
    def show_transition(self, image_file, delay=TIMEOUT_SCREEN):
        self.logger.info(f"Exibindo tela de transição: {image_file}")  # log
        self.state.change_state(GameStateType.TRANSITION,
                                transition_image=image_file,
                                transition_delay=delay)

        background = pygame.image.load(image_file).convert()
        background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
        self.window.blit(background, (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)
        self.logger.debug("Tela de transição concluída")  # log

    # Executa um nível específico do jogo
    def run_level(self, level_name, menu_return, player_score):
        self.logger.info(f"Iniciando nível: {level_name} com modo: {menu_return}")
        self.state.change_state(GameStateType.PLAYING,
                                level_name=level_name,
                                game_mode=menu_return,
                                player_score=player_score)

        level = Level(self.window, level_name, menu_return, player_score)
        result = level.run(player_score)

        self.logger.info(f"Nível {level_name} finalizado com resultado: {result}")  # log

        if result == "game_over":
            self.state.change_state(GameStateType.GAME_OVER)
            self.logger.info("Jogador foi derrotado")  # log
        elif result == "victory":
            self.state.change_state(GameStateType.VICTORY)
            self.logger.info("Jogador venceu o nível")  # log

        return result

    # Gerencia o fluxo do jogo com base no modo selecionado
    def handle_game_mode(self, menu_return):
        self.logger.info(f"Gerenciando modo de jogo: {menu_return}")  # log

        # Reinicia o estado do jogo para uma nova partida
        self.state.reset_game()
        self.state.game_mode = menu_return
        player_score = self.state.player_score

        # Nível 1
        self.logger.info("Iniciando Level1")  # log
        level_return = self.run_level('Level1', menu_return, player_score)

        # Nível 2 (se passou do nível 1)
        if level_return is True:
            self.logger.info("Level 1 concluído com sucesso")  # log
            self.show_transition("assets/tela_2_fase.png")
            level_return = self.run_level('Level2', menu_return, player_score)

            # Nível 3/Boss (se passou do nível 2)
            if level_return is True:
                self.logger.info(
                    "Level 2 concluído com sucesso - Boss")  # log
                self.show_transition("assets/tela_3_fase.png")
                level_return = self.run_level('Level3', menu_return, player_score)

                if level_return == "victory":
                    self.logger.info("Level 3 concluído - Boss derrotado - vitória")  # log
                    self.show_transition("assets/tela_vitoria.png", delay=TIMEOUT_SCREEN)
                    self.score.save(menu_return, player_score)
                elif level_return == "game_over":
                    self.logger.info("Derrota no Level 3, Player derrotado")  # log
                    self.show_transition("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)
            elif level_return == "game_over":
                self.logger.info("Derrota no Level 2, jogo finalizado")  # log
                self.show_transition("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)
        elif level_return == "game_over":
            self.logger.info("Derrota no Level 1, jogo finalizado")  # log
            self.show_transition("assets/tela_gameOver.png", delay=TIMEOUT_SCREEN)

    #  Loop principal do jogo
    def run(self):
        self.logger.info("Iniciando o loop principal do jogo")  # log
        while True:
            # Estado inicial, menu completo
            self.logger.debug("Exibindo menu principal na tela")  # log
            self.state.change_state(GameStateType.MENU)
            menu = Menu()
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Modos de jogo
                self.logger.info(f"Jogador selecionou o modo: {menu_return}")  # log
                self.handle_game_mode(menu_return)
            elif menu_return == MENU_OPTION[3]:  # Score do jogo
                self.logger.info("Consultar o score do jogo")  # log
                self.state.change_state(GameStateType.SCORE)
                self.score.show()
            elif menu_return == MENU_OPTION[4]:  # sair
                self.logger.info("Saindo do jogo")  # log
                self.state.change_state(GameStateType.QUIT)
                pygame.quit()
                quit()
