# Dia @: 
#imports
import pygame
from personaje import Cubo
ANCHO = 1000    # Ancho de la ventana
ALTO = 800      # Alto de la ventana
VENTANA = pygame.display.set_mode([ANCHO,ALTO]) # Ventana principal con un arreglo como parametros

# Bucle principal del juego
juagando = True

cubo = Cubo(100,100)#   Dibujara el personaje en la ventana principal

while juagando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            juagando = False

    cubo.dibujar(VENTANA)

    pygame.display.update()

quit() # Cerrar el programa
