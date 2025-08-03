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
    'Ship_Player1_Shot': 1,
    'Ship_Player2': 3,
    'Ship_Player2_Shot': 1,
    'Ship_Enemy1': 1,
    'Ship_Enemy1_Shot': 1,
    'Ship_Enemy2': 2,
    'Ship_Enemy2_Shot': 1,
}

ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level1BG5': 999,
    'Level1BG6': 999,

    'Ship_Player1': 300,
    'Ship_Player1_Shot': 30,
    'Ship_Player2': 300,
    'Ship_Player2_Shot': 30,

    'Ship_Enemy1': 50,
    'Ship_Enemy1_Shot': 10,
    'Ship_Enemy2': 80,
    'Ship_Enemy2_Shot': 10,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# F
FONT_TYPE = "Lucida Sans Typewriter"

# L
LEVEL_SOUND = "./assets/menu_level.mp3"

# M
MARGIN = 10
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
