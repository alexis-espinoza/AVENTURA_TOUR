
class Empresa():

    def __init__(self, data = range(4)):
        self.id = data[0]
        self.nombre = data[1]
        self.telefono = data[2]
        self.direccion = data[3]

    def __str__(self):
        return '\n--DATOS DE LA EMPRESA--\nNombre: '+self.nombre+'\nTelefono: '+self.telefono +'\nDirección: '+self.direccion

'''
e = Empresa(('test', '99-99-999','San Jose'))
print(e.__str__())
'''