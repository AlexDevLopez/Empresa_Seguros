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
        self.ingreso_mensual = int(input("Ingresos: "))

    def devolverdatos(self):
        return super().devolverdatos() + f",{self.sexo},{self.CURP},{self.telefono},{self.correo},{self.ocupacion},{self.ingreso_mensual}"

def agregar_cliente():
    ocliente = Cliente()
    ocliente.capturardatos()
    archivo_clientes.agregar(ocliente.devolverdatos())
    print("Cliente Guardado con éxito")
def listar_cliente():
    renglones = archivo_clientes.leerDatos()
    if renglones:
        for i,renglon in enumerate(renglones):
            datos = renglon.split(",")
            print(f"--- Cliente {i + 1}. ---")
            print(f"ID: {datos[0]}")
            print(f"Nombre: {datos[1]}")
            print(f"Apellido: {datos[2]}")
            print(f"Fecha de Nacimiento: {datos[3]}")
            print(f"Sexo: {datos[4]}")
            print(f"CURP: {datos[5]}")
            print(f"Teléfono: {datos[6]}")
            print(f"Correo: {datos[7]}")
            print(f"Ocupacion: {datos[8]}")
            print(f"IngresoMensual: {datos[9]}")
            print("\n ------------")
    else:
        print("No hay clientes registrados")
def modificar_cliente():
    listar_cliente()
    cliente_modificado = Cliente()
    try:
        num = int(input("¿Qué número de cliente quieres modificar?: ")) - 1
        cliente_modificado.capturardatos()
        exito = archivo_clientes.modificar(num,cliente_modificado.devolverdatos())
        if exito:
            print("Cliente modificado con éxito")
    except ValueError:
        print("¡Error! Debe ingresar un cliente existente y el formato correcto.")
def borrar_cliente():
    listar_cliente()
    try:
        num = int(input("¿Qué número de cliente quieres borrar?: ")) - 1
        exito = archivo_clientes.eliminar(num)

        if exito:
            print("Cliente eliminado con éxito.")
    except ValueError:
        print("¡Error! Debe ingresar un cliente existente y el formato correcto.")