import pygame

class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidade_x, velocidade_y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill('Yellow')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 600:
            self.kill()

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, caminho_imagem):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [pos_x, pos_y] #posicionando o divo
        self.mask = pygame.mask.from_surface(self.image)
    

class Onca(Inimigo):

    def __init__(self, pos_x, velocidade, vida):
        super().__init__(pos_x, 600, "")
        self.velocidade = velocidade
    
    def update(self):
        self.rect.x -= self.velocidade
    

class Tucano(Inimigo):

    def __init__(self, pos_x, pos_y, velocidade, vida, grupo_tiros):
        super().__init__(pos_x, pos_y, "")
        self.velocidade = velocidade
        self.grupo_tiros = grupo_tiros
        self.cooldown = 0
    
    def update(self):
        self.rect.x -= self.velocidade
        self.cooldown += 1
        if self.cooldown > 100:
            self.cooldown = 0
            bomba = Projetil(self.rect.centerx, self.rect.centery, 0, 10)
            self.grupo_tiros.add(bomba)


class Capivara(Inimigo):

    def __init__(self, pos_x, pos_y, vida, grupo_tiros):
        super().__init__(pos_x, pos_y, "")
        self.grupo_tiros = grupo_tiros
        self.cooldown = 0
    
    def update(self):
        self.cooldown += 1
        if self.cooldown > 200:
            self.cooldown = 0
            bomba = Projetil(self.rect.centerx, self.rect.centery, -10, 0)
            self.grupo_tiros.add(bomba)