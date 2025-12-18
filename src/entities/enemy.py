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
        if self.rect.x < -100 or self.rect.x > 15000 or self.rect.y < -100 or self.rect.y > 15000:
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
        self.no_chao = False

        if collided_platforms:
            platform = collided_platforms[0]
            if self.vel_y > 0:  
                self.rect.bottom = platform.rect.top
                self.no_chao = True
            elif self.vel_y < 0:
                self.rect.top = platform.rect.bottom
            self.vel_y = 0
            
    def update(self, objetos_solidos=None, player_rect=None):
        if objetos_solidos is not None and not self.is_flying:
            self.apply_gravity()
            self.handle_collisions(objetos_solidos)
        
        self.atual += 0.25
        if self.atual >= len(self.sprites):
            self.atual = 0 
        self.image = self.sprites[int(self.atual)]

        AGGRO_RANGE = 800
        distance = player_rect.centerx - self.rect.centerx
        
        if abs(distance) < AGGRO_RANGE:
            # Perseguir
            inalcancavel = -50 < distance and distance < 50 and (self.rect.centery - player_rect.centery > 100 or self.rect.centery - player_rect.centery < 100)
            if inalcancavel:
                self.velocidade = 3
            elif distance > 0:
                self.velocidade = 5
                self.direction = 1 # Player está à direita
            elif distance < 0:
                self.velocidade = 5
                self.direction = -1 # Player está à esquerda
        else:
            self.direction = 0 # Parar se estiver fora do alcance

        self.image = pygame.transform.flip(self.image, True, False) if self.direction == 1 else self.image


class Onca(Inimigo):
    
    def __init__(self, pos_x, pos_y, velocidade, vida): 
        global ataque_timer, ataque_cooldown

        super().__init__(pos_x, pos_y, "assets/images/Inimigos/animais/onca", 36, 130, 75, vida) 
        self.velocidade = velocidade
        self.direction = -1 # Direção inicial de movimento
        self.is_flying = False
        self.atacando = False
        ataque_timer = 0
        ataque_cooldown = 0

        self.sprites_ataque = []
        for i in range(16):
            imagem_a_salvar = pygame.image.load(f"assets/images/Inimigos/animais/onca_atacando{i}.png").convert_alpha()
            imagem_a_salvar = pygame.transform.scale(imagem_a_salvar, (140, 90))
            self.sprites_ataque.append(imagem_a_salvar)
            

    def update(self, objetos_solidos, player_rect):
        global ataque_timer, ataque_cooldown

        if objetos_solidos is not None and not self.is_flying:
            if not self.atacando: self.apply_gravity()
            self.handle_collisions(objetos_solidos)
        
        # Animação de corrida
        self.atual += 0.25
        if self.atual >= len(self.sprites):
            self.atual = 0 
        self.image = self.sprites[int(self.atual)]

        # Perseguição
        AGGRO_RANGE = 800
        distance = player_rect.centerx - self.rect.centerx
        ataque_cooldown -= 1 if ataque_cooldown > 0 and not self.atacando else 0

        if not self.atacando and ataque_cooldown <= 8:
            if abs(distance) < AGGRO_RANGE:
                perto = -80 < distance and distance < 80
                if perto:
                    self.velocidade = 6
                elif distance > 0:
                    self.velocidade = 10
                    self.direction = 1 # Player está à direita
                elif distance < 0:
                    self.velocidade = 10
                    self.direction = -1 # Player está à esquerda
            else:
                self.direction = 0 # Parar se estiver fora do alcance

        # Ataque
        if self.atacando:
            self.atual += .1
            if self.atual >= len(self.sprites_ataque):
                self.atual = 0 
                self.atacando = False
                ataque_timer = 0
        
            ataque_timer += 1
            self.image = self.sprites_ataque[int(self.atual)]
        
        alcancavel = -220 < distance and distance < 220 and (self.rect.centery - player_rect.centery < 40 and self.rect.centery - player_rect.centery > -20)
        if alcancavel and not self.atacando and self.no_chao and ataque_cooldown == 0:
            self.atual = 0
            self.atacando = True

        if self.atacando: # Deslocamento durante ataque
            if ataque_timer >= 15:
                ataque_cooldown = 80
                self.rect.x += 17.5 * self.direction
                self.rect.y -= 2
                if ataque_timer > 35:
                    self.rect.y += 5.2
        elif ataque_cooldown <= 8: # Deslocamento padrão
            self.rect.x += self.velocidade * self.direction

        self.image = pygame.transform.flip(self.image, True, False) if self.direction == 1 else self.image
    

class Tucano(Inimigo):
    
    def __init__(self, pos_x, pos_y, velocidade, vida, grupo_tiros):
        super().__init__(pos_x, pos_y, "assets/images/Inimigos/animais/tucano", 31, 100, 100, vida)
        self.velocidade = velocidade
        self.grupo_tiros = grupo_tiros
        self.cooldown = 0
        self.max_cooldown = 50
        self.is_flying = True
        self.direction = -1
        
    def update(self, objetos_solidos, player_rect):
        self.cooldown += 1

        super().update(objetos_solidos, player_rect)
        self.rect.x += self.velocidade * self.direction

        if self.cooldown > self.max_cooldown:
            self.cooldown = 0
            bomba = Projetil(self.rect.centerx, self.rect.centery, 0, 10) 
            self.grupo_tiros.add(bomba)
        

class Capivara(Inimigo):
    
    def __init__(self, pos_x, pos_y, vida, grupo_tiros):
        super().__init__(pos_x, pos_y, "assets/images/Inimigos/animais/capivara", 36, 50, 50, vida)
        self.grupo_tiros = grupo_tiros
        self.cooldown = 0
        self.max_cooldown = 100
        self.is_flying = False
    
    def update(self, objetos_solidos, player_rect):
        self.cooldown += 1
        
        super().update(objetos_solidos, player_rect)

        if self.cooldown > self.max_cooldown and self.direction != 0:
            self.cooldown = 0
            velocidade = self.direction * 10
            bomba = Projetil(self.rect.centerx, self.rect.centery, velocidade, 0) 
            self.grupo_tiros.add(bomba)