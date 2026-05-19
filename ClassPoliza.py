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
        self.fecha_inicio = input("Fecha de Inicio: ")
        self.fecha_fin = input("Fecha de Fin: ")
        self.prima_mensual = int(input("Prima Mensual: "))
        self.suma_asegurada = int(input("Suma Asegurada: "))
        self.tipo_poliza = input("Tipo de Póliza: ")
        self.estatus = input("Estatus: ")
        self.id_cliente = int(input("¿A qué ID de cliente pertenece esta póliza?: "))
    def devolverdatos(self):
        return f"{self.numero_poliza}, {self.fecha_inicio}, {self.fecha_fin}, {self.prima_mensual}, {self.suma_asegurada}, {self.tipo_poliza}, {self.estatus}, {self.id_cliente}"

def agregar_poliza():
    opoliza = Poliza()
    opoliza.capturardatos()
    archivo_poliza.agregar(opoliza.devolverdatos())
    print("Póliza Guardada con éxito")
def listar_poliza():
    renglones = archivo_poliza.leerDatos()
    if renglones:
        for i,renglon in enumerate(renglones):
            datos = renglon.split(",")
            print(f"--- Póliza {i + 1}. ---")
            print(f"ID: {datos[0]}")
            print(f"Número de Poliza: {datos[1]}")
            print(f"Fecha de Inicio: {datos[2]}")
            print(f"Fecha Fín: {datos[3]}")
            print(f"Prima Mensual: {datos[4]}")
            print(f"Suma Asegurada: {datos[5]}")
            print(f"Tipo de Poliza: {datos[6]}")
            print(f"Estatus: {datos[7]}")
            print(f"Id del Cliente: {datos[8]}")
    else:
        print("No hay pólizas registradas")
def modificar_poliza():
    listar_poliza()
    poliza_modificada = Poliza()
    try:
        num = int(input("¿Qué número de póliza quieres modificar?: ")) - 1
        poliza_modificada.capturardatos()
        exito = archivo_poliza.modificar(num,poliza_modificada.devolverdatos())
        if exito:
            print("Póliza modificada con éxito")
    except ValueError:
        print("¡Error! Debe ingresar una Póliza existente y el formato correcto.")
def borrar_poliza():
    listar_poliza()
    try:    
        num = int(input("¿Qué número de póliza quieres borrar?: ")) - 1
        exito = archivo_poliza.eliminar(num)

        if exito:
            print("Póliza eliminada con éxito.")
    except ValueError:
        print("¡Error! Debe ingresar una póliza existente y el formato correcto.")
