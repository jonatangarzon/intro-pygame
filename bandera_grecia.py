import pygame
import sys


# inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana (proporción sugerida para esta bandera)
ventana = pygame.display.set_mode((450, 270))


# establecer el titulo de la ventana
pygame.display.set_caption("Bandera de Grecia")

# definir colores
azul = (0, 0, 255)
blanco = (255, 255, 255)



# creamos las superficies
s1 = pygame.Surface((450, 30))
s2 = pygame.Surface((450, 30))
s3 = pygame.Surface((450, 30))
s4 = pygame.Surface((450, 30))
s5 = pygame.Surface((450, 30))
s6 = pygame.Surface((450, 30))
s7 = pygame.Surface((450, 30))
s8 = pygame.Surface((450, 30))
s9 = pygame.Surface((450, 30))

# Rellenamos cada franja con su color correspondiente
s1.fill(azul)
s2.fill(blanco)
s3.fill(azul)
s4.fill(blanco)
s5.fill(azul)
s6.fill(blanco)
s7.fill(azul)
s8.fill(blanco)
s9.fill(azul)

# Creamos el cuadro azul de la esquina (el cantón) que mide 150x150
canton = pygame.Surface((150, 150))
canton.fill(azul)

# Creamos las partes de la cruz blanca
cruz_v = pygame.Surface((30, 150)) # Brazo vertical
cruz_h = pygame.Surface((150, 30)) # Brazo horizontal
cruz_v.fill(blanco)
cruz_h.fill(blanco)

# Agregar las franjas a la ventana (una debajo de la otra cada 30px)
ventana.blit(s1, (0, 0))
ventana.blit(s2, (0, 30))
ventana.blit(s3, (0, 60))
ventana.blit(s4, (0, 90))
ventana.blit(s5, (0, 120))
ventana.blit(s6, (0, 150))
ventana.blit(s7, (0, 180))
ventana.blit(s8, (0, 210))
ventana.blit(s9, (0, 240))

# Agregar el cantón y la cruz encima
ventana.blit(canton, (0, 0))
ventana.blit(cruz_v, (60, 0))  # Centrado en el cantón
ventana.blit(cruz_h, (0, 60))  # Centrado en el cantón

# Actualizar visualizacion de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

# importamos la libreria pygame
import pygame
import sys

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Rebotes rectángulo")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)

# variable de movimiento
XX = 300
MOVIMIENTO = 3

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    # movimiento del rectángulo
    XX = XX + MOVIMIENTO

    if XX >= 320:
        XX = 320
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    # dibujar rectangulo en ventana
    pygame.draw.rect(ventana, rojo, (XX,100,80,80))

    # actualizar visualización de la ventana
    pygame.display.flip()