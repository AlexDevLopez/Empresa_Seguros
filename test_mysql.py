import sys
sys.stdout.reconfigure(encoding='utf-8')

from ClassMySql import archivo_clientes, archivo_poliza, archivo_beneficiarios, archivo_pagos, archivo_siniestro
from MySqlConnection import db

# Limpiar TODAS las tablas (orden por foreign keys)
db.ejecutar("DELETE FROM siniestros")
db.ejecutar("DELETE FROM pagos")
db.ejecutar("DELETE FROM beneficiarios")
db.ejecutar("DELETE FROM polizas")
db.ejecutar("DELETE FROM clientes")
# Reiniciar auto-increment
db.ejecutar("ALTER TABLE clientes AUTO_INCREMENT = 1")
db.ejecutar("ALTER TABLE polizas AUTO_INCREMENT = 1")
db.ejecutar("ALTER TABLE beneficiarios AUTO_INCREMENT = 1")
db.ejecutar("ALTER TABLE pagos AUTO_INCREMENT = 1")
db.ejecutar("ALTER TABLE siniestros AUTO_INCREMENT = 1")

print("=" * 55)
print("  TEST COMPLETO: 5 Entidades x 4 Operaciones CRUD")
print("=" * 55)
errores = 0

# ========== 1. CLIENTES ==========
print("\n--- 1. CLIENTES ---")

# Agregar
archivo_clientes.agregar("Carlos, Ramirez Gonzalez, 1985-03-15, Masculino, RAGC850315HDFRNS09, 2228451234, carlos@email.com, Ingeniero, 25000")
archivo_clientes.agregar("Ana, Lopez Torres, 1990-07-22, Femenino, LOTA900722MDFPNX01, 2229876543, ana@email.com, Doctora, 35000")
datos = archivo_clientes.leerDatos()
if len(datos) == 2:
    print("  [OK] Agregar: 2 clientes insertados")
else:
    print(f"  [FAIL] Agregar: esperaba 2, tiene {len(datos)}")
    errores += 1

# Listar
datos = archivo_clientes.leerDatos()
if "Carlos" in datos[0] and "Ana" in datos[1]:
    print("  [OK] Listar: Carlos y Ana encontrados")
else:
    print(f"  [FAIL] Listar: datos inesperados")
    errores += 1

# Modificar (cambiar Carlos -> Pedro)
exito = archivo_clientes.modificar(0, "Pedro, Ramirez Gonzalez, 1985-03-15, Masculino, RAGC850315HDFRNS09, 2228451234, pedro@email.com, Arquitecto, 30000")
datos = archivo_clientes.leerDatos()
if exito and "Pedro" in datos[0]:
    print("  [OK] Modificar: Carlos -> Pedro")
else:
    print(f"  [FAIL] Modificar: exito={exito}")
    errores += 1

# Eliminar (borrar Ana, indice 1)
exito = archivo_clientes.eliminar(1)
datos = archivo_clientes.leerDatos()
if exito and len(datos) == 1:
    print("  [OK] Eliminar: Ana borrada, queda 1 registro")
else:
    print(f"  [FAIL] Eliminar: exito={exito}, registros={len(datos)}")
    errores += 1

# ========== 2. POLIZAS ==========
print("\n--- 2. POLIZAS ---")

# Obtener ID real de Pedro
id_pedro = datos[0].split(",")[0]

archivo_poliza.agregar(f"1001, 2025-01-01, 2026-01-01, 1500.00, 500000.00, Vida, Activa, {id_pedro}")
archivo_poliza.agregar(f"1002, 2025-06-01, 2026-06-01, 800.00, 250000.00, Auto, Activa, {id_pedro}")
datos_p = archivo_poliza.leerDatos()
if len(datos_p) == 2:
    print("  [OK] Agregar: 2 polizas insertadas")
else:
    print(f"  [FAIL] Agregar: esperaba 2, tiene {len(datos_p)}")
    errores += 1

# Listar
if "1001" in datos_p[0] and "1002" in datos_p[1]:
    print("  [OK] Listar: Polizas 1001 y 1002 encontradas")
else:
    print(f"  [FAIL] Listar")
    errores += 1

# Modificar poliza 1001 -> cambiar estatus a Cancelada
exito = archivo_poliza.modificar(0, f"1001, 2025-01-01, 2026-01-01, 1500.00, 500000.00, Vida, Cancelada, {id_pedro}")
datos_p = archivo_poliza.leerDatos()
if exito and "Cancelada" in datos_p[0]:
    print("  [OK] Modificar: Poliza 1001 -> Cancelada")
else:
    print(f"  [FAIL] Modificar: exito={exito}")
    errores += 1

# Eliminar poliza 1002
exito = archivo_poliza.eliminar(1)
datos_p = archivo_poliza.leerDatos()
if exito and len(datos_p) == 1:
    print("  [OK] Eliminar: Poliza 1002 borrada")
else:
    print(f"  [FAIL] Eliminar: exito={exito}")
    errores += 1

