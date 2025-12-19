import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        background = pygame.image.load('assets/images/cenario.png').convert() #Carreguei o fundo
        background = pygame.transform.scale(background, (1280, 850)) #moldei o tamanho
        back_flipado = pygame.transform.flip(background, flip_x=True, flip_y=False)

        self.image = pygame.Surface((20000, background.get_height()), pygame.SRCALPHA)  #Criei uma superfície gigante
        contador = 0
        for x in range(0, 20000, background.get_width()): #Iterei sobre a superfície gigante pra desenhar o fundo sobre ela
            contador += 1
            if contador%2 != 0: self.image.blit(background, (x, 0)) #Desenhando ne be
            else: self.image.blit(back_flipado, (x, 0))

        self.rect = self.image.get_rect()

class Chao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        tile_img = pygame.image.load('assets/images/chao.png').convert_alpha()
        tile_flipado = pygame.transform.flip(tile_img, flip_x=True, flip_y=False)
    
        largura_tile = tile_img.get_width()
        altura_tile = tile_img.get_height() 

        largura_total_mundo = 20000

        self.image = pygame.Surface((largura_total_mundo, altura_tile), pygame.SRCALPHA) 
        contador = 0
        for x in range(0, largura_total_mundo, largura_tile):
            contador += 1
            if contador%2 != 0: self.image.blit(tile_img, (x, 0))
            else: self.image.blit(tile_flipado, (x, 0))

        self.rect = self.image.get_rect(top=600, left=0)
        
        self.hitbox = self.rect.copy()

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        img_bruta = pygame.image.load('assets/images/plataforma.png').convert_alpha()
        rect_real = img_bruta.get_bounding_rect()
        img_limpa = img_bruta.subsurface(rect_real)
        self.image = pygame.transform.scale(img_limpa, (largura, altura))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.caindo = False

        ajuste_vão = 10 
        self.hitbox = self.rect.copy()
        self.hitbox.top += ajuste_vão
        self.hitbox.height -= ajuste_vão
    def update(self):
        if self.caindo:
            self.rect.y += 10 
            if self.rect.y > 2000:
                self.kill()

class Parede (pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()

        self.image = pygame.Surface([largura, altura])
        self.image.fill("Blue")

        self.rect = self.image.get_rect(left = x, top = y)
        self.hitbox = self.rect.copy()