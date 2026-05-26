import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, LEVEL_STATE, GAME_OVER_STATE
from code.Player import Player
from code.Enemy import Enemy


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player()
        self.enemies = []  # Lista para guardar os obstáculos
        self.spawn_timer = 0  # Cronômetro para gerar novos obstáculos

    def run(self, eventos):
        self.window.fill((60, 60, 60))

        # 1. Controles do Jogador
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.pular()

        self.player.update()
        self.player.draw(self.window)

        # 2. Lógica de Geração de Obstáculos (Spawn)
        self.spawn_timer += 1
        if self.spawn_timer > 90:  # A cada 90 frames (1.5 segundos), cria um inimigo
            self.enemies.append(Enemy())
            self.spawn_timer = 0

        # 3. Atualização e Colisão
        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.window)

            # Remove o inimigo se ele sair da tela pela esquerda
            if enemy.rect.x < -50:
                self.enemies.remove(enemy)

            # Verifica a Colisão (Condição de Derrota)
            if self.player.rect.colliderect(enemy.rect):
                print("BATEU!")
                return GAME_OVER_STATE  # Avisa que deu Game Over

        return LEVEL_STATE  # Se não bateu, continua no estado de jogo