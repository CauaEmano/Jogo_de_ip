import pygame

class Chao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        tile_img = pygame.image.load('assets/images/chao.png').convert_alpha()
        # tile_img = pygame.transform.scale(tile_img, (tile_img.get_width(), 210))
    
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