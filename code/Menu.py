import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_BLUE, COLOR_WHITE, COLOR_GREEN, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        # 1. Adicionamos 'bold=True' para deixar as letras mais grossas e legíveis
        self.font_title = pygame.font.SysFont(None, 80, bold=True)
        # Aumentamos a fonte dos controles de 40 para 45 e ativamos o negrito
        self.font_text = pygame.font.SysFont(None, 45, bold=True)

        self.background = pygame.image.load("asset/menu_fundo.png").convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        self.window.blit(self.background, (0, 0))

        # 2. Renderiza os textos coloridos principais
        titulo = self.font_title.render("RUMO AOS 5K", True, COLOR_BLUE)
        controles = self.font_text.render("COMANDOS: Espaço - Pular", True, COLOR_GREEN)
        iniciar = self.font_text.render("Pressione ENTER para largar", True, COLOR_WHITE)

        # 3. Renderiza as "sombras" preenchidas em PRETO
        titulo_sombra = self.font_title.render("RUMO AOS 5K", True, COLOR_BLACK)
        controles_sombra = self.font_text.render("COMANDOS: Espaço - Pular", True, COLOR_BLACK)
        iniciar_sombra = self.font_text.render("Pressione ENTER para largar", True, COLOR_BLACK)

        # 4. Desenha as Sombras com um deslocamento de +3 e +2 pixels
        self.window.blit(titulo_sombra, (WIN_WIDTH // 2 - titulo.get_width() // 2 + 3, 83))
        # Desenha o Título colorido por cima
        self.window.blit(titulo, (WIN_WIDTH // 2 - titulo.get_width() // 2, 80))

        # Calcula as posições X centralizadas para os controles
        pos_x_controles = WIN_WIDTH // 2 - controles.get_width() // 2
        pos_x_iniciar = WIN_WIDTH // 2 - iniciar.get_width() // 2

        # Desenha Sombra e Texto dos Controles
        self.window.blit(controles_sombra, (pos_x_controles + 2, 452))
        self.window.blit(controles, (pos_x_controles, 450))

        # Desenha Sombra e Texto de Iniciar
        self.window.blit(iniciar_sombra, (pos_x_iniciar + 2, 522))
        self.window.blit(iniciar, (pos_x_iniciar, 520))