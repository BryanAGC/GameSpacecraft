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
        self.velocidad = 5  # Auentamos la velocidad debido al cambio en FPS
        self.color = "purple"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Forma de crear el personaje
        self.vida = 3
        self.imagen = pygame.image.load("GameSpacecraft\\alien1.png")
        self.imagen=pygame.transform.scale(self.imagen,(self.ancho,self.alto))
    def dibujar(self, ventana):
        # pygame.draw.rect(ventana,self.color,self.rect) #! Para que no salga el cuadrado pero si la imagen
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto) #Cambiara las coordenadas de enemigo cada vez que sea dibujado
        ventana.blit(self.imagen,(self.x, self.y))
        
    def movimiento(self):   # funcion de miviento que permitira que el personaje se mueva automaticamente 
        self.y += self.velocidad        # Para que la funcion duncione debe ser agregada a pygame1