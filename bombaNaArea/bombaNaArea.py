import sys
import pygame

matrix = [[0,0,0,0,...,0,0,0,0,0,0,0],
          [0,' ',' ',' ',...,' ',' ',' ',0,' ',' ',' '],
          [0,' ',0,' ',...,0,0,' ',0,' ',0,0],
          [0,' ',0,' ',...,' ',' ',' ',0,' ',0,0],
          [0,0,0,' ',...,0,0,' ',0,' ',' ',0],
          [0,' ',' ',' ',...,0,0,' ',' ',' ',' ',0],
          [0,0,0,0,...,0,0,0,0,0,' ',0],
          [0,' ',' ',' ',...,0,0,' ',' ',0,' ',0],
          [0,' ',0,0,...,' ',' ',0,' ',' ',' ',0],
          [0,' ',' ',' ',...,' ',' ',0,' ',0,0,0],
          [0,0,0,0,...,0,0,0,' ',0,0,0]]


pygame.init()
altura_tela = 1100
largura_tela = 600

grade = 50

largura_grade = largura_tela // grade
altura_grade =  altura_tela // grade

cor_tela = (0,120,20)
pygame.display.set_caption("BombaNaArea")

relogio = pygame.time.Clock()

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    tela = pygame.display.set_mode((altura_tela,largura_tela))
    tela.fill(cor_tela)
    pygame.display.update()
    relogio.tick(60)
