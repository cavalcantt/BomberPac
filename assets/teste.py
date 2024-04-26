import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo com Pygame")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Posicionamento proporcional dos personagens
CHARACTER_RADIUS = 20
CHARACTER_SPACING = 50

char1_x = SCREEN_WIDTH // 4
char2_x = SCREEN_WIDTH // 2
char3_x = 3 * SCREEN_WIDTH // 4
char_y = SCREEN_HEIGHT // 1.5

clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    screen.fill(WHITE)

    # Desenhar os personagens
    pygame.draw.circle(screen, RED, (char1_x, char_y), CHARACTER_RADIUS)
    pygame.draw.circle(screen, GREEN, (char2_x, char_y), CHARACTER_RADIUS)
    pygame.draw.circle(screen, BLUE, (char3_x, char_y), CHARACTER_RADIUS)

    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)
