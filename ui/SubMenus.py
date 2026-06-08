from modelos.ClassPoliza import Poliza
from modelos.ClassBeneficiarios import Beneficiario
from modelos.ClassPagos import Pagos
from modelos.ClassSiniestros import Siniestro
from modelos.ClassCliente import Cliente
from bd.ClassMySql import archivo_clientes,archivo_poliza,archivo_beneficiarios,archivo_pagos,archivo_siniestro
from bd.CRUDGenerico import Agregar_generico,Listar_generico,Modificar_generico,Borrar_generico

# Refactorización

def menu_generico(titulo, Clase, archivo, nombre):
    while True:
        print(f"\n--- Menú {titulo} ---")
        print("1. ➕ Agregar")
        print("2. 📜 Listar")
        print("3. 🔃 Modificar")
        print("4. 🗑️  Borrar")
        print("5. ◀️  Regresar")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                Agregar_generico(Clase,archivo,nombre)
            elif opcion == 2:
                Listar_generico(archivo,nombre)
            elif opcion == 3:
                Modificar_generico(Clase,archivo,nombre)
            elif opcion == 4:
                Borrar_generico(archivo,nombre)
            elif opcion == 5:
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")

def menu_Clientes():
    menu_generico(
        "Clientes", Cliente, archivo_clientes, "Cliente"
    )

def menu_Poliza():
    menu_generico(
        "Pólizas", Poliza, archivo_poliza, "Póliza"
    )

def menu_Beneficiarios():
    menu_generico(
        "Beneficiarios", Beneficiario, archivo_beneficiarios, "Beneficiario"
    )

def menu_Pagos():
    menu_generico(
        "Pagos", Pagos, archivo_pagos, "Pago"
    )

def menu_Siniestros():
    menu_generico(
        "Siniestros", Siniestro, archivo_siniestro, "Siniestro"
    )

