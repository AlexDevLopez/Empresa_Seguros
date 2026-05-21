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
