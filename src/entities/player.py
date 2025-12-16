import pygame
from src import *
from src.core.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_cima

        self.max_vida = 12
        self.vida = 12
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

        self.invincible_timer = 0
        self.INVINCIBILITY_DURATION = 60 # 1 segundo de invulnerabilidade (em 60 FPS)

        # --- Configuração da Animação ---
        self.frame_index = 0
        self.animation_speed = 0.5 
        self.frames_andar = []
        self.frames_parado = []

        # (Carregamento de imagens mantido igual ao seu original)
        for i in range(35):
            img = pygame.image.load(f"assets/images/Indigena/indigena_correndo{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_andar.append(img)

        for i in range(36):
            img = pygame.image.load(f"assets/images/Indigena/indigena{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_parado.append(img)
            
        self.image = self.frames_andar[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (80, 500))
        self.mask = pygame.mask.from_surface(self.image)
        self.inventario = {'pedra': 10}
        self.shoot_cooldown = 0
        self.SHOOT_COOLDOWN_MAX = 20
    
    def take_damage(self, amount=None, attacker_rect=None): 
        if self.invincible_timer <= 0:
            self.vida -= 1 
            self.invincible_timer = 60
            
            if self.vida <= 0:
                self.die()
                

    def die(self):
        print("Player morreu!")
        self.kill()

    def movimentacao(self):
        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_cima
        mov_esq = False
        mov_dir = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: mov_esq = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: mov_dir = True

        if mov_esq and not mov_dir:
            self.vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            self.vel_x = velocidade
            self.flip = False
        
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

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        self.rect.x += self.vel_x

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
        if self.no_ar:
            frame_atual = self.frames_andar[5]
        elif self.vel_x != 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames_andar):
                self.frame_index = 0
            frame_atual = self.frames_andar[int(self.frame_index)]
        else:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames_parado):
                self.frame_index = 0
            frame_atual = self.frames_parado[int(self.frame_index)]

        pos_chao_atual = self.rect.midbottom 

        # Efeito visual opcional de piscar ao receber dano
        if self.invincible_timer > 0 and (pygame.time.get_ticks() // 100) % 2 == 0:
            # Não desenha a imagem (cria efeito de piscar)
            self.image = pygame.Surface((0,0))
        else:
            self.image = pygame.transform.flip(frame_atual, self.flip, False)
        
        self.rect = self.image.get_rect(midbottom = pos_chao_atual)
        self.mask = pygame.mask.from_surface(self.image)
    
    def shoot(self, bullet_group, objetos_solidos, coletaveis, Pedra):
        municao_tipo = 'pedra'
        if self.shoot_cooldown == 0 and self.inventario.get(municao_tipo, 0) > 0:
            self.shoot_cooldown = self.SHOOT_COOLDOWN_MAX
            self.inventario[municao_tipo] -= 1 
            direction = -1 if self.flip else 1
            spawn_x = self.rect.centerx + (20 * direction)
            new_bullet = Bullet(spawn_x, self.rect.centery, direction, objetos_solidos, coletaveis, Pedra)
            bullet_group.add(new_bullet)
    
    def update(self):
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        self.movimentacao()
        self.animar()