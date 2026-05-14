import pygame 
import sys

pygame.init()

pantalla = pygame.display.set_mode((370,442))
pygame.display.set_caption("Mario Bros")
Negro = (0,144,225)
pantalla.fill(Negro)

# cargar imajen
# mario = pygame.image.load("assets/images/mario03.png").convert()
# ubicar majen 
# pantalla.blit(mario, (5,5))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip


