import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_STATE, LEVEL_STATE, GAME_OVER_STATE, VICTORY_STATE
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Garante que o sistema de áudio está ativo

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Rumo aos 5K")

        # Inicia a trilha sonora de fundo em loop infinito (-1)
        pygame.mixer.music.load("asset/trilha.wav")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        self.state = MENU_STATE
        self.menu = Menu(self.window)
        self.level = Level(self.window)

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            eventos = pygame.event.get()

            for event in eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Transição do Menu para o Gameplay
                    if self.state == MENU_STATE and event.key == pygame.K_RETURN:
                        self.state = LEVEL_STATE

                    # Permite reiniciar o nível com ENTER caso perca ou ganhe
                    elif (
                            self.state == GAME_OVER_STATE or self.state == VICTORY_STATE) and event.key == pygame.K_RETURN:
                        self.level = Level(self.window)  # Reseta o nível
                        self.state = MENU_STATE

            # --- MÁQUINA DE ESTADOS ---
            if self.state == MENU_STATE:
                self.menu.run()

            elif self.state == LEVEL_STATE:
                self.state = self.level.run(eventos)

            elif self.state == GAME_OVER_STATE:
                self.window.fill((0, 0, 0))
                fonte_go = pygame.font.SysFont(None, 60)
                fonte_sub = pygame.font.SysFont(None, 30)

                texto_game_over = fonte_go.render("GAME OVER", True, (255, 50, 50))
                texto_instrucao = fonte_sub.render("Pressione ENTER para voltar ao Menu", True, (255, 255, 255))

                self.window.blit(texto_game_over,
                                 (WIN_WIDTH // 2 - texto_game_over.get_width() // 2, WIN_HEIGHT // 2 - 40))
                self.window.blit(texto_instrucao,
                                 (WIN_WIDTH // 2 - texto_instrucao.get_width() // 2, WIN_HEIGHT // 2 + 30))

            elif self.state == VICTORY_STATE:
                self.window.fill((0, 0, 0))
                fonte_vic = pygame.font.SysFont(None, 60)
                fonte_sub = pygame.font.SysFont(None, 30)

                texto_vitoria = fonte_vic.render("5K CONCLUÍDOS! NOVO RP!", True, (50, 255, 50))
                texto_instrucao = fonte_sub.render("Pressione ENTER para voltar ao Menu", True, (255, 255, 255))

                self.window.blit(texto_vitoria, (WIN_WIDTH // 2 - texto_vitoria.get_width() // 2, WIN_HEIGHT // 2 - 40))
                self.window.blit(texto_instrucao,
                                 (WIN_WIDTH // 2 - texto_instrucao.get_width() // 2, WIN_HEIGHT // 2 + 30))

            pygame.display.flip()
            self.clock.tick(60)