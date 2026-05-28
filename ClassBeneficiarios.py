from ClassPersona import Persona
from ClassArchivos import archivo_beneficiarios,archivo_poliza
class Beneficiario(Persona):

    def __init__(self):
        self.id = 0
        super().__init__()
        self.parentesco = ""
        self.porcentaje_asignado = 0
        self.id_poliza = None

    def capturardatos(self):
        self.id += 1
        super().capturardatos()
        self.parentesco = input("Parentesco: ")
        while True:
            self.porcentaje_asignado = int(input("Porcentaje: "))
            if self.porcentaje_asignado > 100:
                print("Error: El porcentaje no puede ser mayor a 100")
            else:
                break
        while True:
            self.id_poliza = int(input("¿A qué número de póliza pertenece?"))
            listapoliza = archivo_poliza.leerDatos()
            for renglon in listapoliza:
                datos = renglon.split(",")
                if datos[1].strip() == str(self.id_poliza):
                    break
            else:
                print("Error: La póliza no existe")
                self.id_poliza = int(input("¿A qué número de póliza pertenece?"))

            suma_beneficiarios = 0
            listabeneficiarios = archivo_beneficiarios.leerDatos()
            for renglon in listabeneficiarios:
                datos = renglon.split(",")
                if datos[6].strip() == str(self.id_poliza):
                    suma_beneficiarios += int(datos[5])
            if suma_beneficiarios + self.porcentaje_asignado > 100:
                print("Error: La suma de los porcentajes no puede superar el 100% para esta póliza")
                self.porcentaje_asignado = int(input("Porcentaje: "))
            else:
                print("Quedan",100 - suma_beneficiarios - self.porcentaje_asignado, "por asignar.")
                break
            

    def devolverdatos(self):
        return super().devolverdatos() + f", {self.parentesco}, {self.porcentaje_asignado}, {self.id_poliza}"

