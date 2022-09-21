class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def punto(self):
        return (self.x, self.y)

    def pantalla(self):
        return "({0},{1})".format(self.x, self.y)
    
    def cuadrante(self):
  
        if self.x == 0:
            return "El punto se encuentra sobre el eje x."
        elif self.y == 0:
            return "El punto se encuentra sobre el eje y."
        elif self.x > 0 and self.y > 0:
            return "El punto se encuentra en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto se encuentra en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto se encuentra en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto se encuentra en el cuarto cuadrante."
        else:
            return "El punto se encuentra en el origen de coordenadas."

    def vector(self, punto):
        return Punto(self.x - punto.x, self.y - punto.y)
    
    def distancia(self, punto):
        return ((self.x - punto.x)**2 + (self.y - punto.y)**2)**0.5

print(Punto(1,2).pantalla())
print(Punto(1,2).cuadrante())
print(Punto(1,2).vector(Punto(3,4)).pantalla())
print(Punto(1,1).distancia(Punto(5,1)))
class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def area(self):
        return abs(self.punto1.x - self.punto2.x) * abs(self.punto1.y - self.punto2.y)

print(Rectangulo(Punto(1,1), Punto(5,5)).area())