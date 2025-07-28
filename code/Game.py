import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        # Define o tamanho da janela como variável
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.window = pygame.display.set_mode(self.window_size)

        pygame.display.set_caption("Mountain Shooter - by Alfonso")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True

        while running:
            # Executa o menu passando a janela
            menu = Menu(self.window)
            menu.run()

            # Verifica se o usuário clicou para fechar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(60)

        pygame.quit()
