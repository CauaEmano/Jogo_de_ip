import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global gravidade, vel_x, velocidade, inercia_x

        gravidade = 2
        vel_x = 0
        velocidade = 10
        inercia_x = 1.5
        self.vel_y = gravidade
        self.no_ar = True
        self.flip = False

        self.imagem_normal = pygame.image.load("assets/images/indio.png").convert_alpha()
        self.imagem_normal = pygame.transform.rotozoom(self.imagem_normal, 0, 2)
        self.imagem_invertida = pygame.transform.flip(self.imagem_normal, True, False)
        
        self.image = self.imagem_normal
        self.rect = self.image.get_rect(midbottom = (80, 500))
        self.mask = pygame.mask.from_surface(self.image)
    
    def movimentacao(self):
        global gravidade, vel_x, velocidade, inercia_x

        pulou = False
        mov_esq = False
        mov_dir = False

        keys = pygame.key.get_pressed()

        # Movimentação lateral
        if keys[pygame.K_LEFT]:
            mov_esq = True
        if keys[pygame.K_RIGHT]:
            mov_dir = True

        # Impedir direções simultâneas
        if mov_esq and not mov_dir:
            vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            vel_x = velocidade
            self.flip = False
        
        # Inércia de movimento 
        # Maior no ar do que no chão
        if not self.no_ar: inercia_x = 1.5
        else: inercia_x = 0.7

        if vel_x < 0:
            vel_x += inercia_x
            if vel_x > 0: vel_x = 0
        elif vel_x > 0:
            vel_x -= inercia_x
            if vel_x < 0: vel_x = 0

        self.rect.x += vel_x

        # Pulo
        if keys[pygame.K_UP] and not self.no_ar:
            self.vel_y = -25

        # Gravidade atua até atingir a velocidade terminal
        # 25 é a velocidade terminal
        if self.vel_y <= 25:
            self.vel_y += gravidade

        self.rect.y += self.vel_y

    def sprites(self):
        if self.flip:
            self.image = self.imagem_invertida
        else:
            self.image = self.imagem_normal

    def update(self):
        self.movimentacao()
        self.sprites()