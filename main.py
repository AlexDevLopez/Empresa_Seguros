from ui.SubMenus import menu_Clientes,menu_Poliza,menu_Beneficiarios,menu_Pagos,menu_Siniestros

def main():
    while True:
        print("\n======================================")
        print("     🏢 SISTEMA DE ASEGURADORA 🏢")
        print("======================================")
        print("1. 👥 Gestión de Clientes")
        print("2. 📄 Gestión de Pólizas")
        print("3. 👨‍👩‍👧‍👦 Gestión de Beneficiarios")
        print("4. 💵 Gestión de Pagos")
        print("5. 🚨 Gestión de Siniestros")
        print("6. ❌ Salir del Sistema")
        print("======================================")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                menu_Clientes()
            elif opcion == 2:
                menu_Poliza()
            elif opcion == 3:
                menu_Beneficiarios()
            elif opcion == 4:
                menu_Pagos()
            elif opcion == 5:
                menu_Siniestros()
            elif opcion == 6:
                print("\n ¡Gracias por utilizar el Sistema de Aseguradora! \n ¡Hasta Pronto! 👋")
                break
            else:
                print("\n ¡Opción no válida! Por favor, elija un número del 1 al 6")
        except ValueError:
            print("\n¡Error! Debes ingresar un número, no texto")

if __name__ == "__main__":
    main()