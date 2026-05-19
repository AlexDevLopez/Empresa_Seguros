from ClassAseguradora import Aseguradora
from abc import ABC, abstractmethod
class Persona(Aseguradora, ABC):

    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.fecha_nacimiento = ""

    @abstractmethod
    def capturardatos(self):
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos: ")
        self.fecha_nacimiento = input("Fecha de Nacimiento: ")
    @abstractmethod
    def devolverdatos(self):
        return f"{self.nombre}, {self.apellidos}, {self.fecha_nacimiento}" 
    

def agregar_persona():
    pass
def borrar_persona():
    pass
def modificar_persona():
    pass
def listar_persona():
    pass