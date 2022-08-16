
class Reservacion():

    def __init__(self, data = [None]*4):
        self.numero_reserva    = data[0]
        self.cedula            = data[1]
        self.nombre            = data[2]
        self.cantidad_personas = data[3]


    def __str__(self):
        reservacion = f'''
        \n--DATOS DE LA RESERVACION--
        Número: {self.numero_reserva}
        Cédula: {self.cedula}
        Nombre: {self.nombre}
        Cantidad de personas: {self.cantidad_personas}\n'''
        return reservacion
    
    def no_es_vacio(self):
        return self.numero_reserva!= None and self.cedula!= None and self.nombre!= None and self.cantidad_personas!= None

'''
r = Reservacion((12, '5-0410-0161', 'Alexis Espinoza', 6))
print(r.__str__())
'''