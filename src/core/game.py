import pygame, random
from src.entities.player import *
from src.entities.enemy import *
from src.objects import *


def gerar_itens(coletaveis, Item, quantidade, y=600):
    z = 0
    f = 15000//quantidade
    for i in range(quantidade):
        x = random.randint(z, z + f)
        item = Item(x, y)
        coletaveis.add(item)
        z += f

def carregar_nivel(player, bullet_group, tiros_inimigos, inimigos, coletaveis):
    # Reset do Player
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    
    # Limpa grupos
    bullet_group.empty()
    tiros_inimigos.empty()
    inimigos.empty()
    coletaveis.empty()
    
    # Recria os inimigos e itens
    onca_teste = Onca(pos_x=1200, pos_y=600, velocidade=10, vida=1)
    tucano_teste = Tucano(pos_x=1000, pos_y=100, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    capivara_teste = Capivara(pos_x=1100, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    inimigos.add(onca_teste, tucano_teste, capivara_teste)
    
    gerar_itens(coletaveis, Guarana, 3)
    gerar_itens(coletaveis, Pedra, 5)
    gerar_itens(coletaveis, Pipa, 1, 450)

    return player, bullet_group, tiros_inimigos, inimigos, coletaveis