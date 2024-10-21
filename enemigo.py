# La clase enemigo es una replica hasta el momento de personaje.py
# con la diferencia de sus caracteristicas visuales
# y uan nueva funcion de moviemieno
#imports
import pygame

class Enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 75
        self.alto = 75
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Forma de crear el personaje

    def dibujar(self, ventana):
        pygame.draw.rect(ventana,self.color,self.rect)
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Cambiara las coordenadas de enemigo cada vez que sea dibujado

    def movimiento(self):   # funcion de miviento que permitira que el personaje se mueva automaticamente 
        self.y += self.velocidad        # Para que la funcion duncione debe ser agregada a pygame1