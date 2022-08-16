from functools import partial
from tkinter import *
from tkinter import ttk
from LogicaNegocio.Funciones_generales import Funciones_generales
from LogicaNegocio.Coordinador_de_alertas import Coordinador_de_alertas
from LogicaNegocio.Coordinador_de_catalogos import Coordinador_de_catalogos
from LogicaNegocio.Coordinador_de_reservaciones import Coordinador_de_reservaciones
from Modelos.Reservacion import Reservacion
from Modelos.Reservacion_espacio import Reservacion_espacio

class Aventura_tour:

    def __init__(self):
        self.root = None
        self.ventana_campos = None
        self.frame_espacios = None
        self.frame_disponibles = None
        self.lista_espacios = []
        self.main() # Se instancia el metodo principal

    
    #METODO PRINCPAL QUE INSTANCIA LA INTERFAZ DE USUAIO#
    def main(self):
        self.root = Tk()
        self.root.minsize(500, 600)
        self.root.config(padx=20)
        self.root.title('AVENTURA TOUR')
        self.root.resizable(0,0)

        #_________________________BOTONERA PRINCIPAL_________________________#
        lbl_encabezado = Label(self.root, text='Bienvenido al sistema aventura tour')
        lbl_encabezado.config(font=('Arial','13', 'bold'), foreground='light gray', bg='#527d94')
        lbl_encabezado.grid(row=0,column=0,columnspan=8,ipadx=250, ipady=15, pady=20)

        frame_principal = Frame(self.root,pady=0,padx=20)
        frame_principal.config(relief="ridge", bd=2)
        frame_principal.grid(row=1, column=1,rowspan=3, sticky=N)

        lbl_reserva = Label(frame_principal, text="Datos de la reserva")
        lbl_reserva.config(font= ('Arial','15', 'bold'))
        lbl_reserva.grid(row=0, columnspan = 2,column=1, pady=15)
        
        lbl_numero_reserva = Label(frame_principal, text="Número reserva:")
        lbl_numero_reserva.config(font= ('Arial','11', 'bold'))
        lbl_numero_reserva.grid(row=1, column=1,sticky=W, padx=10, pady=10)
        self.txt_numero_reserva = Entry(frame_principal,width=25)
        self.txt_numero_reserva.config(font= ('Arial','13'))
        self.txt_numero_reserva.insert(0, Coordinador_de_reservaciones().Generar_numero_reserva())
        self.txt_numero_reserva.grid(row=1, column=2,sticky=W, padx=10, pady=10)
        self.txt_numero_reserva.bind("<KeyRelease>", self.Solo_numeros)
        
        lbl_cedula = Label(frame_principal, text="Cedula:")
        lbl_cedula.config(font= ('Arial','11', 'bold'))
        lbl_cedula.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        self.txt_cedula = Entry(frame_principal,width=25)
        self.txt_cedula.config(font= ('Arial','13'))
        self.txt_cedula.grid(row=2, column=2,sticky=W, padx=10, pady=10)
        #self.txt_cedula.bind("<KeyRelease>", Validaciones().Solo_numeros)

        lbl_nombre = Label(frame_principal, text="Nombre:")
        lbl_nombre.config(font= ('Arial','11', 'bold'))
        lbl_nombre.grid(row=3, column=1,sticky=W, padx=10, pady=10)
        self.txt_nombre = Entry(frame_principal,width=25)
        self.txt_nombre.config(font= ('Arial','13'))
        self.txt_nombre.grid(row=3, column=2,sticky=W, padx=10, pady=10)
        
        lbl_cantidad_personas = Label(frame_principal, text="Cantidad:")
        lbl_cantidad_personas.config(font= ('Arial','11', 'bold'))
        lbl_cantidad_personas.grid(row=4, column=1,sticky=W, padx=10, pady=10)
        self.txt_cantidad_personas = Entry(frame_principal,width=25)
        self.txt_cantidad_personas.config(font= ('Arial','13'))
        self.txt_cantidad_personas.grid(row=4, column=2,sticky=W, padx=10, pady=10)
        self.txt_cantidad_personas.bind("<KeyRelease>", self.Solo_numeros)

        lbl_horarios = Label(frame_principal, text="Horario:")
        lbl_horarios.config(font= ('Arial','11', 'bold'))
        lbl_horarios.grid(row=5, column=1,sticky="W", padx=10, pady=10)
        horarios = Coordinador_de_catalogos().Obtener_descripcion_horarios()
        self.cmb_horarios = ttk.Combobox(frame_principal, values = horarios)
        self.cmb_horarios.config(width=23, state="readonly",font=('Arial','13'))
        self.cmb_horarios.grid(row=5, column=2,sticky=W,columnspan=2,padx=10, pady=10)

        frame_botonera_principal =  Frame(frame_principal)
        frame_botonera_principal.grid(row=6,column=1,columnspan=2,sticky=W)

        btn_agregar_reservacion = Button(frame_botonera_principal, text="Agregar reservación",font=('Arial','11','bold'), background="#74a472",foreground="white",command=self.Consultar_horario)
        btn_agregar_reservacion.grid(row=1, column=0,  sticky=W, pady=20, padx=10)

        btn_facturar = Button(frame_botonera_principal, text="Imprimir factura",font=('Arial','11','bold'), background="#7274a4",foreground="white",command=self.Imprimir_factura)
        btn_facturar.grid(row=1, column=1,  sticky=W, pady=20, padx=10) 

        btn_resetear = Button(frame_botonera_principal, text="Limpiar campos",font=('Arial','11','bold'), background="#a47272",foreground="white",command=self.Limpiar_campos)
        btn_resetear.grid(row=1, column=2,  sticky=W, pady=20, padx=10)

        btn_informe = Button(self.root, text="GENERAR INFORME",font=('Arial','13','bold'), background="#72a49a",foreground="white",command=self.Generar_informe)
        btn_informe.grid(row=2, column=1,columnspan=8, ipadx=20, ipady=10, pady=50)

        self.Generar_resumen()
        self.root.mainloop()

    def Imprimir_factura(self):
        coordinadorA = Coordinador_de_alertas()
        coordinadorR = Coordinador_de_reservaciones()
        factura = coordinadorR.Generar_factura(self.txt_cedula.get(), int(self.txt_numero_reserva.get()))
        if(factura!=''):
            coordinadorA.Mostrar_factura(factura)
        else:
            coordinadorA.Mostrar_afirmacion('no_datos')
        self.Limpiar_campos()

    def Consultar_horario(self):
        if(not self.Validar_campos()):
            Coordinador_de_alertas().Mostrar_alerta('formulario')
            return
        coordinador =  Coordinador_de_reservaciones()
        espacios_requeridos = int(self.txt_cantidad_personas.get())
        data = coordinador.Consultar_disponibilidad_por_horario(self.cmb_horarios.get())
        if(data["disponibles"] < espacios_requeridos):
            Coordinador_de_alertas().Mostrar_alerta('no_horario')
        else:
            lista_espacios = coordinador.Generar_espacios_disponibles(espacios_requeridos,data["detalle"])
            self.Modal_cargar_campos()
            self.Insertar_filas(lista_espacios)

    def Generar_resumen(self):
        if(self.frame_disponibles != None):
            self.frame_disponibles.destroy()
        coordinadorR = Coordinador_de_reservaciones()
        self.frame_disponibles = Frame(self.root,pady=0,padx=20)
        self.frame_disponibles.config(relief="ridge", bd=2)
        self.frame_disponibles.grid(row=1, column=2, sticky=E)
        lbl_detalle = Label(self.frame_disponibles, text="Disponibilidad de espacios")
        lbl_detalle.config(font= ('Arial','15', 'bold'))
        lbl_detalle.grid(row=0, column=0, columnspan = 2, pady=15)
        detalle_disponibilidad = coordinadorR.Consultar_disponibilidad_general()
        i = 1
        for recorrido in detalle_disponibilidad[:len(detalle_disponibilidad)-2]:
            lbl_horario = Label(self.frame_disponibles, text=f"Horario: {recorrido['horario']}",font=('Arial','11', 'bold'))
            lbl_horario.grid(row=i, column=0)
            lbl_tot_disponibles = Label(self.frame_disponibles, text= f"Total: {recorrido['disponibles']}",font= ('Arial','11', 'bold'))
            lbl_tot_disponibles.grid(row=i, column=1) 
            j=1
            for telef in recorrido["detalle"]:
                disp = str(telef[1])
                tot = str(telef[2])
                lbl_teleferico = Label(self.frame_disponibles, text="Teleferico: "+str(j),font= ('Arial','11'))
                lbl_teleferico.grid(row=i+1, column=0)
                lbl_disponibles = Label(self.frame_disponibles, text=f"Disponibles: {disp} / {tot}",font= ('Arial','11'))
                lbl_disponibles.grid(row=i+1, column=1)
                j+=1
                i+=1  
            i+=1


    def Solo_numeros(self,event):       
        letra = event.char
        texto = event.widget.get()
        datos_validos=['0','1','2','3','4','5','6','7','8','9','.']
        if(not(letra in datos_validos)):
            nuevo_texto=texto.replace(letra,'')
            event.widget.delete(0,END)
            event.widget.insert(0,nuevo_texto)

    def Validar_campos(self):
        return self.txt_numero_reserva.get()!= '' and self.txt_nombre.get()!='' and self.txt_cedula.get()!='' and self.txt_cantidad_personas.get()!=''
        
    def Limpiar_campos(self):
        self.txt_numero_reserva.delete(0, END)
        self.txt_numero_reserva.insert(0, Coordinador_de_reservaciones().Generar_numero_reserva()) 
        self.txt_cedula.delete(0, END)
        self.txt_nombre.delete(0, END)
        self.txt_cantidad_personas.delete(0, END)
        self.cmb_horarios.set("")     


    def Guardar_reservacion(self):
        nueva_reservacion = Reservacion()
        coordinador =  Coordinador_de_reservaciones()
        nueva_reservacion.numero_reserva = int(self.txt_numero_reserva.get())
        nueva_reservacion.cedula = self.txt_cedula.get()
        nueva_reservacion.nombre = self.txt_nombre.get()
        nueva_reservacion.cantidad_personas = int(self.txt_cantidad_personas.get())
        if(coordinador.Agregar_reservacion(nueva_reservacion)):
            coordinador.Agregar_reservaciones_espacios(self.lista_espacios)
            self.Generar_resumen()
            self.ventana_campos.destroy()
            Coordinador_de_alertas().Mostrar_afirmacion('conf_insert')
            self.Limpiar_campos()
        else:
            Coordinador_de_alertas().Mostrar_error('BD_insertar')
            self.txt_numero_reserva.delete(0, END)
            self.txt_numero_reserva.insert(0, Coordinador_de_reservaciones().Generar_numero_reserva()) 
            


    #VENTANA MODAL PARA LA CONFIGURACION DE LOS CAMPOS
    def Modal_cargar_campos(self):
            self.ventana_campos = Toplevel(self.root)
            self.ventana_campos.minsize(925,300)
            self.ventana_campos.resizable(0,0)
 
            self.frame_espacios = Frame(self.ventana_campos, padx=20, pady=15)
            self.frame_espacios.config(relief="ridge", bd=2)
            self.frame_espacios.grid(row=1, column=0, columnspan=2, sticky=N) #columnspan=8, pady=15)

            lbl_horario = Label(self.frame_espacios, text="Seleccione los tipos de tiquetes")
            lbl_horario.config(font= ('Arial','12', 'bold'))
            lbl_horario.grid(row=0,column=0, columnspan = 2)

            btn_aceptar = Button(self.frame_espacios, text="Aceptar",font=('Arial','11','bold'), background="#5dca56",foreground="white",command=self.Guardar_reservacion)
            btn_aceptar.grid(row=1, column=0,  sticky=W, pady=10)
            
            btn_cancelar = Button(self.frame_espacios, text="Cancelar", font=('Arial','11','bold'), background="#c65757", foreground="white",command=self.ventana_campos.destroy)
            btn_cancelar.grid(row=1, column=1, sticky=W, pady=10)

            lbl_horario = Label(self.frame_espacios, text="Horario", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_horario.grid(row=2, column=0, ipadx=10)

            lbl_reservacion = Label(self.frame_espacios, text="Reserva", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_reservacion.grid(row=2, column=1,ipadx=10)

            lbl_teleferico = Label(self.frame_espacios, text="Teleferico", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_teleferico.grid(row=2, column=2,ipadx=10)

            lbl_tafifa = Label(self.frame_espacios, text="Tarifa", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_tafifa.grid(row=2, column=3,ipadx=10)

            lbl_espacio = Label(self.frame_espacios, text="Espacio", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_espacio.grid(row=2, column=4,ipadx=10)

            lbl_fecha = Label(self.frame_espacios, text="Fecha", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_fecha.grid(row=2, column=5,ipadx=10)

            lbl_tipo_tiquete = Label(self.frame_espacios, text="Ticket", relief="ridge", bd=2, font=('Arial','10', 'bold'))
            lbl_tipo_tiquete.grid(row=2, column=6, ipadx=10)
        
    def Insertar_filas(self, lista_espacios):
        coordinador =  Coordinador_de_catalogos()
        self.lista_espacios.clear()
        for espacio in lista_espacios:
            id_espacio = lista_espacios.index(espacio)
            row_s=self.frame_espacios.grid_slaves()[1].grid_info()['row'] + 2

            txt_horario_cont = Entry(self.frame_espacios)#,
            txt_horario_cont.grid(row=row_s, column=0)#, ipadx=15)
            txt_horario_cont.insert(0,self.cmb_horarios.get())
            
            txt_reservacion_cont = Entry(self.frame_espacios)
            txt_reservacion_cont.grid(row=row_s, column=1)#, ipadx=20)
            txt_reservacion_cont.insert(0,self.txt_numero_reserva.get())

            txt_teleferico_cont = Entry(self.frame_espacios)
            txt_teleferico_cont.grid(row=row_s, column=2)#, ipadx=20)
            txt_teleferico_cont.insert(0,str(espacio[0]))

            self.txt_tafifa_cont = Entry(self.frame_espacios)
            self.txt_tafifa_cont.grid(row=row_s, column=3)#, ipadx=20)

            txt_espacio_cont = Entry(self.frame_espacios)
            txt_espacio_cont.grid(row=row_s, column=4)#,ipadx=20)
            txt_espacio_cont.insert(0,str(espacio[1]))
            
            txt_fecha_cont = Entry(self.frame_espacios)#),
            txt_fecha_cont.grid(row=row_s, column=5)
            txt_fecha_cont.insert(0,Funciones_generales().Fecha_actual())

            tarifas = Coordinador_de_catalogos().Obtener_descripcion_tarifas()
            self.cmb_tipo_tiquete = ttk.Combobox(self.frame_espacios, values = tarifas)
            self.cmb_tipo_tiquete.current(0)
            self.cmb_tipo_tiquete.grid(row=row_s, column=6, pady=2)
            self.cmb_tipo_tiquete.config(state="readonly")
            self.cmb_tipo_tiquete.bind("<<ComboboxSelected>>", partial(self.Editar_tarifa, self.cmb_tipo_tiquete, self.txt_tafifa_cont, id_espacio))#, self.sel_tipo_tiquete.get())) #lambda a: self.lbl_tafifa_cont.insert(0,self.sel_tipo_tiquete.get()))#self.Editar_tarifa)
            self.txt_tafifa_cont.insert(0, str(coordinador.Consultar_tarifa_por_descripcion(self.cmb_tipo_tiquete.get()).monto))

            nueva_reverva_espacio = Reservacion_espacio()
            nueva_reverva_espacio.id_horario = coordinador.Consultar_horario_por_descripcion(self.cmb_horarios.get()).id
            nueva_reverva_espacio.id_reservacion = int(self.txt_numero_reserva.get())
            nueva_reverva_espacio.id_teleferico = espacio[0]
            nueva_reverva_espacio.id_tarifa = coordinador.Consultar_tarifa_por_descripcion(self.cmb_tipo_tiquete.get()).id
            nueva_reverva_espacio.espacio_teleferico = espacio[1]
            nueva_reverva_espacio.fecha_reservacion = txt_fecha_cont.get()
            self.lista_espacios.append(nueva_reverva_espacio)

    def Editar_tarifa(self, sel, text, indice, event):
        coordinador =  Coordinador_de_catalogos()
        tarifa = coordinador.Consultar_tarifa_por_descripcion(sel.get())
        text.delete(0, END)
        text.insert(0, str(tarifa.monto))
        self.lista_espacios[indice].id_tarifa = tarifa.id



    def Generar_informe(self):
        self.ventana_informe = Toplevel(self.root)
        self.ventana_informe.minsize(925,300)
        self.ventana_informe.resizable(0,0)

        self.frame_reporte = Frame(self.ventana_informe,pady=0,padx=20)
        self.frame_reporte.config(relief="ridge", bd=2)
        self.frame_reporte.grid(row=1, column=1)

        self.frame_detalle_informe = Frame(self.frame_reporte,pady=0,padx=20)
        self.frame_detalle_informe.config(relief="ridge", bd=2)
        self.frame_detalle_informe.grid(row=1, column=1)#, sticky=E)

        lbl_detalle = Label(self.frame_detalle_informe, text="Cantidad de personas por horario/teleferico")
        lbl_detalle.config(font= ('Arial','15', 'bold'))
        lbl_detalle.grid(row=0, column=0, columnspan = 2, pady=15)

        coordinadorR = Coordinador_de_reservaciones()
        detalle_disponibilidad = coordinadorR.Consultar_disponibilidad_general()
        mayor = detalle_disponibilidad[-1]
        menor = detalle_disponibilidad[-2]
        i = 1
        for recorrido in detalle_disponibilidad[:len(detalle_disponibilidad)-2]:
            lbl_horario = Label(self.frame_detalle_informe, text=f"Horario: {recorrido['horario']}",font=('Arial','11', 'bold'))
            lbl_horario.grid(row=i, column=0)
            lbl_tot_disponibles = Label(self.frame_detalle_informe, text= f"Total ocupados: {recorrido['ocupados']}",font= ('Arial','11', 'bold'))
            lbl_tot_disponibles.grid(row=i, column=1) 
            if(recorrido['ocupados'] == mayor):
                lbl_horario_mayor = Label(self.frame_detalle_informe, text= f"->Más pasajeros",font= ('Arial','11', 'bold'),foreground="red")
                lbl_horario_mayor.grid(row=i, column=2) 
            if(recorrido['ocupados'] == menor):
                lbl_horario_menor = Label(self.frame_detalle_informe, text= f"->Menos pasajeros",font= ('Arial','11', 'bold'),foreground="blue")
                lbl_horario_menor.grid(row=i, column=2) 
            j=1
            for telef in recorrido["detalle"]:
                ocup = str(telef[0])
                tot = str(telef[2])
                lbl_teleferico = Label(self.frame_detalle_informe, text="Teleferico: "+str(j),font= ('Arial','11'))
                lbl_teleferico.grid(row=i+1, column=0)
                lbl_disponibles = Label(self.frame_detalle_informe, text=f"Ocupados: {ocup} / {tot}",font= ('Arial','11'))
                lbl_disponibles.grid(row=i+1, column=1)
                j+=1
                i+=1  
            i+=1

        self.frame_ganancias = Frame(self.frame_reporte,pady=0,padx=20)
        self.frame_ganancias.config(relief="ridge", bd=2)
        self.frame_ganancias.grid(row=1, column=2)

        lbl_detalle2 = Label(self.frame_ganancias, text="Cantidad de dinero generado por tipo-entrada")
        lbl_detalle2.config(font= ('Arial','15', 'bold'))
        lbl_detalle2.grid(row=0, column=0, columnspan = 4, pady=15)
        coordinadorC = Coordinador_de_catalogos()
        tipos_entrada = coordinadorC.Consultar_totales_tarifas()
        i = 1
        for entrada in tipos_entrada:
            lbl_tipo_entrada = Label(self.frame_ganancias, text=f"Tipo:",font=('Arial','11', 'bold'))
            lbl_tipo_entrada.grid(row=i, column=0, sticky=E)
            lbl_tipo_entrada_cont = Label(self.frame_ganancias, text=f"{entrada.descripcion}",font=('Arial','11'))
            lbl_tipo_entrada_cont.grid(row=i, column=1,sticky=W)#

            lbl_total_entrada = Label(self.frame_ganancias, text= f"Total:",font= ('Arial','11', 'bold'))
            lbl_total_entrada.grid(row=i, column=2, sticky=E)
            lbl_total_entrada_cont = Label(self.frame_ganancias, text= f"{entrada.monto}",font= ('Arial','11'))
            lbl_total_entrada_cont.grid(row=i, column=3, sticky=W)
            i+=1

        
if __name__=='__main__': #Incia el la ejecucion del sistmea
    Aventura_tour()
   
