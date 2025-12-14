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

        # --- Configuração da Animação ---
        self.frame_index = 0
        self.animation_speed = 0.5  # Com 35 frames, 0.5 é um bom começo
        self.frames_andar = []
        self.frames_parado = []

        for i in range(35):
            img = pygame.image.load(f"assets/images/indigena/indigena_correndo{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_andar.append(img)

        for i in range(36):
            img = pygame.image.load(f"assets/images/indigena/indigena{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_parado.append(img)
            
        # Atributos iniciais do sprite
        self.image = self.frames_andar[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (80, 500))
        self.mask = pygame.mask.from_surface(self.image)
    
    def movimentacao(self):
        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_cima

        mov_esq = False
        mov_dir = False
        keys = pygame.key.get_pressed()

        # Movimentação lateral
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mov_esq = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mov_dir = True

        if mov_esq and not mov_dir:
            self.vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            self.vel_x = velocidade
            self.flip = False
        
        # Inércia
        if not self.no_ar: 
            inercia_x = 1.5
            pulo_duplo = False
        else: 
            inercia_x = 0.7

        if self.vel_x < 0:
            self.vel_x += inercia_x
            if self.vel_x > 0: self.vel_x = 0
        elif self.vel_x > 0:
            self.vel_x -= inercia_x
            if self.vel_x < 0: self.vel_x = 0

        self.rect.x += self.vel_x

        # Pulo e Gravidade
        if pulo_duplo: pulo_duplo_timer += 1
        else: pulo_duplo_timer = 0
        
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not tecla_cima and self.no_ar and pulo_duplo and pulo_duplo_timer >= 12:
            pulo_duplo = False
            self.vel_y = -20
        
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not tecla_cima and not self.no_ar:
            self.vel_y = -25
            pulo_duplo = True

        tecla_cima = (keys[pygame.K_UP] or keys[pygame.K_w])

        if self.vel_y <= 25:
            self.vel_y += gravidade

        self.rect.y += self.vel_y

    def animar(self):
        # Seleciona a lista de frames baseada no estado do personagem
        if self.no_ar:
            # Se estiver no ar, usamos um frame fixo da corrida (ou um de pulo se tiver)
            frame_atual = self.frames_andar[5]
            
        elif self.vel_x != 0:
            # Correndo
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames_andar):
                self.frame_index = 0
            frame_atual = self.frames_andar[int(self.frame_index)]
            
        else:
            # Parado
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames_parado):
                self.frame_index = 0
            frame_atual = self.frames_parado[int(self.frame_index)]

        # salva a posição atual da base antes de mudar a imagem
        pos_chao_atual = self.rect.midbottom 

        # aplica a nova imagem
        self.image = pygame.transform.flip(frame_atual, self.flip, False)
        
        # cria o novo rect, mas "prende" ele na posição do chão salva
        self.rect = self.image.get_rect(midbottom = pos_chao_atual)
        
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.movimentacao()
        self.animar()