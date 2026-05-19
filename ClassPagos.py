from ClassPoliza import Poliza
from ClassTransaccion import Transaccion
from ClassArchivos import archivo_pagos
class Pagos(Transaccion):

    def __init__(self):
        self.id = 0
        self.fecha_pago = ""
        self.monto_pagado = 0
        self.metodo_pago = ""
        self.referencia = ""
        self.id_poliza = 0

    def capturardatos(self):
        self.id += 1 
        self.fecha_pago = input("Fecha del Pago: ")
        self.monto_pagado = int(input("Monto Pagado: "))
        self.metodo_pago = input("Método de Pago: ")
        self.referencia = (input("Referencia: "))
        self.id_poliza = input("¿A qué número de póliza pertenece?")
    def devolverdatos(self):
        return f"{self.fecha_pago}, {self.monto_pagado}, {self.metodo_pago}, {self.referencia}, {self.id_poliza}"

    def procesar(self):
        if self.monto_pagado <= 0:
            print("Error: El monto debe ser mayor a 0")
            return False
        if int(self.id_poliza) <= 0:
            print("Error: Debe indicar una póliza válida")
            return False
        print("Pago procesado con éxito")
        return True

def agregar_pago():
    opago = Pagos()
    opago.capturardatos()
    archivo_pagos.agregar(opago.devolverdatos())
    print("Pago Guardado con éxito")
def listar_pago():
    renglones = archivo_pagos.leerDatos()
    if renglones:
        for i,renglon in enumerate(renglones):
            datos = renglon.split(",")
            print(f"--- Pagos {i + 1}. ---")
            print(f"ID: {datos[0]}")
            print(f"Fecha de Pago: {datos[1]}")
            print(f"Monto Pagado: {datos[2]}")
            print(f"Metodo de Pago: {datos[3]}")
            print(f"Referencia: {datos[4]}")
            print(f"Póliza ID: {datos[5]}")
    else:
        print("No hay pagos registrados")
def modificar_pago():
    listar_pago()
    mpago = Pagos()
    try:
        num = int(input("¿Qué número de pago quieres modificar?: ")) - 1
        mpago.capturardatos()
        exito = archivo_pagos.modificar(num,mpago.devolverdatos())
        if exito:
            print("Pago modificado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un pago existente y el formato correcto.")


def borrar_pagos():
    listar_pago()
    try:
        num = int(input("¿Qué número de pago quieres borrar?: ")) - 1
        exito = archivo_pagos.eliminar(num)
        if exito:
            print("Pago eliminado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un pago existente y el formato correcto.")

o = Pagos()
o.procesar()