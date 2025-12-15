import pygame
# from sys import exit

class UI: #Aqui jaz a interface do inventario
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 20)

        self.icones = {
            "guarana": pygame.transform.scale(pygame.image.load("assets/images/Objetos/guarana0.png").convert_alpha(), (30, 30)),
            "pipa": pygame.transform.scale(pygame.image.load('assets/images/Objetos/pipa0.png').convert_alpha(), (40,40)),
            'raio': pygame.transform.scale(pygame.image.load('assets/images/Objetos/raio0.png').convert_alpha(), (40, 40)),
            'pedra': pygame.transform.scale(pygame.image.load('assets/images/Objetos/Pedra0.png').convert_alpha(), (40,40))
        }
    
    def display(self, superficie, inventario): #Display das informações do inventário
        pos_x = 460
        pos_y = 20
        espacamento = 100

        for item_tipo, quantidade in inventario.items():
            superficie.blit(self.icones.get(item_tipo, "chave não adicionada aos ícones"), (pos_x, pos_y))

            texto = self.fonte.render(str(quantidade), True, (255, 255, 255))
            superficie.blit(texto, (pos_x + 35, pos_y + 25), )

            pos_x += espacamento

#Tava testando
# screen = pygame.display.set_mode((1280,720))
# interface = UI()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     interface.display(screen, {"guarana": 3, "pipa": 1, "pedra": 20})
#     pygame.display.update()