#imports
import pygame

class Cubo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10 # Auentamos la velocidad debido al cambio en FPS
        self.color = "red"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Forma de crear el personaje
        self.imagen = pygame.image.load("GameSpacecraft\\nave1.png")
        self.imagen=pygame.transform.scale(self.imagen,(self.ancho,self.alto))
# Funcion que dibujara el personaje
    def dibujar(self, ventana):
        #pygame.draw.rect(ventana,self.color,self.rect) #! Se comenta para que solo apresca la nave pero sigue estando ahi
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Cambiara las coordenadas de perosonaje cada vez que sea dibujado
        ventana.blit(self.imagen,(self.x, self.y))