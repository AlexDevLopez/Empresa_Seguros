from datetime import datetime
from ClassTransaccion import Transaccion
class Siniestro(Transaccion):

    def __init__(self):
        self.id = 0
        self.fecha_reporte = ""
        self.fecha_ocurrencia = ""
        self.tipo_siniestro = ""
        self.monto_reclamado = 0
        self.monto_aprobado = 0
        self.estatus_siniestro = ""
        self.poliza = None
    
    def capturardatos(self):
        self.id += 1 
        self.fecha_reporte = datetime.strptime(input("Fecha del Reporte (DD/MM/YYYY): "), "%d/%m/%Y")
        self.fecha_ocurrencia = datetime.strptime(input("Fecha de Ocurrencia (DD/MM/YYYY): "), "%d/%m/%Y")
        while self.fecha_ocurrencia > self.fecha_reporte:
            print("Error: La fecha de ocurrencia debe ser menor o igual a la fecha del reporte")
            self.fecha_reporte = datetime.strptime(input("Fecha del Reporte (DD/MM/YYYY): "), "%d/%m/%Y")
            self.fecha_ocurrencia = datetime.strptime(input("Fecha de Ocurrencia (DD/MM/YYYY): "), "%d/%m/%Y")
        self.tipo_siniestro = input("Tipo de Siniestro: ")
        self.monto_reclamado = float(input("Monto Reclamado: "))
        while self.monto_reclamado <= 0:
            print("Error: El monto reclamado debe ser mayor a 0")
            self.monto_reclamado = float(input("Monto Reclamado: "))
        self.monto_aprobado = float(input("Monto Aprobado: "))
        while self.monto_aprobado > self.monto_reclamado:
            print("Error: El monto aprobado debe ser menor o igual al reclamado")
            self.monto_aprobado = float(input("Monto Aprobado: "))
        self.estatus_siniestro = input("Estatus: ")
        self.id_poliza = int(input("¿A qué número de póliza pertenece?"))

    def devolverdatos(self):
        return f"{self.fecha_reporte.strftime('%Y-%m-%d')}, {self.fecha_ocurrencia.strftime('%Y-%m-%d')}, {self.tipo_siniestro}, {self.monto_reclamado}, {self.monto_aprobado}, {self.estatus_siniestro}, {self.id_poliza}"

    def procesar(self):
        if self.monto_reclamado <= 0:
            print("Error: El monto reclamado debe ser mayor a 0")
            return False
        if self.monto_aprobado > self.monto_reclamado:
            print("Error: El monto aprobado debe ser menor o igual al reclamado")
            return False
        print("Siniestro procesado con éxito")
        return True

