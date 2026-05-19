from ClassCliente import agregar_cliente,listar_cliente,modificar_cliente,borrar_cliente
from ClassPoliza import agregar_poliza,listar_poliza,borrar_poliza,modificar_poliza
from ClassBeneficiarios import agregar_beneficiario,listar_beneficiario,modificar_beneficiario,borrar_beneficiario
from ClassPagos import agregar_pago,listar_pago,modificar_pago,borrar_pagos
from ClassSiniestros import agregar_siniestro,listar_siniestro,modificar_siniestro,borrar_siniestro

def menu_Clientes():
    while True:
        print("\n --- Menú Clientes ---")
        print("1. ➕ Agregar Cliente")
        print("2. 📜 Listar Clientes")
        print("3. 🔃 Modificar Clientes")
        print("4. 🗑️  Borrar Cliente")
        print("5. ◀️  Regresar al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                agregar_cliente()
            elif opcion == 2:
                listar_cliente()
            elif opcion == 3:
                modificar_cliente()
            elif opcion == 4:
                borrar_cliente()
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")
            
def menu_Poliza():
    while True:
        print("\n --- Menú Pólizas ---")
        print("1. ➕ Agregar Póliza")
        print("2. 📜 Listar Póliza")
        print("3. 🔃 Modificar Póliza")
        print("4. 🗑️  Borrar Póliza")
        print("5. ◀️  Regresar al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                agregar_poliza()
            elif opcion == 2:
                listar_poliza()
            elif opcion == 3:
                modificar_poliza()
            elif opcion == 4:
                borrar_poliza()
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")
        
def menu_Beneficiarios():
    while True:
        print("\n --- Menú Beneficiarios ---")
        print("1. ➕ Agregar Beneficiario")
        print("2. 📜 Listar Beneficiario")
        print("3. 🔃 Modificar Beneficiario")
        print("4. 🗑️  Borrar Beneficiario")
        print("5. ◀️  Regresar al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                agregar_beneficiario()
            elif opcion == 2:
                listar_beneficiario()
            elif opcion == 3:
                modificar_beneficiario()
            elif opcion == 4:
                borrar_beneficiario()
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")

def menu_Pagos():
    while True:
        print("\n --- Menú Pagos ---")
        print("1. ➕ Agregar Pago")
        print("2. 📜 Listar Pago")
        print("3. 🔃 Modificar Pago")
        print("4. 🗑️  Borrar Pago")
        print("5. ◀️  Regresar al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                agregar_pago()
            elif opcion == 2:
                listar_pago()
            elif opcion == 3:
                modificar_pago()
            elif opcion == 4:
                borrar_pagos()
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")

def menu_Siniestros():
    while True:
        print("\n --- Menú Siniestros ---")
        print("1. ➕ Agregar Siniestro")
        print("2. 📜 Listar Siniestro")
        print("3. 🔃 Modificar Siniestro")
        print("4. 🗑️  Borrar Siniestro")
        print("5. ◀️  Regresar al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                agregar_siniestro()
            elif opcion == 2:
                listar_siniestro()
            elif opcion == 3:
                modificar_siniestro()
            elif opcion == 4:
                borrar_siniestro()
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
        except ValueError:
            print("¡Error! Por favor ingrese un formato válido")