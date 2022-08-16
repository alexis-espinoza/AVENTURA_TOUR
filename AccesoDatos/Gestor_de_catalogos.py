from AccesoDatos.Gestor_de_conexiones import Gestor_de_conexiones
class Gestor_de_catalogos(): 

    def Obtener_datos_empresa(self):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            cursor.execute("SELECT * FROM EMPRESA")
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()


    def Obtener_totales_por_tarifa(self, fecha_actual, id_tarifa):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''SELECT RESERVACIONES_ESPACIOS.id_tarifa, TARIFAS.descripcion, SUM(monto) AS tarifa
            FROM TARIFAS, RESERVACIONES_ESPACIOS
            WHERE 
            TARIFAS.id = RESERVACIONES_ESPACIOS.id_tarifa
            AND  RESERVACIONES_ESPACIOS.fecha_reservacion = (?)
            AND RESERVACIONES_ESPACIOS.id_tarifa = (?)
            GROUP BY  
            RESERVACIONES_ESPACIOS.fecha_reservacion, 
            RESERVACIONES_ESPACIOS.id_tarifa,
            TARIFAS.descripcion'''
            cursor.execute(query, fecha_actual, id_tarifa)
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()
            
    def Obtener_tarifa_por_descripcion(self, descripcion):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = "SELECT * FROM TARIFAS WHERE descripcion = (?)"
            cursor.execute(query, descripcion)
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()

    def Obtener_horario_por_descripcion(self, descripcion):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = "SELECT * FROM HORARIOS WHERE descripcion = (?)"
            cursor.execute(query, descripcion)
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()

    def Obtener_telefericos(self):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            cursor.execute("SELECT * FROM TELEFERICOS")
            return cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.Close()

    def Obtener_horarios(self):
        try:                
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            cursor.execute("SELECT * FROM HORARIOS")
            return cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.Close()
    
    def Obtener_tarifas(self):
        try:
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            cursor.execute("SELECT * FROM TARIFAS")
            return cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.Close()
