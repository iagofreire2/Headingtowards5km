import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT


class Background:
    def __init__(self):
        # Carrega a imagem do cenário usando o caminho relativo correto
        self.image = pygame.image.load("asset/fundo.png").convert()
        # Ajusta a imagem para preencher toda a tela
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))

        # Posições X das duas cópias da imagem (uma na tela e outra logo à direita)
        self.x1 = 0
        self.x2 = WIN_WIDTH

        # A velocidade do cenário movendo para a esquerda
        self.velocidade_x = -3

    def update(self):
        # Move as imagens
        self.x1 += self.velocidade_x
        self.x2 += self.velocidade_x

        # Se a imagem 1 saiu da tela, joga ela pro final da imagem 2
        if self.x1 <= -WIN_WIDTH:
            self.x1 = WIN_WIDTH

        # Se a imagem 2 saiu da tela, joga ela pro final da imagem 1
        if self.x2 <= -WIN_WIDTH:
            self.x2 = WIN_WIDTH

    def draw(self, window):
        # Desenha as duas cópias simultaneamente
        window.blit(self.image, (self.x1, 0))
        window.blit(self.image, (self.x2, 0))