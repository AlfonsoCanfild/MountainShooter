import pygame
from code.Entity import Entity


class Explosion(Entity):
    def __init__(self, position, frames):
        # Inicializa manualmente, sem carregar imagem da classe base
        self.name = 'Explosion'
        self.position = position
        self.frames = frames
        self.current_frame = 0
        self.animation_timer = 0

        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(center=position)
        self.health = 1  # Ainda será removida após a animação

    def move(self):
        self.animation_timer += 1
        if self.animation_timer % 5 == 0:
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.surf = self.frames[self.current_frame]
            else:
                self.health = 0  # remove a explosão após a última imagem
