
class Reservacion_espacio():

    def __init__(self, data = ['']*7):
        self. id = data[0]
        self.id_horario = data[1]
        self.id_reservacion = data[2]
        self.id_teleferico = data[3]
        self.id_tarifa = data[4]
        self.espacio_teleferico = data[5]
        self.fecha_reservacion = data[6]

    def __str__(self):
        return '->'+self.id_horario +' | '+ self.id_teleferico +' | '+ 'Espacio '+str(self.espacio_teleferico) +' | '+ self.id_tarifa


    
