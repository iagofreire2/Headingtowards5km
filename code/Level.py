import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player()

    def run(self, eventos):
        # Preenche a tela com um cinza escuro simulando o asfalto
        self.window.fill((60, 60, 60))

        # Escuta os comandos do teclado dentro do Level
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.pular()

        # Atualiza a física e desenha o jogador na tela
        self.player.update()
        self.player.draw(self.window)
