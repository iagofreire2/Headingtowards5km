import pygame
from code.const import WIN_HEIGHT


class Player:
    def __init__(self):
        self.image = pygame.image.load("asset/corredor.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = WIN_HEIGHT - 100

        self.velocidade_y = 0
        self.gravidade = 0.8
        self.is_jumping = False
        self.chao = WIN_HEIGHT - 100

        # 1. Carrega o som de pulo (caminho relativo direto, sem a barra inicial!)
        self.som_pulo = pygame.mixer.Sound("asset/pulo.wav")
        self.som_pulo.set_volume(0.7)  # Volume de 0.0 a 1.0

    def pular(self):
        if not self.is_jumping:
            self.velocidade_y = -16
            self.is_jumping = True
            # 2. Toca o som no momento exato do pulo
            self.som_pulo.play()

    def update(self):
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        if self.rect.y >= self.chao:
            self.rect.y = self.chao
            self.is_jumping = False

    def draw(self, window):
        window.blit(self.image, self.rect)