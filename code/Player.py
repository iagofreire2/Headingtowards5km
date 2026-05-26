import pygame
from code.const import WIN_HEIGHT


class Player:
    def __init__(self):
        # Superfície provisória (um retângulo 50x80)
        self.image = pygame.Surface((50, 80))
        self.image.fill((255, 255, 0))  # Cor Amarela

        # Pega as coordenadas (rect) da imagem para tratar colisões
        self.rect = self.image.get_rect()
        self.rect.x = 100  # Posição fixa no eixo X (lado esquerdo)
        self.rect.y = WIN_HEIGHT - 150  # Fica próximo à base da tela

        # Variáveis da física do pulo
        self.velocidade_y = 0
        self.gravidade = 0.8
        self.is_jumping = False

        # O chão imaginário onde o corredor pisa
        self.chao = WIN_HEIGHT - 150

    def pular(self):
        # Só permite pular se estiver no chão
        if not self.is_jumping:
            self.velocidade_y = -16  # Força do pulo para cima (eixo Y negativo)
            self.is_jumping = True

    def update(self):
        # 1. Aplica a gravidade constantemente
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        # 2. Verifica colisão com o chão
        if self.rect.y >= self.chao:
            self.rect.y = self.chao
            self.is_jumping = False  # Tocou o chão, pode pular novamente

    def draw(self, window):
        window.blit(self.image, self.rect)
