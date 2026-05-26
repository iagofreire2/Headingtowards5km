import pygame
from code.const import WIN_WIDTH, COLOR_BLUE, COLOR_WHITE, COLOR_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        # Fontes nativas do Pygame para não precisarmos de arquivos externos agora
        self.font_title = pygame.font.SysFont(None, 80)
        self.font_text = pygame.font.SysFont(None, 40)

    def run(self):
        # Fundo preto para o menu
        self.window.fill((0, 0, 0))

        # Renderização dos textos
        titulo = self.font_title.render("RUMO AOS 5K", True, COLOR_BLUE)
        controles = self.font_text.render("COMANDOS: Espaço - Pular", True, COLOR_GREEN)
        iniciar = self.font_text.render("Pressione ENTER para largar", True, COLOR_WHITE)

        # Posicionamento centralizado na tela
        self.window.blit(titulo, (WIN_WIDTH // 2 - titulo.get_width() // 2, 120))
        self.window.blit(controles, (WIN_WIDTH // 2 - controles.get_width() // 2, 300))
        self.window.blit(iniciar, (WIN_WIDTH // 2 - iniciar.get_width() // 2, 450))
