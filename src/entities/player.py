import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global gravidade, vel_y
        gravidade = 2
        vel_y = gravidade

        self.image = pygame.image.load("imagens/indio.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1.5)
        self.rect = self.image.get_rect(midbottom = (80, 600))
    
    def movimentacao(self):
        global gravidade, vel_y
        pulou = False
        no_ar = False

        keys = pygame.key.get_pressed()
        # Movimentação lateral
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Pulo
        if self.rect.bottom >= 595: no_ar = False
        else: no_ar = True

        if keys[pygame.K_UP] and not no_ar:
            vel_y = -20

        # gravidade age o tempo todo
        vel_y += gravidade

        self.rect.y += vel_y

        # Mantém no chão
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def update(self):
        self.movimentacao()