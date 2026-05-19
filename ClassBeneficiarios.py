from ClassPersona import Persona
from ClassArchivos import archivo_beneficiarios
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
        self.porcentaje_asignado = int(input("Porcentaje: "))
        self.id_poliza = int(input("¿A qué número de póliza pertenece?"))
    def devolverdatos(self):
        return super().devolverdatos() + f", {self.parentesco}, {self.porcentaje_asignado}, {self.id_poliza}"

def agregar_beneficiario():
    obeneficiario = Beneficiario()
    obeneficiario.capturardatos()
    archivo_beneficiarios.agregar(obeneficiario.devolverdatos())
    print("Beneficiario Guardado con éxito")
def listar_beneficiario():
    renglones = archivo_beneficiarios.leerDatos()
    if renglones:
        for i,renglon in enumerate(renglones):
            datos = renglon.split(",")
            print(f"--- Beneficiarios {i + 1}. ---")
            print(f"ID: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Apellidos: {datos[2]}")
            print(f"Fecha de Naciemiento: {datos[3]}")
            print(f"Parentezco: {datos[4]}")
            print(f"Porcentaje Asignado: {datos[5]}")
            print(f"Póliza ID: {datos[6]}")
    else:
        print("No hay beneficiarios registrados")
def modificar_beneficiario():
    listar_beneficiario()
    mbeneficiario = Beneficiario()
    try:
        num = int(input("¿Qué número de beneficiario quieres modificar?: ")) - 1
        mbeneficiario.capturardatos()
        exito = archivo_beneficiarios.modificar(num,mbeneficiario.devolverdatos())
        if exito:
            print("Beneficiario modificado con éxito")
    except ValueError:
        print("¡Erorr! Debe ingresar un beneficiario existente y el formato correcto")
def borrar_beneficiario():
    listar_beneficiario()
    try:
        num = int(input("¿Qué número de beneficiario quieres eliminar?: ")) - 1
        exito = archivo_beneficiarios.eliminar(num)
        if exito:
            print("Beneficiario eliminado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un beneficiario existente y el formato correcto")

    

