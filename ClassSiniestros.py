from datetime import datetime
from ClassTransaccion import Transaccion
from ClassArchivos import archivo_siniestro
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
        return f"{self.id}, {self.fecha_reporte.strftime('%d/%m/%Y')}, {self.fecha_ocurrencia.strftime('%d/%m/%Y')}, {self.tipo_siniestro}, {self.monto_reclamado}, {self.monto_aprobado}, {self.estatus_siniestro}, {self.id_poliza}"

    def procesar(self):
        if self.monto_reclamado <= 0:
            print("Error: El monto reclamado debe ser mayor a 0")
            return False
        if self.monto_aprobado > self.monto_reclamado:
            print("Error: El monto aprobado debe ser menor o igual al reclamado")
            return False
        print("Siniestro procesado con éxito")
        return True

def agregar_siniestro():
    osiniestro = Siniestro()
    osiniestro.capturardatos()
    archivo_siniestro.agregar(osiniestro.devolverdatos())
    print("Siniestro Guardado con éxito")
def listar_siniestro():
    renglones = archivo_siniestro.leerDatos()
    if renglones:
        for i,renglon in enumerate(renglones):
            datos = renglon.split(",")
            print(f"--- Siniestros {i + 1}. ---")
            print(f"ID: {datos[0]}")
            print(f"Fecha de Reporte: {datos[1]}")
            print(f"Fecha de Ocurrencia: {datos[2]}")
            print(f"Tipo de Siniestro: {datos[3]}")
            print(f"Monto Reclamado: {datos[4]}")
            print(f"Monto Aprobado: {datos[5]}")
            print(f"Estatus Siniestro: {datos[6]}")
            print(f"Poliza ID: {datos[7]}")
    else:
        print("No hay siniestros registrados")
            
def modificar_siniestro():
    listar_siniestro()
    msiniestro = Siniestro()
    try:    
        num = int(input("¿Qué número de siniestro quieres modificar?: ")) - 1
        msiniestro.capturardatos()
        exito = archivo_siniestro.modificar(num,msiniestro.devolverdatos())
        if exito:
            print("Siniestro modificado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un siniestro existente y el formato correcto.")

def borrar_siniestro():
    listar_siniestro()
    try:    
        num = int(input("¿Qué número de siniestro quieres borrar?: ")) - 1
        exito = archivo_siniestro.eliminar(num)
        if exito:
            print("Siniestro eliminado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un siniestro existente y el formato correcto.")
