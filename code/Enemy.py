from code.Entity import Entity
from code.const import WIN_WIDTH

class Enemy(Entity):
    def __init__(self):
        # Chama o construtor da superclasse (largura 40, altura 40, cor vermelha)
        super().__init__(WIN_WIDTH, 450, 40, 40, (255, 50, 50))
        self.velocidade_x = -7 # Move para a esquerda

    def update(self):
        self.rect.x += self.velocidade_x

