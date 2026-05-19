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
        self.fecha_reporte = input("Fecha del Reporte: ")
        self.fecha_ocurrencia = input("Fecha de Ocurrencia: ")
        self.tipo_siniestro = input("Tipo de Siniestro: ")
        self.monto_reclamado = int(input("Monto Reclamado: "))
        self.monto_aprobado = int(input("Monto Aprobado: "))
        self.estatus_siniestro = input("Estatus: ")
        self.id_poliza = int(input("¿A qué número de póliza pertenece?"))

    def devolverdatos(self):
        return f"{self.fecha_reporte}, {self.fecha_ocurrencia}, {self.tipo_siniestro}, {self.monto_reclamado}, {self.monto_aprobado}, {self.estatus_siniestro}, {self.id_poliza}"

    def procesar(self):
        if self.monto_reclamado <= 0:
            print("Error: El monto reclamado debe ser mayor a 0")
            return False
        if self.monto_aprobado > self.monto_reclamado:
            print("Error: El monto aprobado no puede ser mayor al reclamado")
            return False
        if self.monto_aprobado < 0:
            print("Error: El monto aprobado no puede ser negativo")
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
