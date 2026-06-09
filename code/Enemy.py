import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH


class Enemy(Entity):
    # Representa um obstáculo (buraco) que se move da direita para a esquerda.
    # A velocidade é injetada pelo Level para criar dificuldade progressiva.
    def __init__(self, velocidade_x=-7):
        super().__init__(WIN_WIDTH, 550, 40, 40, (255, 50, 50))

        self.image = pygame.image.load("asset/buraco.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH
        self.rect.y = 550

        # Velocidade dinâmica: aumenta conforme o jogador avança
        self.velocidade_x = velocidade_x

    def update(self):
        # Move o obstáculo para a esquerda a cada frame.
        self.rect.x += self.velocidade_x
