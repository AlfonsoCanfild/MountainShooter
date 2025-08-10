import pygame

from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import (
    WIN_WIDTH, WIN_HEIGHT,
    ENTITY_SPEED, ENTITY_SHOT_DELAY, ENTITY_HEALTH
)


class Boss(Entity):
    def __init__(self, position=(WIN_WIDTH - 200, WIN_HEIGHT // 3)):
        super().__init__('Ship_EnemyBoss', position)
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.last_shot_time = 0  # último tempo que atirou
        self.direction = 1  # 1 = descendo, -1 = subindo
        self.shot_timer = 0
        self.shots = []

    def move(self):
        # Movimento vertical do boss
        self.rect.y += self.direction * self.speed
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.direction *= -1

    def shot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time >= ENTITY_SHOT_DELAY[self.name]:
            self.last_shot_time = now
            return EnemyShot(
                name=f'{self.name}_Shot',
                position=(self.rect.left, self.rect.centery))  # Ajustando o tiro
        return None
