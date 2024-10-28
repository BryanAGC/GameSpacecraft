# La clase bala es una replica hasta el momento de enemigo.py
# con la diferencia de sus caracteristicas visuales
# y uan nueva funcion de moviemieno
#imports
import pygame

class Bala:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 10  
        self.color = "white"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Forma de crear la bala

    def dibujar(self, ventana):
        pygame.draw.rect(ventana,self.color,self.rect)
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Cambiara las coordenadas de la bala cada vez que sea dibujado

    def movimiento(self):   # funcion de miviento que permitira que ela bala se mueva automaticamente 
        self.y -= self.velocidad        # El movimiento ira hacia arriba