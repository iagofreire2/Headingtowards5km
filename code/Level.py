import pygame
import random
from code.const import WIN_WIDTH, WIN_HEIGHT, LEVEL_STATE, GAME_OVER_STATE, VICTORY_STATE, TARGET_DISTANCE
from code.Player import Player
from code.Enemy import Enemy
from code.Background import Background


class Level:
    # Gerencia a lógica de um nível: jogador, obstáculos, física e dificuldade progressiva.
    def __init__(self, window):
        self.window = window
        self.bg = Background()
        self.player = Player()
        self.enemies = []
        self.spawn_timer = 0

        # Tempo inicial antes do primeiro obstáculo (em frames)
        self.tempo_spawn = 90

        self.distance = 0
        self.font = pygame.font.SysFont(None, 36)
        self.som_batida = pygame.mixer.Sound("asset/batida.wav")

    def run(self, eventos):
        # Executa a lógica de um frame do nível.
        # Retorna o novo estado (nível, game over ou vitória).
        self.bg.update()
        self.bg.draw(self.window)

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.pular()

        self.player.update()
        self.player.draw(self.window)

        self.distance += 5
        texto_distancia = self.font.render(f"Distância: {self.distance}m / {TARGET_DISTANCE}m", True, (255, 255, 255))
        self.window.blit(texto_distancia, (20, 20))

        if self.distance >= TARGET_DISTANCE:
            return VICTORY_STATE

        # Dificuldade progressiva: a cada 1000m, os obstáculos ficam 1 ponto mais rápidos
        velocidade_atual = -7 - (self.distance // 1000)

        self.spawn_timer += 1
        if self.spawn_timer > self.tempo_spawn:
            # Cria um novo inimigo com velocidade dinâmica
            self.enemies.append(Enemy(velocidade_atual))
            self.spawn_timer = 0

            # Próximo inimigo aparece em intervalo aleatório (imprevisibilidade)
            self.tempo_spawn = random.randint(50, 100)

        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.window)

            # Remove inimigos que saíram da tela (otimização de memória)
            if enemy.rect.x < -50:
                self.enemies.remove(enemy)

            # Verifica colisão: o jogador chocou com um obstáculo?
            if self.player.rect.colliderect(enemy.rect):
                self.som_batida.play()
                return GAME_OVER_STATE

        return LEVEL_STATE
