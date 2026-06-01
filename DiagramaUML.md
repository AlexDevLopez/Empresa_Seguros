# 📊 Diagrama de Clases UML — Aseguradora VidaFutura

## Diagrama de Herencia (Modelo de Negocio)

```mermaid
classDiagram
    direction TB

    class Aseguradora {
        <<abstract>>
        +capturardatos()* 
        +devolverdatos()* str
    }

    class Persona {
        <<abstract>>
        -nombre : str
        -apellidos : str
        -fecha_nacimiento : str
        +capturardatos()*
        +devolverdatos()* str
    }

    class Transaccion {
        <<abstract>>
        -id : int
        -poliza : Poliza
        +procesar()* bool
    }

    class Cliente {
        -id : int
        -sexo : str
        -CURP : str
        -telefono : str
        -correo : str
        -ocupacion : str
        -ingreso_mensual : int
        +capturardatos()
        +devolverdatos() str
    }

    class Beneficiario {
        -id : int
        -parentesco : str
        -porcentaje_asignado : int
        -id_poliza : int
        +capturardatos()
        +devolverdatos() str
    }

    class Poliza {
        -id : int
        -numero_poliza : int
        -fecha_inicio : datetime
        -fecha_fin : datetime
        -prima_mensual : float
        -suma_asegurada : float
        -tipo_poliza : str
        -estatus : str
        -id_cliente : int
        +capturardatos()
        +devolverdatos() str
    }

    class Pagos {
        -id : int
        -fecha_pago : datetime
        -monto_pagado : int
        -metodo_pago : str
        -referencia : str
        -id_poliza : int
        +capturardatos()
        +devolverdatos() str
        +procesar() bool
    }

    class Siniestro {
        -id : int
        -fecha_reporte : datetime
        -fecha_ocurrencia : datetime
        -tipo_siniestro : str
        -monto_reclamado : float
        -monto_aprobado : float
        -estatus_siniestro : str
        -id_poliza : int
        +capturardatos()
        +devolverdatos() str
        +procesar() bool
    }

    Aseguradora <|-- Persona : hereda
    Aseguradora <|-- Poliza : hereda
    Aseguradora <|-- Transaccion : hereda
    Persona <|-- Cliente : hereda
    Persona <|-- Beneficiario : hereda
    Transaccion <|-- Pagos : hereda
    Transaccion <|-- Siniestro : hereda

    Cliente "1" --> "*" Poliza : tiene
    Poliza "1" --> "*" Beneficiario : tiene
    Poliza "1" --> "*" Pagos : recibe
    Poliza "1" --> "*" Siniestro : reporta
```

## Diagrama de Persistencia (Patrón Estrategia)

```mermaid
classDiagram
    direction LR

    class ArchivosCSV {
        -archivo : str
        -encabezado : str
        +agregar(dato)
        +leerDatos() list
        +modificar(indice, nuevo_dato) bool
        +eliminar(indice) bool
        +devolverencabezados() list
        -sobreescribir(renglones)
        -__reiniciarArchivo__()
    }

    class ArchivosMySql {
        -tabla : str
        -encabezado : str
        +agregar(dato)
        +leerDatos() list
        +modificar(id, nuevo_dato) bool
        +eliminar(indice) bool
        +devolverencabezados() list
    }

    class ConexionMySQL {
        -host : str
        -user : str
        -password : str
        -database : str
        +conectar() connection
        +ejecutar(sql, parametros)
        +consultar(sql, parametros) list
    }

    class CRUDGenerico {
        <<module>>
        +Agregar_generico(Clase, archivo, nombre)
        +Listar_generico(archivo, nombre) bool
        +Modificar_generico(clase, archivo, nombre) bool
        +Borrar_generico(archivo, nombre) bool
    }

    ArchivosMySql --> ConexionMySQL : usa
    CRUDGenerico --> ArchivosMySql : opera con
    CRUDGenerico --> ArchivosCSV : opera con
```

## Diagrama de Interfaz de Usuario

```mermaid
classDiagram
    direction TB

    class main {
        <<module>>
        +main()
    }

    class SubMenus {
        <<module>>
        +menu_generico(titulo, Clase, archivo, nombre)
        +menu_Clientes()
        +menu_Poliza()
        +menu_Beneficiarios()
        +menu_Pagos()
        +menu_Siniestros()
    }

    main --> SubMenus : llama
    SubMenus --> CRUDGenerico : delega CRUD
```

## Relaciones en Base de Datos (Modelo E-R)

```mermaid
erDiagram
    CLIENTES ||--o{ POLIZAS : "tiene"
    POLIZAS ||--o{ BENEFICIARIOS : "cubre"
    POLIZAS ||--o{ PAGOS : "recibe"
    POLIZAS ||--o{ SINIESTROS : "reporta"

    CLIENTES {
        int id PK
        varchar nombre
        varchar apellidos
        date fecha_nacimiento
        varchar sexo
        varchar curp UK
        varchar telefono
        varchar correo UK
        varchar ocupacion
        decimal ingreso_mensual
    }

    POLIZAS {
        int id PK
        int numero_poliza UK
        date fecha_inicio
        date fecha_fin
        decimal prima_mensual
        decimal suma_asegurada
        varchar tipo_poliza
        varchar estatus
        int cliente_id FK
    }

    BENEFICIARIOS {
        int id PK
        varchar nombre
        varchar apellidos
        date fecha_nacimiento
        varchar parentesco
        decimal porcentaje_asignado
        int poliza_id FK
    }

    PAGOS {
        int id PK
        date fecha_pago
        decimal monto_pagado
        varchar metodo_pago
        varchar referencia
        int poliza_id FK
    }

    SINIESTROS {
        int id PK
        date fecha_reporte
        date fecha_ocurrencia
        varchar tipo_siniestro
        decimal monto_reclamado
        decimal monto_aprobado
        varchar estatus_siniestro
        int poliza_id FK
    }
```
