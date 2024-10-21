#imports
import pygame

class Cubo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10
        self.color = "red"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Forma de crear el personaje
# Funcion que dibujara el personaje
    def dibujar(self, ventana):
        pygame.draw.rect(ventana,self.color,self.rect)
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Cambiara las coordenadas de perosonaje cada vez que sea dibujado