# ========== 3. BENEFICIARIOS ==========
print("\n--- 3. BENEFICIARIOS ---")

id_poliza = datos_p[0].split(",")[0]

archivo_beneficiarios.agregar(f"Maria, Ramirez Lopez, 2010-05-10, Hija, 60.00, {id_poliza}")
archivo_beneficiarios.agregar(f"Jose, Ramirez Lopez, 2012-08-20, Hijo, 40.00, {id_poliza}")
datos_b = archivo_beneficiarios.leerDatos()
if len(datos_b) == 2:
    print("  [OK] Agregar: 2 beneficiarios")
else:
    print(f"  [FAIL] Agregar: {len(datos_b)}")
    errores += 1

# Listar
if "Maria" in datos_b[0] and "Jose" in datos_b[1]:
    print("  [OK] Listar: Maria y Jose encontrados")
else:
    print(f"  [FAIL] Listar")
    errores += 1

# Modificar
exito = archivo_beneficiarios.modificar(0, f"Maria Elena, Ramirez Lopez, 2010-05-10, Hija, 70.00, {id_poliza}")
datos_b = archivo_beneficiarios.leerDatos()
if exito and "Maria Elena" in datos_b[0]:
    print("  [OK] Modificar: Maria -> Maria Elena, 70%")
else:
    print(f"  [FAIL] Modificar")
    errores += 1

# Eliminar
exito = archivo_beneficiarios.eliminar(1)
datos_b = archivo_beneficiarios.leerDatos()
if exito and len(datos_b) == 1:
    print("  [OK] Eliminar: Jose borrado")
else:
    print(f"  [FAIL] Eliminar")
    errores += 1

# ========== 4. PAGOS ==========
print("\n--- 4. PAGOS ---")

archivo_pagos.agregar(f"2025-01-15, 1500.00, Transferencia, REF001, {id_poliza}")
archivo_pagos.agregar(f"2025-02-15, 1500.00, Efectivo, REF002, {id_poliza}")
datos_pa = archivo_pagos.leerDatos()
if len(datos_pa) == 2:
    print("  [OK] Agregar: 2 pagos")
else:
    print(f"  [FAIL] Agregar: {len(datos_pa)}")
    errores += 1

# Listar
if "REF001" in datos_pa[0]:
    print("  [OK] Listar: Pagos encontrados")
else:
    print(f"  [FAIL] Listar")
    errores += 1

# Modificar
exito = archivo_pagos.modificar(0, f"2025-01-15, 1600.00, Tarjeta, REF001-MOD, {id_poliza}")
datos_pa = archivo_pagos.leerDatos()
if exito and "1600" in datos_pa[0]:
    print("  [OK] Modificar: Monto 1500 -> 1600, Tarjeta")
else:
    print(f"  [FAIL] Modificar")
    errores += 1

# Eliminar
exito = archivo_pagos.eliminar(1)
datos_pa = archivo_pagos.leerDatos()
if exito and len(datos_pa) == 1:
    print("  [OK] Eliminar: Pago REF002 borrado")
else:
    print(f"  [FAIL] Eliminar")
    errores += 1

# ========== 5. SINIESTROS ==========
print("\n--- 5. SINIESTROS ---")

archivo_siniestro.agregar(f"2025-03-01, 2025-02-28, Robo, 50000.00, 45000.00, En revision, {id_poliza}")
archivo_siniestro.agregar(f"2025-04-10, 2025-04-08, Accidente, 100000.00, 0.00, Pendiente, {id_poliza}")
datos_s = archivo_siniestro.leerDatos()
if len(datos_s) == 2:
    print("  [OK] Agregar: 2 siniestros")
else:
    print(f"  [FAIL] Agregar: {len(datos_s)}")
    errores += 1

# Listar
if "Robo" in datos_s[0] and "Accidente" in datos_s[1]:
    print("  [OK] Listar: Siniestros encontrados")
else:
    print(f"  [FAIL] Listar")
    errores += 1

# Modificar
exito = archivo_siniestro.modificar(0, f"2025-03-01, 2025-02-28, Robo, 50000.00, 48000.00, Aprobado, {id_poliza}")
datos_s = archivo_siniestro.leerDatos()
if exito and "Aprobado" in datos_s[0]:
    print("  [OK] Modificar: En revision -> Aprobado, 48000")
else:
    print(f"  [FAIL] Modificar")
    errores += 1

# Eliminar
exito = archivo_siniestro.eliminar(1)
datos_s = archivo_siniestro.leerDatos()
if exito and len(datos_s) == 1:
    print("  [OK] Eliminar: Siniestro Accidente borrado")
else:
    print(f"  [FAIL] Eliminar")
    errores += 1

# ========== RESUMEN ==========
total = 20
print("\n" + "=" * 55)
if errores == 0:
    print(f"  RESULTADO: {total}/{total} tests pasaron!")
else:
    print(f"  RESULTADO: {total - errores}/{total} tests pasaron, {errores} fallaron")
print("=" * 55)
