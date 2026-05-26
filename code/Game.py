import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_STATE, LEVEL_STATE
from code.Menu import Menu
from code.Level import Level  # <-- Nova importação


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Rumo aos 5K")

        self.state = MENU_STATE
        self.menu = Menu(self.window)
        self.level = Level(self.window)  # <-- Instanciamos o Nível

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Captura todos os eventos (teclas, cliques) do frame atual
            eventos = pygame.event.get()

            for event in eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Transição do Menu para o Jogo
                if event.type == pygame.KEYDOWN:
                    if self.state == MENU_STATE and event.key == pygame.K_RETURN:
                        self.state = LEVEL_STATE

            # --- MÁQUINA DE ESTADOS ---
            if self.state == MENU_STATE:
                self.menu.run()
            elif self.state == LEVEL_STATE:
                # O Level agora recebe a lista de eventos para ler a barra de espaço
                self.level.run(eventos)

            pygame.display.flip()
            self.clock.tick(60)