import pygame

class Projetil(pygame.sprite.Sprite):
    """Projetil usado pelos inimigos (Tucano, Capivara)."""
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
        
        # Destruir projétil fora dos limites da tela (ajuste os valores conforme o tamanho do seu mapa)
        if self.rect.x < -100 or self.rect.x > 1380 or self.rect.y < -100 or self.rect.y > 820:
            self.kill()

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, caminho_imagem, frames, tamanho_x, tamanho_y, vida=1):
        super().__init__()
        # Variáveis de física
        self.vel_y = 0
        self.GRAVITY = 1
        self.is_flying = False # Flag para desabilitar gravidade em aéreos
        
        # Placeholder visual
        self.caminho_imagem = caminho_imagem
        self.sprites = []
        for i in range(frames):
            imagem_a_salvar = pygame.image.load(f'{self.caminho_imagem}{i}.png').convert_alpha()
            imagem_a_salvar = pygame.transform.scale(imagem_a_salvar, (tamanho_x, tamanho_y))
            self.sprites.append(imagem_a_salvar)
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)
        self.vida = vida 
        
    def take_damage(self, amount):
        """Aplica dano (chamado pelo projétil do Player)."""
        self.vida -= amount
        if self.vida <= 0:
            self.kill()
            
    # --- Lógica de Colisão/Gravidade ---

    def apply_gravity(self):
        self.vel_y += self.GRAVITY
        self.rect.y += self.vel_y

    def handle_collisions(self, objetos_solidos):
        collided_platforms = pygame.sprite.spritecollide(self, objetos_solidos, False)
        
        if collided_platforms:
            platform = collided_platforms[0]
            if self.vel_y > 0:  
                self.rect.bottom = platform.rect.top
            elif self.vel_y < 0:
                self.rect.top = platform.rect.bottom
            self.vel_y = 0
            
    # 🚨 Base update agora aceita player_rect (para compatibilidade)
    def update(self, objetos_solidos=None, player_rect=None):
        if objetos_solidos is not None and not self.is_flying:
            self.apply_gravity()
            self.handle_collisions(objetos_solidos)
        
        self.atual += 0.25
        if self.atual >= len(self.sprites):
            self.atual = 0 
        self.image = self.sprites[int(self.atual)]

class Onca(Inimigo):
    
    def __init__(self, pos_x, pos_y, velocidade, vida): 
        super().__init__(pos_x, pos_y, "assets/images/Inimigos/animais/onca", 36, 125, 75, vida) 
        self.velocidade = velocidade
        self.direction = -1 # Direção inicial de movimento
        self.is_flying = False
    
    def chase_player(self, player_rect):
        AGGRO_RANGE = 500
        distance = player_rect.centerx - self.rect.centerx
        
        if abs(distance) < AGGRO_RANGE:
            # Perseguir
            if distance > 0 and player_rect.y >= 300:
                self.direction = 1 # Player está à direita
                self.image = pygame.transform.flip(self.image, True, False)
            else:
                self.direction = -1 # Player está à esquerda
        else:
            self.direction = -1 # Parar se estiver fora do alcance
            
        # Aplica o movimento horizontal
        self.rect.x += self.velocidade * self.direction


    # 🚨 Update da Onça chama chase_player e super().update
    def update(self, objetos_solidos, player_rect):
        
        super().update(objetos_solidos, player_rect) 
        if player_rect:
            self.chase_player(player_rect)
    

class Tucano(Inimigo):
    
    def __init__(self, pos_x, pos_y, velocidade, vida, grupo_tiros):
        super().__init__(pos_x, pos_y, "assets/images/Inimigos/animais/tucano", 31, 100, 100, vida)
        self.velocidade = velocidade
        self.grupo_tiros = grupo_tiros
        self.cooldown = 0
        self.max_cooldown = 50
        self.is_flying = True
        
    def update(self, objetos_solidos=None, player_rect=None):
        self.rect.x -= self.velocidade # Movimento simples para a esquerda
        self.cooldown += 1

        self.atual += 0.25
        if self.atual >= len(self.sprites):
            self.atual = 0 
        self.image = self.sprites[int(self.atual)]
        
        if self.cooldown > self.max_cooldown:
            self.cooldown = 0
            bomba = Projetil(self.rect.centerx, self.rect.centery, 0, 10) 
            self.grupo_tiros.add(bomba)
        
        # Não chama super().update() pois é voador.


# class Capivara(Inimigo):
    
#     def __init__(self, pos_x, pos_y, vida, grupo_tiros):
#         super().__init__(pos_x, pos_y, "", vida) 
#         self.grupo_tiros = grupo_tiros
#         self.cooldown = 0
#         self.max_cooldown = 200 
#         self.is_flying = False
    
#     def update(self, objetos_solidos, player_rect=None):
#         self.cooldown += 1
        
#         if self.cooldown > self.max_cooldown:
#             self.cooldown = 0
#             bomba = Projetil(self.rect.centerx, self.rect.centery, -10, 0) 
#             self.grupo_tiros.add(bomba)
            
#         super().update(objetos_solidos, player_rect)