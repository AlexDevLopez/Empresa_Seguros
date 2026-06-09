
from modelos.ClassAseguradora import Aseguradora
from abc import abstractmethod
class Transaccion(Aseguradora):

    def __init__(self):
        pass
        
    @abstractmethod
    def procesar(self):
        pass