import pygame
import random
from code.Entity import Entity  # mantendo padrão do seu projeto


class EnemyBoss(Entity):
    def __init__(self, x, y, all_sprites, enemy_shots_group):
        super().__init__("assets/Ship_EnemyBoss.png", x, y)
        self.all_sprites = all_sprites
        self.enemy_shots_group = enemy_shots_group

        self.speed_y = 2
        self.direction_y = random.choice([-1, 1])

        self.original_x = x
        self.advance_distance = 50
        self.advance_speed = 1
        self.advancing = False

        # Timers
        self.last_double_shot = pygame.time.get_ticks()
        self.last_single_shot = pygame.time.get_ticks()

        self.double_shot_cooldown = 2000  # 2 segundos
        self.single_shot_cooldown = 4000  # 4 segundos

    def update(self):
        # Movimento vertical aleatório
        self.rect.y += self.speed_y * self.direction_y
        if self.rect.top <= 50 or self.rect.bottom >= 520:  # limites verticais
            self.direction_y *= -1

        # Movimento para frente e volta
        if not self.advancing and random.randint(0, 200) == 1:
            self.advancing = True
        if self.advancing:
            self.rect.x -= self.advance_speed
            if self.rect.x <= self.original_x - self.advance_distance:
                self.advancing = False
        else:
            if self.rect.x < self.original_x:
                self.rect.x += self.advance_speed

        # Disparos
        now = pygame.time.get_ticks()

        # Tiro duplo
        if now - self.last_double_shot >= self.double_shot_cooldown:
            self.shoot_double()
            self.last_double_shot = now

        # Tiro central
        if now - self.last_single_shot >= self.single_shot_cooldown:
            self.shoot_single()
            self.last_single_shot = now

    def shoot_single(self):
        shot = Entity("assets/Ship_EnemyBossShot0.png", self.rect.centerx, self.rect.centery)
        shot.speed_x = -5
        self.all_sprites.add(shot)
        self.enemy_shots_group.add(shot)

    def shoot_double(self):
        left_shot = Entity("assets/Ship_EnemyBossShot1.png", self.rect.left, self.rect.top + 10)
        right_shot = Entity("assets/Ship_EnemyBossShot1.png", self.rect.right - 20,
                            self.rect.bottom - 30)
        left_shot.speed_x = -5
        right_shot.speed_x = -5
        self.all_sprites.add(left_shot, right_shot)
        self.enemy_shots_group.add(left_shot, right_shot)
