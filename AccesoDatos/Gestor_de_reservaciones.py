
from AccesoDatos.Gestor_de_conexiones import Gestor_de_conexiones
#from Gestor_de_conexiones import Gestor_de_conexiones
class Gestor_de_reservaciones():
    
    def Insertar_reservacion(self, reservacion):
        try:  
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''INSERT INTO RESERVACIONES (id, cedula, nombre, cantidad_personas) 
            VALUES (?,?,?,?);'''
            cursor.execute(query, reservacion)
            conn.Commit()
            return True
        except Exception as e:
            return False
        finally:
            conn.Close()

    def Obtener_ultima_reservacion(self):
        try:    
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            cursor.execute("SELECT TOP 1 * FROM RESERVACIONES ORDER BY id DESC")
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()   

    def Insertar_reservaciones_espacios(self, reservacion_horario):
        try:  
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''INSERT INTO RESERVACIONES_ESPACIOS
            (id_horario, id_reservacion, id_teleferico, id_tarifa, espacio_teleferico, fecha_reservacion) 
            VALUES (?,?,?,?,?,?);'''
            cursor.executemany(query, reservacion_horario)
            conn.Commit()
        except Exception as e:
            print(e)
        finally:
            conn.Close()

    def Obtener_reservacion(self, cedula, numero_reservacion):
        try:    
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''SELECT * FROM RESERVACIONES WHERE cedula = (?) AND id = (?)''' 
            cursor.execute(query, cedula, numero_reservacion)
            return cursor.fetchone()
        except Exception as e:
            pass
        finally:
            conn.Close()   

    def Obtener_reservaciones_espacios(self, numero_reservacion):
        try:    
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''SELECT RESERVACIONES_ESPACIOS.id, HORARIOS.descripcion,  
            RESERVACIONES.id, TELEFERICOS.descripcion, TARIFAS.descripcion,
            RESERVACIONES_ESPACIOS.espacio_teleferico, RESERVACIONES_ESPACIOS.fecha_reservacion
            FROM RESERVACIONES_ESPACIOS, HORARIOS, RESERVACIONES,TELEFERICOS, TARIFAS WHERE
            RESERVACIONES.id = RESERVACIONES_ESPACIOS.id_reservacion AND
            HORARIOS.id = RESERVACIONES_ESPACIOS.id_horario AND
            TELEFERICOS.id = RESERVACIONES_ESPACIOS.id_teleferico AND
            TARIFAS.id = RESERVACIONES_ESPACIOS.id_tarifa 
            AND RESERVACIONES.id = (?)''' 
            cursor.execute(query, numero_reservacion)
            return cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.Close()

    def Obtener_espacios_ocupados(self, id_horario, id_teleferico, fecha_reservacion):
        try:    
            conn = Gestor_de_conexiones()
            cursor = conn.Cursor()
            query = '''SELECT * FROM RESERVACIONES_ESPACIOS 
            WHERE id_horario = (?) AND id_teleferico = (?) AND fecha_reservacion = (?)''' 
            cursor.execute(query, id_horario, id_teleferico, fecha_reservacion)
            return cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.Close()


