from modelos.ClassPersona import Persona
from bd.ClassArchivos import archivo_clientes
class Cliente(Persona):

    def __init__(self):
        super().__init__()
        self.sexo = ""
        self.CURP = ""
        self.telefono = 0
        self.correo = ""
        self.ocupacion = ""
        self.ingreso_mensual = 0
        

    def capturardatos(self):
        super().capturardatos()
        while True:
            self.sexo = input("Sexo (M/F): ").upper()
            if self.sexo == "M" or self.sexo == "F":
                break
            else:
                print("Error: Debe ingresar M o F")

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
        while True:
            self.correo = input("Correo: ")
            if "@" in self.correo and "." in self.correo.split("@")[-1]:
                break
            print("Error: Correo inválido. Debe contener @ y un dominio (ej: usuario@mail.com)")
        self.ocupacion = input("Ocupacion: ")
        while True:
            try:
                self.ingreso_mensual = int(input("Ingresos: "))
                break
            except ValueError:
                print("Error: Debe ingresar un numero")

    def devolverdatos(self):
        return super().devolverdatos() + f",{self.sexo},{self.CURP},{self.telefono},{self.correo},{self.ocupacion},{self.ingreso_mensual}"
