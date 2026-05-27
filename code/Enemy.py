import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH


class Enemy(Entity):
    # 1. Adicionamos o parâmetro de velocidade (padrão -7)
    def __init__(self, velocidade_x=-7):
        super().__init__(WIN_WIDTH, 550, 40, 40, (255, 50, 50))

        self.image = pygame.image.load("asset/buraco.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH
        self.rect.y = 550

        # 2. Agora ele usa a velocidade ditada pelo Nível
        self.velocidade_x = velocidade_x

    def update(self):
        self.rect.x += self.velocidade_x