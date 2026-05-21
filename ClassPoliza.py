from datetime import datetime
from ClassAseguradora import Aseguradora
from ClassArchivos import archivo_poliza
class Poliza(Aseguradora):

    def __init__(self):
        self.id = 0
        self.numero_poliza = 0
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.prima_mensual = 0
        self.suma_asegurada = 0
        self.tipo_poliza = ""
        self.estatus = ""
        self.id_cliente = 0

    def capturardatos(self):
        self.id += 1 
        self.numero_poliza = int(input("Número de  Póliza: "))
        self.fecha_inicio = datetime.strptime(input("Fecha de Inicio (DD/MM/YYYY): "), "%d/%m/%Y")
        self.fecha_fin = datetime.strptime(input("Fecha de Fin (DD/MM/YYYY): "), "%d/%m/%Y")
        while self.fecha_inicio >= self.fecha_fin:
            print("Error: Las fechas no pueden ser iguales o la fecha de inicio debe ser menor a la fecha de fin")
            self.fecha_inicio = datetime.strptime(input("Fecha de Inicio (DD/MM/YYYY): "), "%d/%m/%Y")
            self.fecha_fin = datetime.strptime(input("Fecha de Fin (DD/MM/YYYY): "), "%d/%m/%Y")
        self.prima_mensual = float(input("Prima Mensual: "))
        while self.prima_mensual <= 0:
            print("Error: La prima mensual debe ser mayor a 0")
            self.prima_mensual = float(input("Prima Mensual: "))
        self.suma_asegurada = float(input("Suma Asegurada: "))
        self.tipo_poliza = input("Tipo de Póliza: ")
        self.estatus = input("Estatus: ")
        self.id_cliente = int(input("¿A qué ID de cliente pertenece esta póliza?: "))
    def devolverdatos(self):
        return f"{self.numero_poliza}, {self.fecha_inicio}, {self.fecha_fin}, {self.prima_mensual}, {self.suma_asegurada}, {self.tipo_poliza}, {self.estatus}, {self.id_cliente}"
