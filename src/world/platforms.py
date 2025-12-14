import pygame

class Chao (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([99999, 720])
        self.image.fill("Red")

        self.rect = self.image.get_rect(top=600)

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