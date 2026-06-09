import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_BLUE, COLOR_WHITE, COLOR_GREEN, COLOR_BLACK


class Menu:
    # Tela inicial do jogo com controles e instruções.
    # Usa técnica de shadow rendering (renderiza texto preto deslocado para criar profundidade).
    def __init__(self, window):
        self.window = window
        # Fontes negritadas para melhor legibilidade no menu
        self.font_title = pygame.font.SysFont(None, 80, bold=True)
        self.font_text = pygame.font.SysFont(None, 45, bold=True)

        self.background = pygame.image.load("asset/menu_fundo.png").convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        self.window.blit(self.background, (0, 0))

        # Renderiza textos coloridos principais
        titulo = self.font_title.render("RUMO AOS 5K", True, COLOR_BLUE)
        controles = self.font_text.render("COMANDOS: Espaço - Pular", True, COLOR_GREEN)
        iniciar = self.font_text.render("Pressione ENTER para largar", True, COLOR_WHITE)

        # Renderiza sombras em preto para criar efeito de profundidade
        titulo_sombra = self.font_title.render("RUMO AOS 5K", True, COLOR_BLACK)
        controles_sombra = self.font_text.render("COMANDOS: Espaço - Pular", True, COLOR_BLACK)
        iniciar_sombra = self.font_text.render("Pressione ENTER para largar", True, COLOR_BLACK)

        # Desenha sombra deslocada (+3, +2 pixels), depois o texto colorido por cima
        self.window.blit(titulo_sombra, (WIN_WIDTH // 2 - titulo.get_width() // 2 + 3, 83))
        self.window.blit(titulo, (WIN_WIDTH // 2 - titulo.get_width() // 2, 80))

        pos_x_controles = WIN_WIDTH // 2 - controles.get_width() // 2
        pos_x_iniciar = WIN_WIDTH // 2 - iniciar.get_width() // 2

        self.window.blit(controles_sombra, (pos_x_controles + 2, 452))
        self.window.blit(controles, (pos_x_controles, 450))

        self.window.blit(iniciar_sombra, (pos_x_iniciar + 2, 522))
        self.window.blit(iniciar, (pos_x_iniciar, 520))
