import pygame
from code.const import WIN_HEIGHT


class Player:
    # Representa o jogador (corredor) que pode pular para evitar obstáculos.
    def __init__(self):
        self.image = pygame.image.load("asset/corredor.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = WIN_HEIGHT - 100

        # Física do pulo: velocidade vertical, gravidade e estado de salto
        self.velocidade_y = 0
        self.gravidade = 0.8
        self.is_jumping = False
        self.chao = WIN_HEIGHT - 100

        # Som para feedback ao jogador ao pular
        self.som_pulo = pygame.mixer.Sound("asset/pulo.wav")
        self.som_pulo.set_volume(0.7)

    def pular(self):
        # Inicia um pulo se o jogador estiver no chão.
        if not self.is_jumping:
            self.velocidade_y = -12
            self.is_jumping = True
            self.som_pulo.play()

    def update(self):
        # Atualiza a posição do jogador aplicando gravidade e detectando colisão com o chão.
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        # Detecta se voltou ao chão e reseta o estado de pulo
        if self.rect.y >= self.chao:
            self.rect.y = self.chao
            self.is_jumping = False

    def draw(self, window):
        window.blit(self.image, self.rect)
