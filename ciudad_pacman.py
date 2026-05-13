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
cafe = (65,57,56)


# bucle principal del juego
while True:

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # rectangulo
    pygame.draw.rect(ventana, azul, (150,150,50,50))
    pygame.draw.rect(ventana, rojo, (200,100,150,50))
    pygame.draw.rect(ventana, naranja, (350,150,50,50))
    pygame.draw.rect(ventana, amarillo, (150,200,50,50))
    pygame.draw.rect(ventana, cian, (350,200,50,50))
    pygame.draw.rect(ventana, rosado, (150,250,50,50))
    pygame.draw.rect(ventana, verde, (350,250,50,50))
    pygame.draw.rect(ventana, blanco, (200,300,150,50))
    pygame.draw.line(ventana, rojo, (280,350), (500,700), 6)
    pygame.draw.line(ventana, rojo, (280,350), (100,700), 6)
    pygame.draw.rect(ventana, blanco, (650,200,50,50))
    pygame.draw.rect(ventana, blanco, (650,250,50,50))
    pygame.draw.rect(ventana, blanco, (650,300,50,50))
    pygame.draw.rect(ventana, blanco, (650,350,50,200))
    pygame.draw.rect(ventana, blanco, (650,500,300,50))
    pygame.draw.rect(ventana, blanco, (650,200,300,50))
    pygame.draw.rect(ventana, blanco, (900,250,50,200))
    pygame.draw.rect(ventana, cafe, (900,450,50,50))

# texto
    fuente_arial = pygame.font.SysFont("Atial", 35, 1, 1)
    texto = fuente_arial.render("Siudad de los pacmas",1, blanco)
    ventana.blit(texto, (0,50))

    fuente_arial = pygame.font.SysFont("Atial", 100, 1, 600)
    texto = fuente_arial.render("tienda",1, azul)
    ventana.blit(texto, (700,70))


    # actualizar visualización de la ventana
    pygame.display.flip()