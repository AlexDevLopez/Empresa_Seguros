# 🏢 Aseguradora VidaFutura — Contexto del Proyecto

## ¿Qué es esto?
Sistema de gestión de seguros para la aseguradora VidaFutura.
Proyecto escolar de POO (Programación Orientada a Objetos) en Python.
**Deadline: primera semana de junio 2026.**

## Arquitectura de clases actual

```
Aseguradora (ABC) ← ClassAseguradora.py
├── Persona (abstracta) ← ClassPersona.py
│   ├── Cliente ← ClassCliente.py
│   └── Beneficiario ← ClassBeneficiarios.py
├── Poliza ← ClassPoliza.py
└── Transaccion (abstracta) ← ClassTransaccion.py
    ├── Pagos ← ClassPagos.py  ✅ Hereda de Transaccion
    └── Siniestro ← ClassSiniestros.py  ✅ Hereda de Transaccion
```

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Menú principal del sistema |
| `SubMenus.py` | Submenús CRUD para cada entidad |
| `ClassAseguradora.py` | Clase abstracta raíz (ABC) con `capturardatos()` y `devolverdatos()` |
| `ClassPersona.py` | Clase abstracta intermedia (nombre, apellidos, fecha_nacimiento) |
| `ClassCliente.py` | Cliente con CURP, teléfono, correo, etc. + funciones CRUD + validación CURP única |
| `ClassBeneficiarios.py` | Beneficiario con parentesco, porcentaje + funciones CRUD + validación % ≤ 100 |
| `ClassPoliza.py` | Póliza con fechas, prima, suma asegurada + funciones CRUD + validación fechas |
| `ClassTransaccion.py` | Clase abstracta con método `procesar()` |
| `ClassPagos.py` | Pago con monto, método, referencia + funciones CRUD + `procesar()` |
| `ClassSiniestros.py` | Siniestro con montos, fechas, tipo + funciones CRUD + `procesar()` + validaciones |
| `ClassArchivos.py` | Persistencia en CSV (legacy, ya no se usa en producción) |
| `ClassMySql.py` | Persistencia en MySQL (reemplaza CSV con misma interfaz) |
| `MySqlConnection.py` | Conexión robusta a MySQL con try/except/finally |
| `CRUDGenerico.py` | Funciones genéricas: Agregar, Listar, Modificar, Borrar |
| `aeguradora.sql` | Script SQL para crear la base de datos y tablas |
| `DiagramaUML.md` | Diagrama de clases UML (Mermaid) |
| `Refactorizacion.md` | Documento de refactorización antes/después |
| `test_mysql.py` | Tests automatizados CRUD (20/20 OK) |

## Persistencia actual
- **MySQL** (base de datos `aseguradora` en Laragon)
- Clase `ArchivosMySql` maneja todo el CRUD con misma interfaz que `ArchivosCSV`
- Clase `ConexionMySQL` gestiona conexiones con rollback ante errores
- ✅ Migración completada — solo se cambió 1 línea de import en `SubMenus.py`

## Estado del plan de implementación

### ✅ Fase 1 — Calentamiento (COMPLETADA)
- [x] Guardar evidencia del código "antes" (para refactorización)
- [x] Hacer `Persona` abstracta con ABC
- [x] Verificar que el sistema sigue funcionando

### ✅ Fase 2 — Abstracción (COMPLETADA)
- [x] Crear clase abstracta `Transaccion` con `procesar()`
- [x] Migrar `Pagos` para heredar de `Transaccion`
- [x] **Arreglar bug en `procesar()` de Pagos** — corregido: ahora usa if/else y retorna True/False
- [x] **Migrar `Siniestro` para heredar de `Transaccion`**
- [x] Implementar `procesar()` en `Siniestro` — valida monto_aprobado ≤ monto_reclamado

### ✅ Fase 3 — Validaciones (COMPLETADA)
- [x] Validar `monto_aprobado ≤ monto_reclamado` en siniestros (while loop en capturardatos)
- [x] Validar `fecha_inicio < fecha_fin` en pólizas (usa `datetime.strptime` con formato DD/MM/YYYY)
- [x] Validar `fecha_ocurrencia ≤ fecha_reporte` en siniestros (usa `datetime.strptime`)
- [x] Validar CURP única al registrar cliente (lee CSV existente con `for/else` + `while True`)
- [x] Validar porcentaje beneficiarios ≤ 100% por póliza (suma porcentajes existentes del CSV)
- [x] Extra: validación de teléfono 10 dígitos en cliente
- [x] Extra: validación de que la póliza exista al registrar beneficiario

### ✅ Fase 4 — Refactorización (COMPLETADA)
- [x] Crear funciones genéricas de CRUD (eliminar código duplicado)
- [x] Unificar submenús en un menú genérico
- [x] Limpiar nombres y código muerto

### ✅ Fase 5 — MySQL con Laragon (COMPLETADA)
- [x] Diseñar tablas SQL con catálogos normalizados
- [x] Escribir script `.sql` de creación de BD
- [x] Crear clase de conexión a MySQL
- [x] Reemplazar operaciones CSV por MySQL

### ✅ Fase 6 — Entregables (COMPLETADA)
- [x] Diagrama de clases UML → `DiagramaUML.md`
- [x] Script SQL entregable → `aeguradora.sql`
- [x] Documento de refactorización antes/después → `Refactorizacion.md`

## Bugs conocidos
1. ~~`ClassPagos.py` línea 24: `procesar()` hace `print() + string` → TypeError~~ ✅ CORREGIDO
2. ~~`ClassSiniestros.py`: todavía hereda de `Aseguradora` en vez de `Transaccion`~~ ✅ CORREGIDO
3. El `self.id += 1` en las clases siempre da 1 (el ID real lo pone `ArchivosCSV`)
4. ~~Las fechas en Póliza y Siniestro se guardan como `datetime` en el CSV (formato largo `2026-01-15 00:00:00`). Pendiente formatear con `strftime()` en `devolverdatos()`~~ ✅ CORREGIDO

## Notas para Fase 4 — ✅ RESUELTO
El código duplicado fue eliminado con `CRUDGenerico.py` (4 funciones genéricas) y `menu_generico()` en SubMenus.py.
Ver `Refactorizacion.md` para detalles completos del antes/después.

## Preferencia de enseñanza
El usuario prefiere que la IA lo **guíe paso a paso con pistas**, no que escriba el código por él.
Darle preguntas para pensar, señalar errores lógicos, y dejar que él implemente las soluciones.

## Cómo pedirle contexto a la IA en otra compu
Cuando abras el proyecto en otra computadora, dile a la IA:
> "Lee el archivo CONTEXTO.md para entender el proyecto y dime en qué fase estoy"
