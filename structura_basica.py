import pygame


# inicialisamos los modulos de la libreria
pygame.init()

# establecer dimenciones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("pygame Guanenta")

# definir colores
Azul = (0,0,255)
Rojo = (255,0,0)
verde = (0,255,0)
verde_oscuro = (71,98,0)

# creamos una superficie
superficie_1 = pygame.Surface((200,200))
superficie_2 = pygame.Surface((200,200))
superficie_3 = pygame.Surface((200,200))
superficie_4 = pygame.Surface((200,200))

# Rellenamos la superficie de color
superficie_1.fill(Azul)
superficie_2.fill(Rojo)
superficie_3.fill(verde)
superficie_4.fill(verde_oscuro)

# agregar o mover la ventana
ventana.blit(superficie_1, (0,0))
ventana.blit(superficie_2, (200,200))
ventana.blit(superficie_3, (0,200))
ventana.blit(superficie_4, (300,0))

# actualisar visualisacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:

        pygame.quit()