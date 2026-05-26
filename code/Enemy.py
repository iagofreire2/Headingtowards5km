import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH


class Enemy(Entity):
    def __init__(self):
        # Aumentamos o Y de 450 para 490 para ele descer em direção ao asfalto
        super().__init__(WIN_WIDTH, 550, 40, 40, (255, 50, 50))

        self.image = pygame.image.load("asset/buraco.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH

        # O Y aqui também precisa ser atualizado para 490
        self.rect.y = 550

        self.velocidade_x = -7

    def update(self):
        self.rect.x += self.velocidade_x
