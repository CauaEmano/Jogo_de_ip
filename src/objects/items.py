import pygame
# from pygame.locals import * #Usei pra evitar escrever pygame.QUIT por exemplo

class Coletavel(pygame.sprite.Sprite): #Classe pai
    
    def __init__(self, pos_x, pos_y, caminho_imagem, frames, tamanho, tipo):
        super().__init__()
        self.caminho_imagem = caminho_imagem
        self.sprites = []
        for i in range(frames): #Adicionando os sprites
            imagem_a_salvar = pygame.image.load(f'{self.caminho_imagem}{i}.png').convert_alpha()
            imagem_a_salvar = pygame.transform.scale(imagem_a_salvar, (tamanho, tamanho))
            
            self.sprites.append(imagem_a_salvar)
        
        self.atual = 0 #Sprite atual
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [pos_x, pos_y] #posicionando o divo
        self.tipo = tipo #Criei para adicionar os efeitos certos pra cada item
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self): #Adicionando animação 
        self.atual += 0.1

        if self.atual >= len(self.sprites):
            self.atual = 0 

        self.image = self.sprites[int(self.atual)]
        
#Caso queira mudar o tamanho de algum objeto mude o penultimo parametro na chamada super

class Guarana(Coletavel):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, "assets/images/Objetos/guarana", 9, 50, 'guarana')

class Pipa(Coletavel):
    
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, "assets/images/Objetos/pipa", 9, 75, 'pipa')
    
class Pedra(Coletavel):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, "assets/images/Objetos/Pedra", 1, 50, 'pedra')
    
class Raio(Coletavel):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, "assets/images/Objetos/raio", 36, 50, 'raio')

#Descomente o código abaixo caso queria testar 
# pygame.init()
# janela = pygame.display.set_mode((400, 400))
# pygame.display.set_caption("Animando o guaraná")
# relogio = pygame.time.Clock()

# movendo_sprites = pygame.sprite.Group()
# guarana = Guarana(10, 10)
# pipa = Pipa(200,200)
# pedra = Pedra(300,300)
# raio = Raio(150, 250)
# movendo_sprites.add(guarana)
# movendo_sprites.add(pipa)
# movendo_sprites.add(pedra)
# movendo_sprites.add(raio)

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
    
#     janela.fill((0,0,0))
#     movendo_sprites.draw(janela)
#     movendo_sprites.update()
#     pygame.display.flip()
#     relogio.tick(60)