#imports
import pygame

class Enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = .33
        self.color = "purple"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) 

    def dibujar(self, ventana):
        pygame.draw.rect(ventana,self.color,self.rect)
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) 
