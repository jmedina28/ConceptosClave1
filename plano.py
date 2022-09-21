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
            return "El punto se encuentra sobre el eje x"
        elif self.y == 0:
            return "El punto se encuentra sobre el eje y"
        elif self.x > 0 and self.y > 0:
            return "El punto se encuentra en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto se encuentra en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto se encuentra en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto se encuentra en el cuarto cuadrante"
        else:
            return "El punto se encuentra en el origen"

print(Punto(1,2).pantalla())
print(Punto(1,2).cuadrante())