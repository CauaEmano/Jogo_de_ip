import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        background = pygame.image.load('assets/images/cenario.png').convert() #Carreguei o fundo
        background = pygame.transform.scale(background, (1280, 850)) #moldei o tamanho

        self.image = pygame.Surface((20000, background.get_height()), pygame.SRCALPHA)  #Criei uma superfície gigante
        for x in range(0, 20000, background.get_width()): #Iterei sobre a superfície gigante pra desenhar o fundo sobre ela
            self.image.blit(background, (x, 0)) #Desenhando ne be

        self.rect = self.image.get_rect()

class Chao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        tile_img = pygame.image.load('assets/images/chao.png').convert_alpha()
    
        largura_tile = tile_img.get_width()
        altura_tile = tile_img.get_height() 

        largura_total_mundo = 20000

        self.image = pygame.Surface((largura_total_mundo, altura_tile), pygame.SRCALPHA) 

        for x in range(0, largura_total_mundo, largura_tile):
            self.image.blit(tile_img, (x, 0))

        self.rect = self.image.get_rect(top=600, left=0)

class Plataforma (pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()

        self.image = pygame.Surface([largura, altura])
        self.image.fill("Green")

        self.rect = self.image.get_rect(left = x, top = y)

class Parede (pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()

        self.image = pygame.Surface([largura, altura])
        self.image.fill("Blue")

        self.rect = self.image.get_rect(left = x, top = y)