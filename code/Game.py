import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_STATE, LEVEL_STATE, GAME_OVER_STATE
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        # Inicializa a janela com as dimensões das constantes
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Rumo aos 5K")

        # Define o estado inicial como o Menu
        self.state = MENU_STATE
        self.menu = Menu(self.window)
        self.level = Level(self.window)

        self.clock = pygame.time.Clock()

    def run(self):
        # Loop Principal do Motor do Jogo
        while True:
            # Captura os eventos de teclado e sistema do frame atual
            eventos = pygame.event.get()

            for event in eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Transição: Menu -> Jogo (Largar)
                    if self.state == MENU_STATE and event.key == pygame.K_RETURN:
                        self.state = LEVEL_STATE

                    # Transição: Game Over -> Reiniciar para o Menu
                    elif self.state == GAME_OVER_STATE and event.key == pygame.K_RETURN:
                        # Reinancia o objeto Level para limpar os obstáculos antigos da lista
                        self.level = Level(self.window)
                        self.state = MENU_STATE

            # --- MÁQUINA DE ESTADOS (Gerenciador de Telas) ---
            if self.state == MENU_STATE:
                self.menu.run()

            elif self.state == LEVEL_STATE:
                # O Level atualiza a física e retorna o próximo estado (continua ou morre)
                self.state = self.level.run(eventos)

            elif self.state == GAME_OVER_STATE:
                # Desenha uma tela de Game Over limpa
                self.window.fill((0, 0, 0))

                fonte_go = pygame.font.SysFont(None, 60)
                fonte_sub = pygame.font.SysFont(None, 30)

                texto_game_over = fonte_go.render("GAME OVER", True, (255, 50, 50))
                texto_instrucao = fonte_sub.render("Pressione ENTER para voltar ao Menu", True, (255, 255, 255))

                self.window.blit(texto_game_over,
                                 (WIN_WIDTH // 2 - texto_game_over.get_width() // 2, WIN_HEIGHT // 2 - 40))
                self.window.blit(texto_instrucao,
                                 (WIN_WIDTH // 2 - texto_instrucao.get_width() // 2, WIN_HEIGHT // 2 + 30))

            # Atualiza a tela física e segura a taxa de quadros em 60 FPS
            pygame.display.flip()
            self.clock.tick(60)