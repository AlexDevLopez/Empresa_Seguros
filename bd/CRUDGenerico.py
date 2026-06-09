def Agregar_generico(Clase, archivo, nombre):
    os = Clase()
    os.capturardatos()
    archivo.agregar(os.devolverdatos())
    print(f"{nombre} guardado con éxito")


def Listar_generico(archivo, nombre):
    lista = archivo.leerDatos()
    if not lista:
        print(f"No hay {nombre}s registrados")
        return False

    else:
        enca = archivo.devolverencabezados()
        for i, item in enumerate(lista):
            print(f"\n--- {nombre} {i+1} ---")
            datos = item.split(",")
            for k, v in zip(enca, datos):
                print(f"{k}: {v}")
        return True

def Modificar_generico(clase, archivo, nombre):
    if Listar_generico(archivo, nombre):
        clase_modificada = clase()
        try:
            num = int(input("¿Qué número de " + nombre + " quieres modificar?: ")) - 1
            clase_modificada.capturardatos()
            exito = archivo.modificar(num, clase_modificada.devolverdatos())
            if exito:
                print(f"{nombre} modificado con éxito")
                return True
        except ValueError:
            print(f"¡Error! Debe ingresar un {nombre} existente y el formato correcto.")
            return False
        except Exception as e:
            print(f"Error inesperado: {e}")
            return False    
    else:
        print(f"No hay {nombre}s registrados")    
        
def Borrar_generico(archivo, nombre):
    if Listar_generico(archivo, nombre):
        try:
            num = int(input("¿Qué número de " + nombre + " quieres borrar?: ")) - 1
            exito = archivo.eliminar(num)
            if exito:
                print(f"{nombre} eliminado con éxito.")
                return True
        except ValueError:
            print(f"¡Error! Debe ingresar un {nombre} existente y el formato correcto.")
            return False
        except Exception as e:
            print(f"Error inesperado: {e}")   
            return False 
    
