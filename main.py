
from plano import Punto, Rectangulo

x1 = 0
y1 = 0
print(Punto(x1,y1).pantalla())
print(Punto(x1,y1).cuadrante())
x2 = 5
y2 = 5
print(Punto(x2,y2).pantalla())
print(Punto(x2,y2).cuadrante())
print("El vector que forman los dos puntos es el siguiente: " + str(Punto(x1,y1).vector(Punto(x2,y2)).pantalla()))
print("La distancia entre los dos puntos es de: " + str(Punto(x1,y1).distancia(Punto(x2,y2))))

x1 = 0
y1 = 0
print(Punto(x1,y1).pantalla())
x2 = 5
y2 = 5
print(Punto(x2,y2).pantalla())
print("El área del rectángulo es: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).area()))
print("La base del rectángulo mide: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).base()))
print("La altura del rectángulo mide: " + str(Rectangulo(Punto(x1,y1), Punto(x2,y2)).altura()))
print("*" * 50)
# Experimentación
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)
print(A.pantalla()), print(A.cuadrante())
print(B.pantalla()), print(B.cuadrante())
print(C.pantalla()), print(C.cuadrante())
print(D.pantalla()), print(D.cuadrante())
print("El vector AB es el siguiente: " + str(B.vector(A).pantalla()))
print("El vector BA es el siguiente: " + str(A.vector(B).pantalla()))
print("La distancia entre A y B es de: " + str(A.distancia(B)))
print("La distancia entre B y A es de: " + str(B.distancia(A)))
# Rectángulo con vértices A y B
print("El área del rectángulo que forma la diagonal AB es la siguiente: " + str(Rectangulo(A, B).area()))
