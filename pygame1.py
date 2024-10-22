# Dia @: 
#imports
import pygame
from personaje import Cubo
from enemigo import Enemigo
import random

ANCHO = 1000    # Ancho de la ventana
ALTO = 800      # Alto de la ventana
VENTANA = pygame.display.set_mode([ANCHO,ALTO]) # Ventana principal con un arreglo como parametros
FPS = 60 # Creamos la variable de FPs para que el juego valla igual en todos los ordenadores sin importar la potencia

# Variables
juagando = True
reloj = pygame.time.Clock() # Se crea un reloj
tiempo_pasado = 0   # Inicializamos timpo pasado en 0
tiempo_entre_enemigos = 500 # Teimpo entre enemigos, dia 5 aun no se utiliza

cubo = Cubo(ANCHO/2,ALTO-75)#   Dibujara el personaje en la ventana principal
enemigos = []   #Lista de enemigos que apareceran por panatalla

enemigos.append(Enemigo(ANCHO/2,100))   # Test de colocar un enemigo en la VENTANA principal
                                        # Se reajustaron las coordenas de personaje cubo para que aparesca hasta abajo del todo



def gestionar_teclas(teclas):   #Funcion para gestionar las teclas que controlaran al personaje
    ## Se documentaron teclas para evitar que la nave se mueva en el eje y

    # if teclas[pygame.K_w]:  # Detecta si la tecla deleccionada esta siendo presionada
    #     cubo.y -= cubo.velocidad    # Si "w" es presionada resta la posision de y. Resta 1 que es la velocidad
    # if teclas[pygame.K_s]:  # Detecta si la tecla deleccionada esta siendo presionada
    #     cubo.y += cubo.velocidad    # Si "s" es presionada suma la posision de y. Suma 1 que es la velocidad
    if teclas[pygame.K_a]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.x -= cubo.velocidad    # Si "a" es presionada resta la posision de x. Resta 1 que es la velocidad
    if teclas[pygame.K_d]:  # Detecta si la tecla deleccionada esta siendo presionada
        cubo.x += cubo.velocidad    # Si "d" es presionada suma la posision de x. Suma 1 que es la velocidad

# Ciclo principal
while juagando:
    tiempo_pasado += reloj.tick(FPS)    # Tiempo en el cual el juego esta corriendo
    #print(tiempo_pasado)    # Test del timpo pasado

    if tiempo_pasado > tiempo_entre_enemigos:   # Condicional para agregar enemigos
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))  # Se agregan enemigosn en coordenas X aleatorias
        tiempo_pasado = 0   # Se recetea el tiempo para que no aparescan demasiados enemigos a la vez debdo al condicional if

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()   # Esto devolvera una lista con todas las teclas que sean presionadas
                    #"key es para acceder a todo lo que tenga que ver con el teclado"
    gestionar_teclas(teclas)    # Llamada a la funcion


    for evento in eventos:
        if evento.type == pygame.QUIT:
            juagando = False
    
    VENTANA.fill("black")   # Rellenara de color cada por cada vuelta en el bucle principal.
                            # Ya que si no se realiza el perosonaje aparecera en toda la pantalla.Parecido al paint
    cubo.dibujar(VENTANA)
    
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()    #Llamada  ala funcion moviento par aque enemigo se mueva por si mismo

    pygame.display.update()

quit() # Cerrar el programa
