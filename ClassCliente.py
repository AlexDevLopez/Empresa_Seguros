from ClassPersona import Persona
from ClassArchivos import archivo_clientes
class Cliente(Persona):

    def __init__(self):
        self.id = 0
        super().__init__()
        self.sexo = ""
        self.CURP = ""
        self.telefono = 0
        self.correo = ""
        self.ocupacion = ""
        self.ingreso_mensual = 0
        

    def capturardatos(self):
        self.id += 1
        super().capturardatos()
        self.sexo = input("Sexo: ")
        self.CURP = input("Curp: ")
        while True:
            listacliente = archivo_clientes.leerDatos()
            for renglon in listacliente:
                datos = renglon.split(",")
                if datos[5].strip() == self.CURP:
                    print("Error: La CURP ya existe")
                    self.CURP = input("Curp: ")
                    break
            else:
                break
        self.telefono = (input("Telefono: "))
        while len(self.telefono) != 10:
            print("Error: El telefono debe tener 10 digitos")
            self.telefono = (input("Telefono: "))
        self.correo = input("Correo: ")
        self.ocupacion = input("Ocupacion: ")
        while True:
            try:
                self.ingreso_mensual = int(input("Ingresos: "))
                break
            except ValueError:
                print("Error: Debe ingresar un numero")

    def devolverdatos(self):
        return super().devolverdatos() + f",{self.sexo},{self.CURP},{self.telefono},{self.correo},{self.ocupacion},{self.ingreso_mensual}"
