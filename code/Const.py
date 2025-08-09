import pygame

# B
BOSS_SHOT_CENTER_INTERVAL = 4000  # 4 segundos
BOSS_SHOT_DOUBLE_INTERVAL = 2000  # 2 segundos

# C
C_ORANGE = 255, 128, 0
C_CYAN = 0, 206, 209
C_WHITE = 255, 255, 255
C_GREEN = 0, 255, 0
C_BLUE = 0, 0, 255

# E
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,

    'Level2BG0': 0,
    'Level2BG1': 1,
    'Level2BG2': 2,
    'Level2BG3': 3,

    'Level3BG0': 0,
    'Level3BG1': 1,
    'Level3BG2': 2,

    'Ship_Player1': 3,
    'Ship_Player1_Shot': 4,
    'Ship_Player2': 3,
    'Ship_Player2_Shot': 4,

    'Ship_Enemy1': 1,
    'Ship_Enemy1_Shot': 3,
    'Ship_Enemy2': 2,
    'Ship_Enemy2_Shot': 4,

    'Ship_EnemyBoss': 3,
    'Ship_EnemyBossShot0': 3,
    'Ship_EnemyBossShot1': 4,
}

ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,

    'Level2BG0': 999,
    'Level2BG1': 999,
    'Level2BG2': 999,
    'Level2BG3': 999,

    'Level3BG0': 999,
    'Level3BG1': 999,
    'Level3BG2': 999,

    'Ship_Player1': 300,
    'Ship_Player1_Shot': 1,
    'Ship_Player2': 300,
    'Ship_Player2_Shot': 1,

    'Ship_Enemy1': 50,
    'Ship_Enemy1_Shot': 1,
    'Ship_Enemy2': 80,
    'Ship_Enemy2_Shot': 1,

    'Ship_EnemyBoss': 500,
    'Ship_EnemyBossShot0': 1,
    'Ship_EnemyBossShot1': 1,
}

ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,

    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,

    'Level3BG0': 0,
    'Level3BG1': 0,
    'Level3BG2': 0,

    'Ship_Player1': 1,
    'Ship_Player1_Shot': 25,
    'Ship_Player2': 1,
    'Ship_Player2_Shot': 25,

    'Ship_Enemy1': 1,
    'Ship_Enemy1_Shot': 30,
    'Ship_Enemy2': 1,
    'Ship_Enemy2_Shot': 50,

    'Ship_EnemyBoss': 20,
    'Ship_EnemyBossShot0': 90,
    'Ship_EnemyBossShot1': 40,
}

ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,

    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,

    'Level3BG0': 0,
    'Level3BG1': 0,
    'Level3BG2': 0,

    'Ship_Player1': 0,
    'Ship_Player1_Shot': 0,
    'Ship_Player2': 0,
    'Ship_Player2_Shot': 0,

    'Ship_Enemy1': 100,
    'Ship_Enemy1_Shot': 0,
    'Ship_Enemy2': 200,
    'Ship_Enemy2_Shot': 0,

    'Ship_EnemyBoss': 500,
    'Ship_EnemyBossShot0': 0,
    'Ship_EnemyBossShot1': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_ENEMY_SHOT = pygame.USEREVENT + 2

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SHOT_DELAY = {
    'Ship_Player1': 10,
    'Ship_Player2': 10,
    'Ship_Enemy1': 3000,
    'Ship_Enemy2': 4000,
}

# F
FONT_TYPE = "Lucida Sans Typewriter"

# M
MARGIN = 10
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

# S
MENU_SOUND = "./assets/menu_sound.mp3"

LEVEL_SOUND = "./assets/menu_level.mp3"

# T
TIMEOUT_STEP = 100

TIMEOUT_LEVEL = 10000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 120),
             1: (WIN_WIDTH / 2, 140),
             2: (WIN_WIDTH / 2, 160),
             3: (WIN_WIDTH / 2, 180),
             4: (WIN_WIDTH / 2, 200),
             5: (WIN_WIDTH / 2, 220),
             6: (WIN_WIDTH / 2, 240),
             7: (WIN_WIDTH / 2, 260),
             8: (WIN_WIDTH / 2, 280),
             9: (WIN_WIDTH / 2, 300),
             }
