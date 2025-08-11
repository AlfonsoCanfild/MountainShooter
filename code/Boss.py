import pygame
import random

from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Boss(Enemy):
    def __init__(self):
        # Posição inicial no canto direito e centralizado verticalmente
        start_x = WIN_WIDTH - 120
        start_y = WIN_HEIGHT // 2 - 60
        super().__init__('Ship_EnemyBoss', (start_x, start_y))

        # Movimento vertical
        self.speed_y = 2
        self.direction_y = random.choice([-1, 1])

        # Movimento horizontal (avançar/recuar)
        self.original_x = self.rect.x
        self.advance_distance = 90
        self.advance_speed = 1
        self.advancing = False

        # Timers de tiro
        self.last_center_shot = pygame.time.get_ticks()
        self.last_double_shot = pygame.time.get_ticks()

    def move(self):
        # Movimento vertical
        self.rect.y += self.speed_y * self.direction_y
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.direction_y *= -1

        # Movimento horizontal de avanço/recuo
        if not self.advancing and random.randint(0, 200) == 1:
            self.advancing = True
        if self.advancing:
            self.rect.x -= self.advance_speed
            if self.rect.x <= self.original_x - self.advance_distance:
                self.advancing = False
        else:
            if self.rect.x < self.original_x:
                self.rect.x += self.advance_speed

    def shoot_center(self):
        # Dispara do centro da nave
        shot_x = self.rect.centerx - 10
        shot_y = self.rect.centery
        return EnemyShot('Ship_EnemyBoss_Shot', (shot_x, shot_y))

    def shoot_double(self):
        # Dispara das extremidades
        shots = []
        left_shot_pos = (self.rect.left, self.rect.centery - 20)
        right_shot_pos = (self.rect.right - 20, self.rect.centery + 20)
        shots.append(EnemyShot('Ship_EnemyBoss_Shot', left_shot_pos))
        shots.append(EnemyShot('Ship_EnemyBoss_Shot', right_shot_pos))
        return shots
