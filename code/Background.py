import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT


class Background:
    # Gerencia o cenário com efeito de scroll infinito (parallax).
    # Usa duas cópias da imagem que se alternam para criar ilusão de movimento contínuo.
    def __init__(self):
        # Carrega a imagem do cenário
        self.image = pygame.image.load("asset/fundo.png").convert()
        # Ajusta a imagem para preencher toda a tela
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))

        # Posições X das duas cópias da imagem
        self.x1 = 0
        self.x2 = WIN_WIDTH

        # A velocidade do cenário movendo para a esquerda
        self.velocidade_x = -3

    def update(self):
        # Move as imagens e reseta a posição quando sai da tela.
        self.x1 += self.velocidade_x
        self.x2 += self.velocidade_x

        # Quando a imagem 1 sai completamente, leva ela para trás da imagem 2
        if self.x1 <= -WIN_WIDTH:
            self.x1 = WIN_WIDTH

        # Mesmo para a imagem 2
        if self.x2 <= -WIN_WIDTH:
            self.x2 = WIN_WIDTH

    def draw(self, window):
        # Renderiza ambas as cópias da imagem.
        window.blit(self.image, (self.x1, 0))
        window.blit(self.image, (self.x2, 0))
