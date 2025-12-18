import pygame
from src import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, objetos_solidos, coletaveis, classe_pedra):
        super().__init__()
        
        self.image = pygame.image.load("assets/images/Objetos/Pedra0.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)
        self.rect = self.image.get_rect(center=(x, y))
        # tirei o self maskpq tava travando glr, a colisão agr vai ser por rect
        
        # Variáveis de Movimento
        self.speed_x = 20
        self.vel_y = 0
        self.GRAVITY = 0.2
        self.direction = direction
        
        self.objetos_solidos = objetos_solidos
        self.coletaveis = coletaveis               
        self.Pedra_Coletavel = classe_pedra

    def apply_gravity(self):
        self.vel_y += self.GRAVITY
        self.rect.y += self.vel_y

    def update(self):

        # Movimento Horizontal
        self.rect.x += (self.speed_x * self.direction)
        
        # Checa Colisão com Objetos Sólidos APÓS o movimento horizontal
        collided_platforms_horizontal = pygame.sprite.spritecollide(self, self.objetos_solidos, False) 
        
        if collided_platforms_horizontal:
            
            # Se colidiu, é um rebote na parede (não queremos que vire coletável)
            plataforma_colidida = collided_platforms_horizontal[0]
            
            # Reposiciona para evitar que fique presa
            if self.direction > 0: # Vindo da esquerda (indo para a direita)
                self.rect.right = plataforma_colidida.rect.left
            else: # Vindo da direita (indo para a esquerda)
                self.rect.left = plataforma_colidida.rect.right

            # Inverte a direção e define a nova velocidade
            self.direction *= -1 
            self.speed_x = 30
            

        # Movimento Vertical e Gravidade
        self.apply_gravity()
        
        # Checa Colisão com Objetos Sólidos APÓS o movimento vertical
        collided_platforms_vertical = pygame.sprite.spritecollide(self, self.objetos_solidos, False) 
        
        if collided_platforms_vertical:
            # Dropar a Pedra Coletável 
            plataforma_chao = collided_platforms_vertical[0]
            self.rect.bottom = plataforma_chao.rect.top # Posiciona exatamente no topo
            
            # Cria a nova instância do coletável
            nova_pedra = self.Pedra_Coletavel(self.rect.centerx, self.rect.bottom)
            
            # Adiciona ao grupo de coletáveis
            self.coletaveis.add(nova_pedra)

            # Destrói o projétil
            self.kill()
            
        # Limite de Voo Vertical (kill para fora da tela)
        if self.rect.top > 720 + 50:
            self.kill()