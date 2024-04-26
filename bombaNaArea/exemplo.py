import pygame
import os

gridDisplay = pygame.display.set_mode((1100, 600))
pygame.display.get_surface().fill((0, 250, 0))  # background

matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
          [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0],
          [0,1,0,2,2,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0],
          [0,0,0,2,2,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1],
          [0,1,1,2,2,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0],
          [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
          [0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0], 
          [1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0],
          [0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
          [0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]
 
grid_node_width = 50  
grid_node_height = 50

chao_zero = pygame.image.load("assets/1 Tiles/FieldsTileset.png")
chao_zero = pygame.transform.scale(chao_zero, (50, 50))

chao_um = pygame.image.load("assets/obj/1.png")
chao_um = pygame.transform.scale(chao_um, (50, 50))

agua_dois = pygame.image.load("assets/obj/Map_tile_13.png")
agua_dois = pygame.transform.scale(agua_dois, (50, 50))

mapa_tiles = {
    0: chao_zero,
    1: chao_um,
    2: agua_dois
}

listaTiles = []

# lista_objetos = [
#     pygame.image.load("assets/obj/Map_tile_13.png"),
#     pygame.image.load("assets/obj/Tree1.png"),
#     pygame.image.load("assets/obj/4.png"),
#   ]

def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])

Imagem = pygame.image.load("assets/1 Tiles/FieldsTileset.png")

def visualizeGrid():
    y = 0  # começamos no topo da tela
    for linha in matrix:
        x = 0 # para cada linha começamos à esquerda da tela novamente
        listaTiles.append([])
        pos_lista = len(listaTiles) - 1
        for item in linha:
            if item == 1:
                # i = linha.index(item)
                retangulo = mapa_tiles[item].get_rect(center=(x, y))
                gridDisplay.blit(mapa_tiles[item], retangulo)

                listaTiles[pos_lista].append({"item": item, "retangulo": retangulo})
            else:
                # Em vez de desenhar um quadrado verde, blite a imagem padrão
                gridDisplay.blit(Imagem, (x, y))
            x += grid_node_width  
        y += grid_node_height  

visualizeGrid()   

# jogador_imagem = pygame.image.load
# jogador_rect = jogador_imagem.get_rect(center=(x, y))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()