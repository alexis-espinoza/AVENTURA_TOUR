
from datetime import datetime

class Funciones_generales():
    
    def Fecha_actual(self):
        formato = "%Y-%m-%d"
        hoy = datetime.today()  # Asigna fecha-hora
        #return print(hoy.strftime(formato))
        return hoy.strftime(formato)