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

    #zona final
    subboss = pygame.sprite.GroupSingle()
    subboss.add(SubBoss(pos_x=500, pos_y=600))
    
    # Limpa grupos
    bullet_group.empty()
    tiros_inimigos.empty()
    inimigos.empty()
    coletaveis.empty()
    
    # Recria os inimigos e itens
    #zona1
    capivara0 = Capivara(pos_x=800, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    capivara1 = Capivara(pos_x=1500, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    capivara2 = Capivara(pos_x=2000, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    inimigos.add(capivara0, capivara1, capivara2)
    
    #zona 2
    tucano1 = Tucano(pos_x=2500, pos_y=400, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    onca1 = Onca(pos_x=3230, pos_y=600, velocidade=5, vida=2)
    capivara3 = Capivara(pos_x=4000, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    tucano2 = Tucano(pos_x=4000, pos_y=400, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    inimigos.add(tucano1, onca1, capivara3, tucano2)
    
    #Zona 3
    onca2 = Onca(pos_x=5000, pos_y=600, velocidade=5, vida=2)
    onca3 = Onca(pos_x=7000, pos_y=600, velocidade=5, vida=2)
    onca4 = Onca(pos_x=12000, pos_y=600, velocidade=5, vida=2)
    capivara4 = Capivara(pos_x=6000, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    capivara5 = Capivara(pos_x=10000, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    tucano3 = Tucano(pos_x=6000, pos_y=400, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    tucano4 = Tucano(pos_x=8000, pos_y=400, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    tucano5 = Tucano(pos_x=11000, pos_y=400, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    inimigos.add(onca2, onca3, onca4, capivara4, capivara5, tucano3, tucano4, tucano5)

    gerar_itens(coletaveis, Guarana, 8)
    gerar_itens(coletaveis, Pedra, 30)
    gerar_itens(coletaveis, Pipa, 1, 450)

    return player, bullet_group, tiros_inimigos, inimigos, coletaveis