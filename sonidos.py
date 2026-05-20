import pygame
import sys

# inicializar modulos 
pygame.init()
pygame.mixer.init()

# colores
Blanco = pygame.Color(255,255,255)

# ventana
pantalla = pygame.display.set_mode((400,400))
pantalla.fill(Blanco)
pygame.display.set_caption("sonidos en pygame")

# variables auxiliares
continuar = True

# sonido de fondo
SILBATO = pygame.mixer.music.load("assets/sounds/silbato.ogg")
pygame.mixer.music.play(1,0.0)

# efectos de sonido
GALLO = pygame.mixer.Sound("assets/sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("assets/sounds/cuervo.ogg")
BICI = pygame.mixer.Sound("assets/sounds/timbre.ogg")

#------------------
#  Bucle deljuego
#-------------------

while continuar:
    for event in pygame.event.get():
        # cerrar ventana si hace clik en el botan de cerrar
        if event.type == pygame.QUIT:
            continuar = False
        # deteactar si se oprime una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                contiuar = False
            elif event.key == pygame.K_o:
                GALLO.play()
            elif event.key == pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_v:
                BICI.play()

pygame.display.flip()





