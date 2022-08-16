
from AccesoDatos.Gestor_de_catalogos import Gestor_de_catalogos
from Modelos.Teleferico import Teleferico
from Modelos.Horario import Horario
from Modelos.Tarifa import  Tarifa
from Modelos.Empresa import  Empresa
from LogicaNegocio.Funciones_generales import Funciones_generales


class Coordinador_de_catalogos():

    def Consultar_tarifa_por_descripcion(self, desc_tarifa):
        gestor = Gestor_de_catalogos()
        return Tarifa(gestor.Obtener_tarifa_por_descripcion(desc_tarifa))

    def Consultar_horario_por_descripcion(self, desc_horario):
        gestor = Gestor_de_catalogos()
        return Horario(gestor.Obtener_horario_por_descripcion(desc_horario))

    def Consultar_totales_tarifas(self):
        gestor = Gestor_de_catalogos()
        tarifas = self.Consultar_tarifas()
        fecha_actual = Funciones_generales().Fecha_actual()
        totales_tarifas = []
        for tarifa in tarifas:
            tarifa_actual = gestor.Obtener_totales_por_tarifa(fecha_actual, tarifa.id)
            if(tarifa_actual!= None):
                totales_tarifas.append(Tarifa(tarifa_actual))
            else:
                totales_tarifas.append(Tarifa((tarifa.id,tarifa.descripcion,0.00)))

        return totales_tarifas
    
    def Consultar_telefericos(self):
        gestor = Gestor_de_catalogos()
        Telefericos = []
        for data in gestor.Obtener_telefericos():
            Telefericos.append(Teleferico(data))
        return Telefericos

    def Consultar_tarifas(self):
        gestor = Gestor_de_catalogos()
        Tarifas = []
        for data in gestor.Obtener_tarifas():
            Tarifas.append(Tarifa(data))
        return Tarifas

    def Consultar_horarios(self):
        gestor = Gestor_de_catalogos()
        Horarios = []
        for data in gestor.Obtener_horarios():
            Horarios.append(Horario(data))
        return Horarios

    def Consultar_datos_empresa(self):
        gestor = Gestor_de_catalogos()
        return Empresa(gestor.Obtener_datos_empresa())

    def Obtener_descripcion_horarios(self):
        return list(map(lambda Horario: Horario.descripcion, self.Consultar_horarios()))
    
    def Obtener_descripcion_telefericos(self):
        return list(map(lambda Teleferico: Teleferico.descripcion, self.Consultar_telefericos()))

    def Obtener_descripcion_tarifas(self):
        return list(map(lambda Tarifa: Tarifa.descripcion, self.Consultar_tarifas()))

    def Obtener_monto_tarifas(self):
        return list(map(lambda Tarifa: Tarifa.monto, self.Consultar_tarifas()))


