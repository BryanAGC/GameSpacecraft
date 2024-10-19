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

def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y == cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_w]:
        cubo.x += cubo.velocidad


while juagando:
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)


    for evento in eventos:
        if evento.type == pygame.QUIT:
            juagando = False

    cubo.dibujar(VENTANA)

    pygame.display.update()

quit() # Cerrar el programa
