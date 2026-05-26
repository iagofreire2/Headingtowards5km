import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_STATE, LEVEL_STATE
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Cria a janela principal do jogo
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Rumo aos 5K")

        # O jogo sempre começa no menu
        self.state = MENU_STATE
        self.menu = Menu(self.window)

        self.clock = pygame.time.Clock()

    def run(self):
        # O clássico Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Transição de tela: do Menu para o Jogo
                if event.type == pygame.KEYDOWN:
                    if self.state == MENU_STATE and event.key == pygame.K_RETURN:
                        self.state = LEVEL_STATE

            # Máquina de Estados: Renderiza a tela correspondente
            if self.state == MENU_STATE:
                self.menu.run()
            elif self.state == LEVEL_STATE:
                # Aqui entraremos com o cenário e o corredor mais tarde
                self.window.fill((50, 50, 50))

            pygame.display.flip()
            self.clock.tick(60)  # Crava o jogo em 60 FPS