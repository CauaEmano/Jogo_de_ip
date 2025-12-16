import pygame
# from sys import exit

from src import *

class UI: #Aqui jaz a interface do inventario E a barra de vida
    def __init__(self):
        pygame.font.init()

        self.fonte = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 10) 
        self.fonte_vida = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 30)

        self.heart_icon = pygame.image.load("assets/images/Objetos/coracao.png").convert_alpha()
        self.heart_icon = pygame.transform.scale(self.heart_icon, (25, 25))

        self.vida_pos_x = 20
        self.vida_pos_y = 20

        self.icones = {
            "guarana": pygame.transform.scale(pygame.image.load("assets/images/Objetos/guarana0.png").convert_alpha(), (30, 30)),
            "pipa": pygame.transform.scale(pygame.image.load('assets/images/Objetos/pipa0.png').convert_alpha(), (40,40)),
            'raio': pygame.transform.scale(pygame.image.load('assets/images/Objetos/raio0.png').convert_alpha(), (40, 40)),
            'pedra': pygame.transform.scale(pygame.image.load('assets/images/Objetos/Pedra0.png').convert_alpha(), (40,40))
        }
        
        self.bar_width = 10
        self.bar_height = 20
        self.bar_pos_x = 20 # Canto superior esquerdo
        self.bar_pos_y = 20

    def display_vida(self, surface, vida_atual, vida_maxima):
        espacamento_coracao = 30 # Distância entre um coração e outro
        
        for i in range(vida_maxima):
            x = self.vida_pos_x + (i * espacamento_coracao)
            y = self.vida_pos_y
            
            # Desenha o coração apenas se o índice for menor que a vida atual
            if i < vida_atual:
                surface.blit(self.heart_icon, (x, y))
            else:
                sombra = self.heart_icon.copy()
                sombra.fill((50, 50, 50), special_flags=pygame.BLEND_RGB_MULT)
                surface.blit(sombra, (x, y))

    def display(self, superficie, inventario, player_vida, player_max_vida): 
        
        # 1. Exibir a Barra de Vida
        self.display_vida(superficie, player_vida, player_max_vida)
        
        # 2. Exibir o Inventário (Mantido do seu código original)
        pos_x = 460
        pos_y = 20
        espacamento = 100

        for item_tipo, quantidade in inventario.items():
            superficie.blit(self.icones.get(item_tipo, "chave não adicionada aos ícones"), (pos_x, pos_y))

            texto = self.fonte.render(str(quantidade), True, (255, 255, 255))
            superficie.blit(texto, (pos_x + 35, pos_y + 25), )

            pos_x += espacamento