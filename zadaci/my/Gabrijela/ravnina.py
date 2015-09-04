import math

class Tocka:
    """
    Opis ove klase
    
    2-dim točke u ravnini
    """
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return "Tocka x= {0}, y={1}".format(self.x,self.y)
    
    class Vektor(Tocka):
        def __add__(self,b):
            x=self.x + b.x
            y=self.y + b.y
            return Vektor (x,y)
    
    def __repr__(self):
        return "Vektor({0}, {1}".format(self.x, self.y)
    