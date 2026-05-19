
from ClassAseguradora import Aseguradora
from abc import abstractmethod
class Transaccion(Aseguradora):

    def __init__(self):
        self.id = 0
        self.poliza = None
        
    @abstractmethod
    def procesar(self):
        pass