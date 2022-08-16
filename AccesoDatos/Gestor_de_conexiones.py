import pyodbc
from os import getcwd


class Gestor_de_conexiones():

    def __init__(self):
        self.string_conexion = ("Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-9EJDP1D;"
                "Database=AVENTURA_TOUR;"
                "Trusted_Connection=yes;")
        self.conexion = pyodbc.connect(self.string_conexion)
        self.cursor = None
            
    def Conexion(self):
        return self.conexion
        
    def Cursor(self):
        self.cursor = self.conexion.cursor()
        return self.cursor

    def Commit(self):
        self.conexion.commit()

    def Close(self):
       self.conexion.close()



