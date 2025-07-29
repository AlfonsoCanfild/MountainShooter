import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_SOUND, MENU_OPTION, COLOR_ORANGE, \
    COLOR_WHITE
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        # Define o tamanho da janela como variável
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.window = pygame.display.set_mode(self.window_size)

        pygame.display.set_caption("Mountain Shooter - by Alfonso")
        self.clock = pygame.time.Clock()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        running = True

        # play the menu sound
        pygame.mixer.music.load(MENU_SOUND)
        pygame.mixer.music.set_volume(0.5)  # volume - 0.0 e 1.0
        pygame.mixer.music.play(-1)  # faz a música repetir

        # Executa o menu, mostra a tela de fundo
        menu = Menu(self.window)
        menu.run()

        while running:
            # Verifica se o usuário clicou para fechar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # executa o texto do menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 380 + 30 * i))

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
