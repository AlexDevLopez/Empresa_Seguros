from ClassCliente import agregar_cliente,listar_cliente,modificar_cliente,borrar_cliente
from ClassPoliza import agregar_poliza,listar_poliza,borrar_poliza,modificar_poliza
from ClassBeneficiarios import agregar_beneficiario,listar_beneficiario,modificar_beneficiario,borrar_beneficiario
from ClassPagos import agregar_pago,listar_pago,modificar_pago,borrar_pagos
from ClassSiniestros import agregar_siniestro,listar_siniestro,modificar_siniestro,borrar_siniestro

# Refactorización

def menu_generico(titulo, fn_agregar, fn_listar, fn_modificar, fn_borrar):
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
                fn_agregar()
            elif opcion == 2:
                fn_listar()
            elif opcion == 3:
                fn_modificar()
            elif opcion == 4:
                fn_borrar()
            elif opcion == 5:
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")

def menu_Clientes():
    menu_generico(
        "Clientes",
        agregar_cliente,
        listar_cliente,
        modificar_cliente,
        borrar_cliente,
        "Clientes"
    )

def menu_Poliza():
    menu_generico(
        "Pólizas",
        agregar_poliza,
        listar_poliza,
        modificar_poliza,
        borrar_poliza,
        "Pólizas"
    )

def menu_Beneficiarios():
    menu_generico(
        "Beneficiarios",
        agregar_beneficiario,
        listar_beneficiario,
        modificar_beneficiario,
        borrar_beneficiario,
        "Beneficiarios"
    )

def menu_Pagos():
    menu_generico(
        "Pagos",
        agregar_pago,
        listar_pago,
        modificar_pago,
        borrar_pagos,
        "Pagos"
    )

def menu_Siniestros():
    menu_generico(
        "Siniestros",
        agregar_siniestro,
        listar_siniestro,
        modificar_siniestro,
        borrar_siniestro,
        "Siniestros"
    )

