import pygame
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

        # Variáveis do HUD e placar
        self.distance = 0
        self.font = pygame.font.SysFont(None, 36)

        # Carrega o efeito sonoro de colisão/derrota
        self.som_batida = pygame.mixer.Sound("asset/batida.wav")

    def run(self, eventos):
        # 1. Atualiza e desenha o fundo em movimento
        self.bg.update()
        self.bg.draw(self.window)

        # 2. Captura os comandos do jogador
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.pular()

        # Atualiza a física do jogador e desenha na tela
        self.player.update()
        self.player.draw(self.window)

        # 3. Incrementa a distância e exibe no HUD
        self.distance += 5
        texto_distancia = self.font.render(f"Distância: {self.distance}m / {TARGET_DISTANCE}m", True, (255, 255, 255))
        self.window.blit(texto_distancia, (20, 20))

        # Verifica a CONDIÇÃO DE VITÓRIA
        if self.distance >= TARGET_DISTANCE:
            return VICTORY_STATE

        # 4. Lógica de Geração de Obstáculos (Spawn)
        self.spawn_timer += 1
        if self.spawn_timer > 90:  # A cada 90 frames, cria um inimigo
            self.enemies.append(Enemy())
            self.spawn_timer = 0

        # 5. Atualização e verificação de Colisão dos inimigos
        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.window)

            # Remove o inimigo da memória se ele sair da tela
            if enemy.rect.x < -50:
                self.enemies.remove(enemy)

            # Verifica a CONDIÇÃO DE DERROTA
            if self.player.rect.colliderect(enemy.rect):
                self.som_batida.play()  # Toca o som de impacto
                return GAME_OVER_STATE

        return LEVEL_STATE