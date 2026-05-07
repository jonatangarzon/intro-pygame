# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmanans


# importamos la libreria pygame
import pygame
import sys
import math


# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((1000,700))

# establecer titulo de la ventana
pygame.display.set_caption("Dibujar formas básicas")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0,255,255)


# bucle principal del juego
while True:

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # rectangulo
    pygame.draw.rect(ventana, azul, (150,150,50,50))

    # actualizar visualización de la ventana
    pygame.display.flip()