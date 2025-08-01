import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_SOUND, MENU_OPTION, \
    COLOR_WHITE, COLOR_CYAN


class Menu:
    def __init__(self):
        pygame.init()

        # Define o tamanho da janela como variável
        self.window_size = (WIN_WIDTH, WIN_HEIGHT)
        self.window = pygame.display.set_mode(self.window_size)

        pygame.display.set_caption("Mountain Shooter - by Alfonso")
        self.clock = pygame.time.Clock()

        self.background = pygame.transform.scale(
            pygame.image.load("assets/tela_inicial_com_titulo.png"),
            self.window_size
        )

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_option = 0

        # play the menu sound
        pygame.mixer.music.load(MENU_SOUND)
        pygame.mixer.music.set_volume(0.5)  # volume - 0.0 e 1.0
        pygame.mixer.music.play(-1)  # faz a música repetir

        while True:
            # Verifica os eventos do usuário, o que foi clicado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # tecla pra baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # tecla pra cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # tecla enter
                        return MENU_OPTION[menu_option]

            self.window.blit(self.background, (0, 0))

            # executa o texto do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(22, MENU_OPTION[i], COLOR_CYAN, ((WIN_WIDTH / 2), 190 + 30 * i))
                else:
                    self.menu_text(22, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 190 + 30 * i))

            pygame.display.update()
            self.clock.tick(60)

