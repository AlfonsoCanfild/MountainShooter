import pygame
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_shot_time = 0  # último tempo que atirou
        self.shot_cooldown = ENTITY_SHOT_DELAY  # ficou em milissegundos

    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]

    def shot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time >= ENTITY_SHOT_DELAY[self.name]:
            self.last_shot_time = now
            return EnemyShot(
                name=f'{self.name}_Shot',
                position=(self.rect.left, self.rect.centery))  # Ajustando o tiro
        return None

