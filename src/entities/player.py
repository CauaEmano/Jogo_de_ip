import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_cima

        gravidade = 2
        velocidade = 10
        inercia_x = 1.5
        pulo_duplo = False
        pulo_duplo_timer = 0
        tecla_cima = False
        self.vel_x = 0
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
        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_cima

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
            self.vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            self.vel_x = velocidade
            self.flip = False
        
        # Inércia de movimento 
        # Maior no ar do que no chão
        if not self.no_ar: 
            inercia_x = 1.5
            pulo_duplo = False
        else: inercia_x = 0.7

        if self.vel_x < 0:
            self.vel_x += inercia_x
            if self.vel_x > 0: self.vel_x = 0
        elif self.vel_x > 0:
            self.vel_x -= inercia_x
            if self.vel_x < 0: self.vel_x = 0

        self.rect.x += self.vel_x

        # Movimentação vertical
        # Pulo duplo   
        if pulo_duplo: pulo_duplo_timer += 1
        else: pulo_duplo_timer = 0
        
        # keys[pygame.K_UP] and not tecla_cima tem comportamento semelhante ao KEYDOWN
        if keys[pygame.K_UP] and not tecla_cima and self.no_ar and pulo_duplo and pulo_duplo_timer >= 12:
            pulo_duplo = False
            self.vel_y = -20
        
        # Pulo normal
        if keys[pygame.K_UP] and not tecla_cima and not self.no_ar:
            self.vel_y = -25
            pulo_duplo = True

        tecla_cima = keys[pygame.K_UP]

        

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

