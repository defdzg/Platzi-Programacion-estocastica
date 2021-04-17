import random

class Borracho:
    
    #Nombre del borracho
    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho): 
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    
    
class BorrachoConEstoides(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(-5, 0), (1, -2), (0, 12), (3, 4)])