from MySqlConnection import db

class ArchivosMySql:
    def __init__(self, tabla, encabezado):
        self.tabla = tabla
        self.encabezado = encabezado

    def devolverencabezados(self):
        return self.encabezado.split(",")
    
    def agregar(self,dato):
        columnas = self.devolverencabezados()[1:]
        valores = [v.strip() for v in dato.split(",")]

        placeholders = " ,".join(["%s"] * len(columnas))
        cols = ",".join(columnas)

        sql = f"INSERT INTO {self.tabla} ({cols}) VALUES ({placeholders})"
        db.ejecutar(sql,tuple(valores))
        
    def leerDatos(self):
        resultado = db.consultar(f"SELECT * FROM {self.tabla}")
        datos = []
        for renglon in resultado:
            datos.append(",".join(map(str,renglon)))
        return datos

    def modificar(self,id,nuevo_dato):
        datos = self.leerDatos()
        if 0 <= id < len(datos):
            id_real = datos[id].split(",")[0]
            
            columnas = self.devolverencabezados()[1:]
            valores = [v.strip() for v in nuevo_dato.split(",")]

            set_clausulas = []
            for i, col in enumerate(columnas):
                if i < len(valores):
                    set_clausulas.append(f"{col} = %s")
        
            sql = f"UPDATE {self.tabla} SET {', '.join(set_clausulas)} WHERE ID = %s"
            parametros = tuple(valores) + (id_real,)
            
            db.ejecutar(sql, parametros)
            return True
        else:
            print("Índice fuera de rango")
            return False

    def eliminar(self, indice):
        datos = self.leerDatos()
        if 0 <= indice < len(datos):
            id_real = datos[indice].split(",")[0]

            sql = f"DELETE FROM {self.tabla} WHERE ID = %s"
            db.ejecutar(sql, (id_real,))
            return True
        else:
            print("Índice fuera de rango")
            return False


archivo_clientes = ArchivosMySql("clientes", "id,nombre,apellidos,fecha_nacimiento,sexo,curp,telefono,correo,ocupacion,ingreso_mensual")
archivo_poliza = ArchivosMySql("polizas", "id,numero_poliza,fecha_inicio,fecha_fin,prima_mensual,suma_asegurada,tipo_poliza,estatus,cliente_id")
archivo_beneficiarios = ArchivosMySql("beneficiarios", "id,nombre,apellidos,fecha_nacimiento,parentesco,porcentaje_asignado,poliza_id")
archivo_pagos = ArchivosMySql("pagos", "id,fecha_pago,monto_pagado,metodo_pago,referencia,poliza_id")
archivo_siniestro = ArchivosMySql("siniestros", "id,fecha_reporte,fecha_ocurrencia,tipo_siniestro,monto_reclamado,monto_aprobado,estatus_siniestro,poliza_id")
