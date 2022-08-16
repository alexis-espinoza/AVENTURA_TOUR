from LogicaNegocio.Funciones_generales import Funciones_generales
from LogicaNegocio.Coordinador_de_catalogos import Coordinador_de_catalogos
from AccesoDatos.Gestor_de_reservaciones import Gestor_de_reservaciones
from LogicaNegocio.Funciones_generales import Funciones_generales
from Modelos.Reservacion import Reservacion
from Modelos.Reservacion_espacio import Reservacion_espacio



class Coordinador_de_reservaciones():

    def Generar_numero_reserva(self):
        try:
            gestor = Gestor_de_reservaciones()        
            utimo_cod = Reservacion(gestor.Obtener_ultima_reservacion()).numero_reserva #obtiene la parte numérica del ultimo código
            cod_sig = str(utimo_cod+1)
            return cod_sig
        except AttributeError as err:
            return '1'
        except Exception:
            return '1'

    def Generar_factura(self,cedula, numero_reserva):
        factura = ''
        monto_total = 0
        reservacion = self.Consultar_reservacion(cedula, numero_reserva)
        if(reservacion.no_es_vacio()):
            coordinador = Coordinador_de_catalogos()
            empresa = coordinador.Consultar_datos_empresa() 
            factura += empresa.__str__() + f'\nFecha: {Funciones_generales().Fecha_actual()}'
            factura += reservacion.__str__()
            factura += '\n--DATALLE DE LOS CAMPOS--\n'
            reservaciones_espacios = self.Consultar_reservaciones_espacios(numero_reserva)
            for espacio in reservaciones_espacios:
                monto = coordinador.Consultar_tarifa_por_descripcion(espacio.id_tarifa).monto
                factura += espacio.__str__()+ '\n'
                factura += 'Valor: '+str(monto)+'\n'#+f'{"-"*50}\n' 
                monto_total+= monto
            factura += f'\nTotal a pagar: {monto_total}'
        return factura


    def Agregar_reservacion(self, nueva_reservacion):
            gestor = Gestor_de_reservaciones()
            return gestor.Insertar_reservacion(tuple(nueva_reservacion.__dict__.values()))
    

    def Agregar_reservaciones_espacios(self, lista_reservacion_horario):
        try:
            gestor = Gestor_de_reservaciones()
            reservaciones_horario = list(map(lambda Reservacion_horario: tuple(list(Reservacion_horario.__dict__.values())[1:]), lista_reservacion_horario))
            gestor.Insertar_reservaciones_espacios(reservaciones_horario)
        except:
            pass

    def Consultar_reservacion(self, cedula, numero_reserva):  
        try:
            gestor = Gestor_de_reservaciones()
            return Reservacion(gestor.Obtener_reservacion(cedula, numero_reserva))
        except:
            return Reservacion()
    
    def Consultar_reservaciones_espacios(self, numero_reserva):
        gestor = Gestor_de_reservaciones()
        reservaciones_espacios = []
        for data in gestor.Obtener_reservaciones_espacios(numero_reserva):
            reservaciones_espacios.append(Reservacion_espacio(data))
        return reservaciones_espacios


    def Espacios_ocupados_teleferico(self, id_horario, id_teleferico, fecha_reservacion):
        gestor = Gestor_de_reservaciones()
        espacios_ocupados = []
        for data in gestor.Obtener_espacios_ocupados(id_horario, id_teleferico, fecha_reservacion):
            espacios_ocupados.append(Reservacion_espacio(data))
        return espacios_ocupados

    def Consultar_disponibilidad_general(self):
        coordinador = Coordinador_de_catalogos()
        resumen_disponibilidad = []
        mayor = 0
        menor = 1000
        horarios = coordinador.Obtener_descripcion_horarios()
        for horario in horarios:
            diponible_por_horario = self.Consultar_disponibilidad_por_horario(horario)
            diponible_por_horario['horario'] = horario
            mayor = diponible_por_horario['ocupados'] if diponible_por_horario['ocupados'] > mayor else mayor
            menor = diponible_por_horario['ocupados'] if diponible_por_horario['ocupados'] < menor else menor
            resumen_disponibilidad.append(diponible_por_horario)
        resumen_disponibilidad.append(menor)
        resumen_disponibilidad.append(mayor)
        return resumen_disponibilidad

    def Consultar_disponibilidad_por_horario(self,desc_horario):
        lista_espacios = []
        total_disponibles = 0
        total_ocupados = 0
        coordinador = Coordinador_de_catalogos()
        telefericos = coordinador.Consultar_telefericos()
        id_horario = coordinador.Consultar_horario_por_descripcion(desc_horario).id
        for teleferico in telefericos:
            ocupados = len(self.Espacios_ocupados_teleferico(id_horario, teleferico.id, Funciones_generales().Fecha_actual()))
            total = teleferico.capacidad
            disponibles = total-ocupados
            total_disponibles += disponibles
            total_ocupados += ocupados
            lista_espacios.append((ocupados,disponibles,total))
        return {'disponibles': total_disponibles, 'ocupados':total_ocupados,'detalle': lista_espacios}
        
        
    def Generar_espacios_disponibles(self, cantidad_espacios, estado_actual):
        espacios_teleferico = []
        utilizados = 1
        id_tel = 1
        for telf in estado_actual:    
            for espacio in range(telf[0]+1, telf[2]+1):
                if(utilizados <= cantidad_espacios):     #TELEFERICO     /   ESPACIO
                    espacios_teleferico.append((id_tel, espacio))
                utilizados+=1
            id_tel+=1
        return espacios_teleferico


    
