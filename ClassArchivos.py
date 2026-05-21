import os

class ArchivosCSV:

    def __init__(self, archivo, encabezado):
        self.archivo = archivo
        self.encabezado = encabezado

        
        if not os.path.exists(archivo):
            self.__reiniciarArchivo__()
           
    def leerDatos(self):
        datos = []
        try:
            with open(self.archivo, "r") as a:
                for linea in a:
                    if linea.strip() != self.encabezado:
                        datos.append(linea.strip())
        except FileNotFoundError:
            return datos
        return datos
    
    def devolverencabezados(self):
        return self.encabezado.split(",")

    def agregar(self, dato):
        datos = self.leerDatos()
        siguiente = len(datos) + 1
        try:
            with open(self.archivo, "a") as a:
                a.write(f"{siguiente},{dato}\n")
        except FileNotFoundError:
            print("Archivo no encontrado")

    def sobreescribir(self, renglones):
        try:
            with open(self.archivo, "w") as a:
                a.write(self.encabezado + "\n")
                for i, renglon in enumerate(renglones):
                    
                    partes = renglon.split(",", 1) 
                    if len(partes) > 1:
                        dato_sin_id = partes[1] 
                    else:
                        dato_sin_id = partes[0]
                    a.write(f"{i + 1},{dato_sin_id}\n")
        except PermissionError:
            print("Error: El archivo está siendo usado por otro programa.")
            print("Cierra el archivo CSV si lo tienes abierto en VS Code o Excel e intenta de nuevo.")

    def eliminar(self, indice):
        renglones = self.leerDatos()
        if 0 <= indice < len(renglones):
            renglones.pop(indice)
            self.sobreescribir(renglones)
            return True
        else:
            print("Índice fuera de rango")
            return False

    def modificar(self, indice, nuevo_dato):
        renglones = self.leerDatos()
        if 0 <= indice < len(renglones):

            renglones[indice] = f"{indice + 1},{nuevo_dato}"
            self.sobreescribir(renglones)
            return True
        else:
            print("Índice fuera de rango")
            return False

    def __reiniciarArchivo__(self):
        with open(self.archivo, "w") as a:
            a.write(self.encabezado + "\n")

    
    


carpeta_script = os.path.dirname(os.path.abspath(__file__))
carpeta_datos = os.path.join(carpeta_script, "Datos(Aseguradora)")
os.makedirs(carpeta_datos, exist_ok=True)

archivo_clientes = ArchivosCSV(os.path.join(carpeta_datos, "Clientes.csv"), 
    "ID,Nombre,Apellidos,FechaDeNacimiento,Sexo,CURP,Télefono,Correo,Ocupación,Ingreso"
)

archivo_poliza = ArchivosCSV(os.path.join(carpeta_datos, "poliza.csv"),
    "ID,NúmeroPoliza,FechaInicio,FechaFin,PrimaMensual,SumaAsegurada,TipoPoliza,Estatus,ClienteAsignado"
)

archivo_beneficiarios = ArchivosCSV(os.path.join(carpeta_datos, "beneficiario.csv"),
    "ID,Nombre,Apellidos,FechaDeNacimiento,Parentesco,PorcentajeAsignado,PolizaAsignada"
)

archivo_pagos = ArchivosCSV(os.path.join(carpeta_datos, "pagos.csv"), 
    "ID,FechaPago,MontoPagado,MetodoPago,Referencia,PolizaAsignada"
)

archivo_siniestro = ArchivosCSV(os.path.join(carpeta_datos, "siniestro.csv"),
    "ID,FechaReporte,FechaOcurrencia,TipoSiniestro,MontoReclamado,MontoAprobado,EstatusSiniestro,PolizaAsignada"
)
