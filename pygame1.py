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

def gestionar_teclas(teclas):   #Funcion para gestionar las teclas que controlaran al personaje
    if teclas[pygame.K_w]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.y -= cubo.velocidad    # Si "w" es presionada resta la posision de y. Resta 1 que es la velocidad
    if teclas[pygame.K_s]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.y += cubo.velocidad    # Si "s" es presionada suma la posision de y. Suma 1 que es la velocidad
    if teclas[pygame.K_a]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.x -= cubo.velocidad    # Si "a" es presionada resta la posision de x. Resta 1 que es la velocidad
    if teclas[pygame.K_d]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.x += cubo.velocidad    # Si "d" es presionada suma la posision de x. Suma 1 que es la velocidad


while juagando:
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()   # Esto devolvera una lista con todas las teclas que sean presionadas
                    #"key es para acceder a todo lo que tenga que ver con el teclado"
    gestionar_teclas(teclas)    # Llamada a la funcion


    for evento in eventos:
        if evento.type == pygame.QUIT:
            juagando = False

    cubo.dibujar(VENTANA)

    pygame.display.update()

quit() # Cerrar el programa
