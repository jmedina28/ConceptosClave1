from re import X


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
   
x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))

print(Punto(x1,y1).pantalla())
print(Punto(x1,y1).cuadrante())

x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de x2: "))

print(Punto(x2,y2).pantalla())
print(Punto(x2,y2).cuadrante())

print("El vector que forman los dos puntos es el siguiente: " + str(Punto(x1,y1).vector(Punto(x2,y2)).pantalla()))
print("La distancia entre los dos puntos es de: " + str(Punto(x1,y1).distancia(Punto(x2,y2))))

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def area(self):
        return abs(self.punto1.x - self.punto2.x) * abs(self.punto1.y - self.punto2.y)
    
    def base(self):
        return abs(self.punto1.x - self.punto2.x)
    
    def altura(self):
        return abs(self.punto1.y - self.punto2.y)

x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de x2: ")) 
print("El área del rectángulo es: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).area()))
print("La base del rectángulo mide: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).base()))
print("La altura del rectángulo mide: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).altura()))