import pygame
import random  # <-- NOVA IMPORTAÇÃO para sortear os obstáculos
from code.const import WIN_WIDTH, WIN_HEIGHT, LEVEL_STATE, GAME_OVER_STATE, VICTORY_STATE, TARGET_DISTANCE
from code.Player import Player
from code.Enemy import Enemy
from code.Background import Background


class Level:
    def __init__(self, window):
        self.window = window
        self.bg = Background()
        self.player = Player()
        self.enemies = []
        self.spawn_timer = 0

        # Define um tempo inicial de 90 frames para o primeiro obstáculo
        self.tempo_spawn = 90

        self.distance = 0
        self.font = pygame.font.SysFont(None, 36)
        self.som_batida = pygame.mixer.Sound("asset/batida.wav")

    def run(self, eventos):
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

        # --- NOVA LÓGICA DE DIFICULDADE ---

        # 1. PACE PROGRESSIVO: A cada 1000m, a velocidade aumenta em 1 ponto
        velocidade_atual = -7 - (self.distance // 1000)

        self.spawn_timer += 1
        # Verifica se passou o tempo sorteado
        if self.spawn_timer > self.tempo_spawn:
            # 2. Cria o inimigo injetando a velocidade dinâmica
            self.enemies.append(Enemy(velocidade_atual))
            self.spawn_timer = 0

            # 3. SURGIMENTO IMPREVISÍVEL: Sorteia entre 50 e 100 frames para o próximo
            self.tempo_spawn = random.randint(50, 100)

        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.window)

            if enemy.rect.x < -50:
                self.enemies.remove(enemy)

            if self.player.rect.colliderect(enemy.rect):
                self.som_batida.play()
                return GAME_OVER_STATE

        return LEVEL_STATE