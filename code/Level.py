import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, LEVEL_STATE, GAME_OVER_STATE, VICTORY_STATE, TARGET_DISTANCE
from code.Player import Player
from code.Enemy import Enemy


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player()
        self.enemies = []
        self.spawn_timer = 0

        # Variáveis do HUD (Heads-Up Display)
        self.distance = 0
        self.font = pygame.font.SysFont(None, 36)

    def run(self, eventos):
        self.window.fill((60, 60, 60))

        # 1. Controles do Jogador
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.pular()

        self.player.update()
        self.player.draw(self.window)

        # 2. Incrementa a distância (simula o deslocamento do asfalto)
        self.distance += 5

        # Renderiza o placar de distância na tela
        texto_distancia = self.font.render(f"Distância: {self.distance}m / {TARGET_DISTANCE}m", True, (255, 255, 255))
        self.window.blit(texto_distancia, (20, 20))

        # CONDIÇÃO DE VITÓRIA
        if self.distance >= TARGET_DISTANCE:
            return VICTORY_STATE

        # 3. Lógica de Geração de Obstáculos (Spawn)
        self.spawn_timer += 1
        if self.spawn_timer > 90:
            self.enemies.append(Enemy())
            self.spawn_timer = 0

        # 4. Atualização e Colisão
        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.window)

            if enemy.rect.x < -50:
                self.enemies.remove(enemy)

            # CONDIÇÃO DE DERROTA
            if self.player.rect.colliderect(enemy.rect):
                return GAME_OVER_STATE

        return LEVEL_STATE