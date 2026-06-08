from abc import ABC, abstractmethod

class Aseguradora(ABC):
    @abstractmethod
    def capturardatos(self):
        pass
    @abstractmethod
    def devolverdatos(self):
        pass
    