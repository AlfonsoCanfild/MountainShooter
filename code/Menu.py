import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.background_scale = self.window.get_size()  # pega o tamanho da janela principal

        # scale the background
        self.background = pygame.transform.scale(
            pygame.image.load("assets/tela_inicial_com_titulo.png"), self.background_scale
        ).convert()

    def run(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()
