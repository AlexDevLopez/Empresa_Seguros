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
    ├── Pagos ← ClassPagos.py  ✅ Ya hereda de Transaccion
    └── Siniestro ← ClassSiniestros.py  ⚠️ PENDIENTE: migrar a Transaccion
```

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Menú principal del sistema |
| `SubMenus.py` | Submenús CRUD para cada entidad |
| `ClassAseguradora.py` | Clase abstracta raíz (ABC) con `capturardatos()` y `devolverdatos()` |
| `ClassPersona.py` | Clase abstracta intermedia (nombre, apellidos, fecha_nacimiento) |
| `ClassCliente.py` | Cliente con CURP, teléfono, correo, etc. + funciones CRUD |
| `ClassBeneficiarios.py` | Beneficiario con parentesco, porcentaje + funciones CRUD |
| `ClassPoliza.py` | Póliza con fechas, prima, suma asegurada + funciones CRUD |
| `ClassTransaccion.py` | Clase abstracta con método `procesar()` |
| `ClassPagos.py` | Pago con monto, método, referencia + funciones CRUD |
| `ClassSiniestros.py` | Siniestro con montos, fechas, tipo + funciones CRUD |
| `ClassArchivos.py` | Persistencia en CSV (agregar, leer, modificar, eliminar) |

## Persistencia actual
- Archivos CSV en la carpeta `Datos(Aseguradora)/`
- Clase `ArchivosCSV` maneja todo el CRUD de archivos
- **PENDIENTE:** Migrar a MySQL (Laragon)

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
- [x] Validar `monto_aprobado ≤ monto_reclamado` en siniestros
- [x] Validar `fecha_inicio < fecha_fin` en pólizas
- [x] Validar `fecha_ocurrencia ≤ fecha_reporte` en siniestros
- [x] Validar CURP única al registrar cliente
- [x] Validar porcentaje beneficiarios = 100%

### ⬜ Fase 4 — Refactorización (PENDIENTE)
- [ ] Crear funciones genéricas de CRUD (eliminar código duplicado)
- [ ] Unificar submenús en un menú genérico
- [ ] Limpiar nombres y código muerto

### ⬜ Fase 5 — MySQL con Laragon (PENDIENTE)
- [ ] Diseñar tablas SQL con catálogos normalizados
- [ ] Escribir script `.sql` de creación de BD
- [ ] Crear clase de conexión a MySQL
- [ ] Reemplazar operaciones CSV por MySQL

### ⬜ Fase 6 — Entregables (PENDIENTE)
- [ ] Diagrama de clases UML
- [ ] Script SQL entregable
- [ ] Documento de refactorización antes/después

## Bugs conocidos
1. ~~`ClassPagos.py` línea 24: `procesar()` hace `print() + string` → TypeError~~ ✅ CORREGIDO
2. ~~`ClassSiniestros.py`: todavía hereda de `Aseguradora` en vez de `Transaccion`~~ ✅ CORREGIDO
3. El `self.id += 1` en las clases siempre da 1 (el ID real lo pone `ArchivosCSV`)

## Cómo pedirle contexto a la IA en otra compu
Cuando abras el proyecto en otra computadora, dile a la IA:
> "Lee el archivo CONTEXTO.md para entender el proyecto y dime en qué fase estoy"
