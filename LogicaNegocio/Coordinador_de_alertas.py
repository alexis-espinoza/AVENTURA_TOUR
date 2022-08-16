from tkinter import messagebox as MessageBox

class Coordinador_de_alertas():

    def __init__(self):
        self.alerta = {'no_horario':'No hay la cantidad de espacios requeridos en el horario seleccionado',
                        'BD_insertar':'No fue posible insertar el registro. Posibles causas:\n-Registro duplicado\n-Tipo de dato incorrecto',                        
                        'error_general':'La operación actual no pudo ser ejecutada',
                        'BD_consultar':'No fue posible realizar la operación. Posibles causas:\n-Esta función depende de otra\n-No existe la data solicitada',
                        'no_datos': 'La consulta realizada no retornó datos',
                        'seleccion':'¿Está seguro que desea continuar con esta operación?',
                        'confirmacion':'La operación se ejecutó de manera exitosa',
                        'formulario':'Faltan campos obligatorios en el formulario.\nVerifique los valores ingresados',
                        'conf_insert':'Los datos fueron agregados correctamente'}
            
                                
    def Mostrar_factura(self, detalle):
        MessageBox.showinfo('Detalle de factura', detalle)

    def Mostrar_afirmacion(self, tipo):
        MessageBox.showinfo('Información', self.alerta[tipo])

    def Mostrar_alerta(self, tipo):
        MessageBox.showwarning('Alerta',self.alerta[tipo])

    def Mostrar_error(self, tipo):
        MessageBox.showerror('Error',self.alerta[tipo])

    def Mostrar_confirmacion(self, tipo):
        confirmacion = 'no'
        confirmacion = MessageBox.askquestion('Requiere confirmación', self.alerta[tipo])
        return confirmacion    

        

