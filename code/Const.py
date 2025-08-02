# C
import pygame

COLOR_ORANGE = 255, 128, 0
COLOR_CYAN = 0, 255, 255
COLOR_WHITE = 255, 255, 255

# E
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level1BG5': 5,
    'Level1BG6': 6,
    'Ship_Player1': 3,
    'Ship_Player2': 3,
    'Ship_Enemy1': 0.8,
    'Ship_Enemy2': 1.5,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# F
FONT_TYPE = "Lucida Sans Typewriter"

# L
LEVEL_SOUND = "./assets/menu_level.mp3"

# M
MENU_SOUND = "./assets/menu_sound.mp3"
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")

# P
PLAYER_KEY_UP = {'Ship_Player1': pygame.K_UP,
                 'Ship_Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Ship_Player1': pygame.K_DOWN,
                   'Ship_Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Ship_Player1': pygame.K_LEFT,
                   'Ship_Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Ship_Player1': pygame.K_RIGHT,
                    'Ship_Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Ship_Player1': pygame.K_SPACE,
                   'Ship_Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
