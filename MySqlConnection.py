import mysql.connector

class ConexionMySQL:

    def __init__(self, host="localhost", user="root", password="", database="aseguradora"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def ejecutar(self, sql, parametros=None):
        """Ejecuta INSERT, UPDATE, DELETE (modifica datos)"""
        conex = self.conectar()
        cursor = conex.cursor()
        try:
            cursor.execute(sql, parametros)
            conex.commit()
            return True
        except mysql.connector.Error as e:
            if e.errno == 1451:
                print("No se puede eliminar: tiene registros asociados en otra tabla.")
            else:
                print(f"Error en la base de datos: {e}")
            conex.rollback()
            return False
        finally:
            cursor.close()
            conex.close()

    def consultar(self, sql, parametros=None):
        """Ejecuta SELECT (lee datos). Retorna lista de tuplas."""
        conex = self.conectar()
        cursor = conex.cursor()
        try:
            cursor.execute(sql, parametros)
            resultado = cursor.fetchall()
            return resultado
        except mysql.connector.Error as e:
            print(f"Error en la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conex.close()


db = ConexionMySQL()