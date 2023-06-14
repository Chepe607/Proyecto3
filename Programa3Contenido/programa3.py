#Proyecto #3
#Realizado por Emmanuel Rodríguez y José Miguel González Barrantes
"""Información importante"""

#Módulos
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from datetime import datetime, timedelta
from email_validator import validate_email, EmailNotValidError
from tkcalendar import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

#Funciones
"""cant_lineas_trabajo_fija = cant_lineas_trabajo.get()
            hora_inicial_fija = hora_inicial.get()
            hora_final_fija = hora_final.get()
            minutos_cada_cita_fija = minutos_cada_cita.get()
            cant_max_dias_reinspeccion_fija = cant_max_dias_reinspeccion.get()
            fallas_graves_para_no_circular_fija = fallas_graves_para_no_circular.get()
            meses_considerados_automatico_fija = meses_considerados_automatico.get()
            porcentaje_IVA_fija = porcentaje_IVA.get()"""

def configuracion_sistema():
    global lineas_trabajo_entry, hora_inicial_entry, hora_final_entry, minutos_cada_cita_entry, cantidad_max_dias_resinspeccion_entry, fallas_graves_para_no_circular_entry, meses_considerados_automatico_entry, porcentaje_IVA_entry
    bandera_entro_configuracion = True
    cantidad_de_horas_mostrar = [ ]

    def limpiar_entradas():
        lineas_trabajo_entry.delete(0, END)
        hora_inicial_entry.delete(0, END)
        hora_final_entry.delete(0, END)
        minutos_cada_cita_entry.delete(0, END)
        cantidad_max_dias_resinspeccion_entry.delete(0, END)
        fallas_graves_para_no_circular_entry.delete(0, END)
        meses_considerados_automatico_entry.delete(0, END)
        porcentaje_IVA_entry.delete(0, END)
        tarifa_modificada_entrada.delete(0, END)

        configuracion_sistema_ventana.destroy()
    

    def guardar_informacion():
        
        if validar_entradas():
            global cant_lineas_trabajo_fija, hora_inicial_fija, hora_final_fija, minutos_cada_cita_fija, cant_max_dias_reinspeccion_fija
            global fallas_graves_para_no_circular_fija, meses_considerados_automatico_fija, porcentaje_IVA_fija
            global particular_menor_igual_3500_fija, particular_entre_3500_y_8000_fija, carga_pesada_mayor_igual_8000_fija
            global taxis_fija, buses_fija, motos_fija, equipo_obras_fija, equipo_agricola_fija

            cant_lineas_trabajo_fija = cant_lineas_trabajo.get() 
            hora_inicial_fija = hora_inicial.get()
            hora_final_fija = hora_final.get()
            minutos_cada_cita_fija = minutos_cada_cita.get()
            cant_max_dias_reinspeccion_fija = cant_max_dias_reinspeccion.get()
            fallas_graves_para_no_circular_fija = fallas_graves_para_no_circular.get()
            meses_considerados_automatico_fija = meses_considerados_automatico.get()
            porcentaje_IVA_fija = porcentaje_IVA.get()

            for i, fila in enumerate(tarifas_tv.get_children()):
                tarifas[i] = int(tarifas_tv.item(fila, "values")[0])

            particular_menor_igual_3500_fija = tarifas[0]
            particular_entre_3500_y_8000_fija = tarifas[1]
            carga_pesada_mayor_igual_8000_fija= tarifas[2]
            taxis_fija = tarifas[3]
            buses_fija = tarifas[4]
            motos_fija = tarifas[5]
            equipo_obras_fija = tarifas[6]
            equipo_agricola_fija = tarifas[7]

            limpiar_entradas()



    def validar_entradas():
        try:
            prueba = int(cant_lineas_trabajo.get())
            prueba = int(hora_inicial.get())
            prueba = int(hora_final.get())
            prueba = int(minutos_cada_cita.get())
            prueba = int(cant_max_dias_reinspeccion.get())
            prueba = int(fallas_graves_para_no_circular.get())
            prueba = int(meses_considerados_automatico.get())
            prueba = float(porcentaje_IVA.get())
            
        except:
            MessageBox.showerror("Error", "Todos los datos ingresados deben ser enteros.")
            return False
        
        if int(cant_lineas_trabajo.get()) < 0 or int(cant_lineas_trabajo.get()) > 25:
            MessageBox.showerror("Error", "La cantidad de lineas de trabajo debe ser un número entre 1 y 25.")
            return False
        
        if int(hora_inicial.get()) < 0 or int(hora_inicial.get()) > 23:
            MessageBox.showerror("Error", "La hora inicial debe ser un entero entre 0 y 23.")
            return False
        
        if int(hora_final.get()) < 0 or int(hora_final.get()) > 23 or int(hora_final.get()) < int(hora_inicial.get()):
            MessageBox.showerror("Error", "La hora final debe ser un entero entre 0 y 23, y debe ser mayor o igual a la hora inicial.")
            return False
        
        if int(minutos_cada_cita.get()) < 5 or int(minutos_cada_cita.get()) > 45:
            MessageBox.showerror("Error", "La cantidad de minutos entre cada cita debe ser un entero entre 5 y 45.")
            return False
        
        if int(cant_max_dias_reinspeccion.get()) < 1 or int(cant_max_dias_reinspeccion.get()) > 60:
            MessageBox.showerror("Error", "La cantidad máxima de días naturales para una reinspección debe ser un entero entre 1 y 60.")
            return False
        
        if int(fallas_graves_para_no_circular.get()) < 0:
            MessageBox.showerror("Error", "La cantidad máxima de fallas graves para retirar un vehículo de circulación debe ser un entero mayor a 0.")
            return False
        
        if int(meses_considerados_automatico.get()) < 1 or int(meses_considerados_automatico.get()) > 12:
            MessageBox.showerror("Error", "La cantidad de meses considerados para desplegar las citas en modo automático debe ser\n\
            un entero entre 1 y 12")
            return False
        
        if float(porcentaje_IVA.get()) < 0:
            MessageBox.showerror("Error", "El porcentaje de Impuesto al Valor Agregado sobre la tarifa debe ser un número entre\n\
            0 y 20.")
            return False
        
        return True


        

    def cambiar_tarifa(elemento):
        try:
            tarifa_nueva = int(tarifa_modificada.get())
            if tarifa_nueva <= 0:
                MessageBox.showerror("Error", "La tarifa nueva debe ser un entero mayor a 0")
                return
        except:
            MessageBox.showerror("Error", "Debe de ingresar un número mayor a 0.")
            return 
        seleccionado = elemento.focus()
        if seleccionado == "":
            MessageBox.showerror("Error", "debe de seleccionar una línea de la tabla de tarifas.")
            return 
        clave = elemento.item(seleccionado, "text")
        valor = elemento.item(seleccionado, "values")

        datos = str(clave) + ", " + str(valor[0])
        pregunta =  MessageBox.askquestion("Modificar", "Desea modificar la información seleccionada?\n" + datos)
        if pregunta == MessageBox.YES:
            elemento.set(seleccionado, column="col1", value=tarifa_nueva)

    #Ventana
    configuracion_sistema_ventana = tk.Toplevel()
    configuracion_sistema_ventana.geometry("900x900")
    configuracion_sistema_ventana.title("Configuración del sistema")
    

    #Elementos
    titulo_configuracion_sistema = Label(configuracion_sistema_ventana, text="Configuración del sistema", font="Helvetica 20 bold")
    titulo_configuracion_sistema.place(x=275, y=40)

    #Líneas de trabajo (6)
    lineas_trabajo_etiqueta = Label(configuracion_sistema_ventana, text="Cantidad de líneas de trabajo en la estación:", font="Helvetica 14 bold")
    lineas_trabajo_entry = Entry(configuracion_sistema_ventana, textvariable= cant_lineas_trabajo)
    lineas_trabajo_entry.insert(0, cant_lineas_trabajo_fija)
    lineas_trabajo_etiqueta.place(x=50, y=120)
    lineas_trabajo_entry.place(x=480, y=125)
    
    #Horario de la estación: Hora inicial (6:00 am) y hora final (9:00pm)
    horario_estacion_etiqueta = Label(configuracion_sistema_ventana, text="Horario de la estación", font="Helvetica 14 bold")
    hora_inicial_etiqueta = Label(configuracion_sistema_ventana, text="Hora inicial:", font="Helvetica 14 bold")
    hora_final_etiqueta = Label(configuracion_sistema_ventana, text="Hora final:", font="Helvetica 14 bold")
    hora_inicial_entry = Entry(configuracion_sistema_ventana, textvariable=hora_inicial)
    hora_final_entry = Entry(configuracion_sistema_ventana, textvariable=hora_final)
    hora_inicial_entry.insert(0, hora_inicial_fija)
    hora_final_entry.insert(0, hora_final_fija)
    horario_estacion_etiqueta.place(x=50, y=160)
    hora_inicial_etiqueta.place(x=90, y=190)
    hora_final_etiqueta.place(x=90, y=220)
    hora_inicial_entry.place(x=220, y=195)
    hora_final_entry.place(x=220, y=225)

    #Minutos por cada cita de revisión (20)
    minutos_cada_cita_etiqueta = Label(configuracion_sistema_ventana, text="Minutos por cada cita de revisión:", font="Helvetica 14 bold")
    minutos_cada_cita_entry = Entry(configuracion_sistema_ventana, textvariable=minutos_cada_cita)
    minutos_cada_cita_entry.insert(0, minutos_cada_cita_fija)
    minutos_cada_cita_etiqueta.place(x=50, y=260)
    minutos_cada_cita_entry.place(x=380, y=265)

    #Cantidad máxima de días naturales para reinspección (30)
    cantidad_max_dias_resinspeccion_etiqueta = Label(configuracion_sistema_ventana, text="Cantidad máxima de días naturales para reinspección:", font="Helvetica 14 bold")
    cantidad_max_dias_resinspeccion_entry = Entry(configuracion_sistema_ventana, textvariable=cant_max_dias_reinspeccion)
    cantidad_max_dias_resinspeccion_entry.insert(0, cant_max_dias_reinspeccion_fija)
    cantidad_max_dias_resinspeccion_etiqueta.place(x=50, y=300)
    cantidad_max_dias_resinspeccion_entry.place(x=570, y=305)

    #Cantidad de fallas graves para sacar vehículo de circulación (4)
    fallas_graves_para_no_circular_etiqueta = Label(configuracion_sistema_ventana, text="Cantidad de fallas graves para sacar vehículo de circulación:", font="Helvetica 14 bold")
    fallas_graves_para_no_circular_entry = Entry(configuracion_sistema_ventana, textvariable=fallas_graves_para_no_circular)
    fallas_graves_para_no_circular_entry.insert(0, fallas_graves_para_no_circular_fija)
    fallas_graves_para_no_circular_etiqueta.place(x=50, y=340)
    fallas_graves_para_no_circular_entry.place(x=630, y=345)

    #Cantidad de meses considerados para desplegar citas disponibles en la parte automática de citas (1)
    meses_considerados_automatico_etiqueta1 = Label(configuracion_sistema_ventana, text="Cantidad de meses que se van a considerar", font="Helvetica 14 bold")
    meses_considerados_automatico_etiqueta2 = Label(configuracion_sistema_ventana, text="para desplegar todas las citas disponibles", font="Helvetica 14 bold")
    meses_considerados_automatico_etiqueta3 = Label(configuracion_sistema_ventana, text="en la asignación automática de citas:", font="Helvetica 14 bold")
    meses_considerados_automatico_entry = Entry(configuracion_sistema_ventana, textvariable=meses_considerados_automatico)
    meses_considerados_automatico_entry.insert(0, meses_considerados_automatico_fija)
    meses_considerados_automatico_etiqueta1.place(x=50, y=380)
    meses_considerados_automatico_etiqueta2.place(x=50, y=405)
    meses_considerados_automatico_etiqueta3.place(x=50, y=430)
    meses_considerados_automatico_entry.place(x=405, y=435)

    #% de Impuesto al Valor agregado (IVA) sobre la tarifa (13)
    porcentaje_IVA_etiqueta = Label(configuracion_sistema_ventana, text="Porcentaje de Impuesto al Valor Agregado (IVA) sobre la tarifa:", font="Helvetica 14 bold")
    porcentaje_IVA_entry = Entry(configuracion_sistema_ventana, textvariable=porcentaje_IVA)
    porcentaje_IVA_entry.insert(0, porcentaje_IVA_fija)
    porcentaje_IVA_etiqueta.place(x=50, y=470)
    porcentaje_IVA_entry.place(x=645, y=475)

    #Tabla de tarifas
    tarifas_tv = ttk.Treeview(configuracion_sistema_ventana, columns=("col1"))
    tarifas_tv.column("#0", width=500, anchor=CENTER)
    tarifas_tv.column("col1", width=80, anchor=CENTER)

    tarifas_tv.heading("#0", text="VEHÍCULOS", anchor=CENTER)
    tarifas_tv.heading("col1", text="TARIFA", anchor=CENTER)

    tarifas_tv.insert("", END, text="Automóvil particular y vehículo de carga liviana (menor o igual a 3500 kg)", values=str(tarifas[0]))
    tarifas_tv.insert("", END, text="Automóvil particular y vehículo de carga liviana (mayor a 3500 kg pero menor a 8000 kg)", values=str(tarifas[1]))
    tarifas_tv.insert("", END, text="Vehículo de carga pesada y cabezales (mayor o igual a 8000 kg)", values=str(tarifas[2]))
    tarifas_tv.insert("", END, text="Taxis", values=str(tarifas[3]))
    tarifas_tv.insert("", END, text="Autobuses, buses y microbuses", values=str(tarifas[4]))
    tarifas_tv.insert("", END, text="Motocicletas", values=str(tarifas[5]))
    tarifas_tv.insert("", END, text="Equipo especial de obras", values=str(tarifas[6]))
    tarifas_tv.insert("", END, text="Equipo especial agrícola (maquinaria agrícola)", values=str(tarifas[7]))

    tarifas_tv.place(x=50, y=550)

    #Botón cambiar tarifa
    cambiar = Button(configuracion_sistema_ventana, text="Cambiar tarifa", font="Helvetica 10 bold", bg="brown", command=lambda: cambiar_tarifa(tarifas_tv))
    cambiar.place(x=710, y=647)

    #Entrada para modificar tarifa
    tarifa_modificada_entrada = Entry(configuracion_sistema_ventana, textvariable=tarifa_modificada)
    tarifa_modificada_entrada.place(x=700, y=625)

    #Texto para mostrar donde se cambia la tarifa
    tarifa_nueva_etiqueta = Label(configuracion_sistema_ventana, text="Tarifa nueva", font="Helvetica 14 bold")
    tarifa_nueva_etiqueta.place(x=700, y=595)

    #Botones guardar configuración y volver atrás
    guardar_config_boton = Button(configuracion_sistema_ventana, text="Guardar configuración", font="Helvetica 10 bold", bg="#08f26e", width=22, height=4, command=lambda: guardar_informacion())
    volver_atras_boton = Button(configuracion_sistema_ventana, text="Volver atrás", font="Helvetica 10 bold", bg="#ff3333", width=22, height=4, command=lambda: limpiar_entradas())     
    guardar_config_boton.place(x=200, y=800)
    volver_atras_boton.place(x=500, y=800)

    


    configuracion_sistema_ventana.mainloop()



def programar_citas ():
    global cantidad_de_horas_mostrar

    def es_correo_valido(correo): #Validar que el correo electrónico sea válido
        testEmail = str(correo)
        try:
            #Validar el que el coreo sea valido (Syntax)
            emailObject = validate_email(testEmail)
            testEmail = emailObject.email
            return True
        except EmailNotValidError as errorMsg:
            return False
    
    def validar_entries (): #Restricciones de los datos
        if var_primera_vez.get () == False and var_reinspeccion.get () == False:
            MessageBox.showerror ("Error", "Debe seleccionar al menos un tipo de cita")
            return False

        if len (numero_placa.get ()) > 8:
            MessageBox.showerror ("Error", "El número de placa deber estar entre 1 y 8 caracteres")
            return False
            
        if len (numero_placa. get()) == 0:
            MessageBox.showerror ("Error", "Debe ingresar un número de placa")
            return False
        
        if len (tipo_vehiculo_combobox.get ()) == 0:
            MessageBox.showerror ("Error", "Debe ingresar un tipo de vehículo")
            return False
        
        if len (marca_vehiculo.get ()) > 15 or len (marca_vehiculo.get ()) < 3:
            MessageBox.showerror ("Error", "La marca del vehículo debe ser mayor o igual a 3 caracteres y menor o igual a 15 caracteres")
            return False
        
        if len (marca_vehiculo.get ()) == 0:
            MessageBox.showerror ("Error", "Debe ingresar una marca de vehículo")
            return False
            
        if len (modelo.get ()) > 15:
            MessageBox.showerror ("Error", "El modelo a ingresar debe tener menos de 15 caracteres")
            return False

        if len (modelo.get ()) < 1:
            MessageBox.showerror ("Error", "Debe ingresar un modelo del medio de transporte")
            return False

        if len (propetario.get ()) > 40 or len (propetario.get ()) < 6:
            MessageBox.showerror ("Error", "El dato a ingresar del propetario debe tener una extensión entre 6 y 40 caracteres")
            return False
        
        if len (telefono.get ()) != 20:
            MessageBox.showerror ("Error", "Debe ingresar un número de teléfono de 20 caracteres")
            return False

        correo = correo_entry.get ()
        validacion_correo = es_correo_valido (correo)
        
        if validacion_correo == False:
            MessageBox.showerror ("Error", "El correo electrónico ingresado no es válido")
            return False

        if len (direccion_fisica.get ()) < 10 or len (direccion_fisica.get ()) > 40:
            MessageBox.showerror ("Error", "La dirección física debe ser una entre 10 y 40 caracteres")
            return False
        
        if var_automatico.get () == False and var_manual.get () == False:
            MessageBox.showerror ("Error", "Debe seleccionar al menos un tipo de asignación de fecha y hora")
            return False
        
        return True
    
    def generar_horas (): #Generar los valores de las horas dependiendo y teniendo en cuenta la configuración default
        hora_actual = datetime.now ()

        #Lista de las horas a mostrar:
        if bandera_entro_configuracion == True:
            hora_actual_mod = hora_actual
            mes_termino = hora_actual.month + int (meses_considerados_automatico_entry.get())
            anio_termino = hora_actual.year + (mes_termino > 12)
            if mes_termino % 12 != 0:
                mes_termino = mes_termino % 12
            else:
                mes_termino = 12
            hora_termino_mod = datetime(anio_termino, mes_termino, hora_actual.day, hora_final_entry.get())
            while hora_actual_mod <= hora_termino_mod:
                if int (hora_inicial_entry.get ()) <= hora_actual_mod.hour < int (hora_final_entry.get ()):
                    cantidad_de_horas_mostrar.append(hora_actual_mod.strftime("%d/%m/%Y %I:%M %p"))
                    
                hora_actual_mod += timedelta(minutes=minutos_cada_cita_entry.get ())
        else:
            hora_actual_mod = hora_actual
            mes_termino = hora_actual.month + int (meses_considerados_automatico_fija)
            anio_termino = hora_actual.year + (mes_termino > 12)
            if mes_termino % 12 != 0:
                mes_termino = mes_termino % 12
            else:
                mes_termino = 12
            hora_termino_mod = datetime(anio_termino, mes_termino, hora_actual.day, int (hora_final_fija))
            while hora_actual_mod <= hora_termino_mod:
                if int (hora_inicial_fija) <= hora_actual_mod.hour < int (hora_final_fija):
                    cantidad_de_horas_mostrar.append(hora_actual_mod.strftime("%d/%m/%Y %I:%M %p"))
                    
                hora_actual_mod += timedelta(minutes=int (minutos_cada_cita_fija))
            

    def mostrar_manual (): #Mostrar ventana al seleccionar la opcion de manual
        global hora_entry, calendario_fecha, valor_seleccionado_manual

        MessageBox.showinfo ("Información a considerar", "A la hora de realizar la escogencia de la fecha y hora, no cierre esta ventana hasta que guarde la cita correspondiente")

        valor_actual_manual = var_manual.get ()
        hora_seleccionada = tk.StringVar ()


        def validar_hora_manual (hora_v): #Validación de las horas al seleccionar de manera manual
            try:
                datetime.strptime (hora_v, "%I:%M %p")
                return True
            except ValueError:
                return False
            
        def boton_confirmacion (): #Acción de guardar los datos de manera manual
            global valor_seleccionado_manual, hora_seleccionada, fecha_seleccionada
            fecha_seleccionada = calendario_fecha.get_date ()
            hora_seleccionada = hora_entry.get ()

            validacion = validar_hora_manual (hora_seleccionada)
            if validacion == True:
                print ("Pasa #1", fecha_seleccionada, hora_seleccionada)
                valor_seleccionado_manual = str (fecha_seleccionada) + " " + str (hora_seleccionada)
                return valor_seleccionado_manual, hora_seleccionada
            else:
                MessageBox.showerror ("Error", "Hora indicada es inválida")
                valor_seleccionado_manual = False
                return valor_seleccionado_manual
                
        if valor_actual_manual == True:
            automatico.config (state = "disable")
            ventana_manual = tk.Toplevel ()
            ventana_manual.geometry ("700x550")
            ventana_manual.title ("Selección manual de fecha y hora")


            manual_label = tk.Label (ventana_manual, text = "Asignación de fecha y hora", font = "Helvetica 15 bold")
            manual_label.place (x = 200, y = 30)
            manual_label_instruccion = tk.Label (ventana_manual, text = "Seleccione la fecha y hora deseada para su cita; utilice el botón de abajo para confirmar la selección.", font = "Helvetica 10")
            manual_label_instruccion.place (x = 58, y = 70)
            fecha_label = tk.Label (ventana_manual, text= "Seleccione la fecha deseada:", font = "Helvetica 13 bold")
            fecha_label.place (x = 58, y = 150)

            fecha_actual = datetime.now ()

            calendario_fecha = Calendar(ventana_manual, year = fecha_actual.year, month = fecha_actual.month, day = fecha_actual.day , mindate = fecha_actual, date_pattern = "dd/mm/yyyy")
            calendario_fecha.place (x = 50, y = 200)

            hora_label = tk.Label (ventana_manual, text = "Seleccione la hora deseada:", font = "Helvetica 13 bold")
            hora_label.place (x = 390, y = 150)
            hora_entry = tk.Entry (ventana_manual, textvariable = hora_seleccionada, font = "Helvetica 12", width = 25, justify = "center")
            hora_entry.place (x= 390, y = 200 )

            boton_confirmacion_manual = tk.Button (ventana_manual, text = "Confirmar cita", font = "Helvetica 12 bold", width = 15, height = 3, bg= "#08f26e", command = lambda: boton_confirmacion ())
            boton_confirmacion_manual.place (x = 250, y = 420)

            

        else:
            automatico.config (state = "normal")


    def mostrar_automatico (): #Mostrar ventana al seleccionar la opcion de automático
        global valor_seleccionado_automatico
        MessageBox.showinfo ("Información a considerar", "A la hora de realizar la escogencia de la fecha y hora, no cierre esta ventana hasta que guarde la cita correspondiente")
        valor_actual_automatico = var_automatico.get ()

        def guardar_fecha_automatico (): #Obtener el dato seleccionado del listbox
            global valor_seleccionado_automatico
            indice_valor_seleccionado = fecha_listbox.curselection() [0]
            valor_seleccionado_automatico = fecha_listbox.get (indice_valor_seleccionado)
            ####FALTA VALORAR LA DISPONIBILIDAD DE LAS CITAS
            print (valor_seleccionado_automatico)

        if valor_actual_automatico == True:
            manual.config (state = "disable")
            generar_horas () #Se generan las horas

            ventana_automatico = tk.Toplevel () #Ventana a mostrar
            ventana_automatico.title ("Selección automática de fecha y hora")
            ventana_automatico.geometry ("300x300")

            lista_horas_listbox = tk.Variable (value = cantidad_de_horas_mostrar) #Lista de las citas 
            fecha_listbox = tk.Listbox (ventana_automatico, listvariable= lista_horas_listbox, height = 10,borderwidth = 2, relief = "sunken") #Generar el listbox
            fecha_listbox.place (x= 80, y = 80 )
            scrollbar_listbox = ttk.Scrollbar(ventana_automatico, orient = "vertical", command = fecha_listbox.yview)
            
            scrollbar_listbox.place (x= 200, y = 80, height = 160) #Generar el scrollbar
            fecha_listbox["yscrollcommand"] = scrollbar_listbox.set

            #Elemenos extra:
            automatico_label = tk.Label (ventana_automatico, text = "Asignación automática fecha/hora", font = "Helvetica 12 bold")
            automatico_label.place (x= 20, y = 30)
            automatico_instruccion = tk.Label (ventana_automatico, text = "Seleccione de la lista la fecha y hora de la cita", font = "Helvetica 10")
            automatico_instruccion.place (x = 15, y = 55)

            boton_confirmacion = tk.Button (ventana_automatico, text = "Confirmar cita", font = "Helvetica 10 bold", bg = "#08f26e", command = lambda: guardar_fecha_automatico ())
            boton_confirmacion.place (x = 90, y = 260)

        else:
            manual.config (state = "normal")

    def validar_fechas_horas ():
        if valor_seleccionado_manual == None and valor_seleccionado_automatico == None:
            MessageBox.showerror ("Error", "Dentro de las opciones de manual y automático, debe seleccionar fecha y hora")
            return False
        else:
            return True

    def bloquear_reinspeccion (): #Bloquear opcion reinspeccion
        valor_actual_primera_vez = var_primera_vez.get ()

        if valor_actual_primera_vez == True:
            tipo_cita_reinspeccion.config (state = "disable")
        
        else:
            tipo_cita_reinspeccion.config (state = "normal")

    def bloquear_primera_vez (): #Bloquear opcion reinspeccion
        valor_actual_reinspeccion = var_reinspeccion.get ()

        if valor_actual_reinspeccion == True:
            tipo_cita_primera_vez.config (state = "disable")
        else:
            tipo_cita_primera_vez.config (state = "normal")

    def guardar_cita (): #Guardar valores de las citas
        validacion = validar_entries ()
        if validacion == True:
            validacion2 = validar_fechas_horas ()
            if validacion2 == True:

                mandar_correo (correo_entry.get())
                tipo_cita_primera_vez_f = var_primera_vez.get ()
                tipo_cita_reinspeccion_f = var_manual.get ()

                if tipo_cita_primera_vez_f == True:
                    tipo_cita_f = "Primera vez"
                elif tipo_cita_reinspeccion_f == True:
                    tipo_cita_f = "Reinspección"

                numero_placa_f = numero_placa_entry.get ()
                tipo_de_vehiculo_f = tipo_vehiculo_combobox.get ()
                marca_del_vehiculo_f = marca_del_vehiculo_entry.get ()
                modelo_f = modelo_entry.get ()
                propetario_f = propetario_entry.get ()
                telefono_f = telefono_entry.get ()
                correo_f = correo_entry.get ()
                direccion_fisica_f = direccion_fisica_entry.get ()
                estado_f = "PENDIENTE"
                if var_automatico.get () == True:
                    final = [contador_citas, tipo_cita_f, numero_placa_f, tipo_de_vehiculo_f, marca_del_vehiculo_f, modelo_f, propetario_f, telefono_f, correo_f, direccion_fisica_f, valor_seleccionado_automatico, estado_f]
                elif var_manual.get () == True:
                    final = [contador_citas, tipo_cita_f, numero_placa_f, tipo_de_vehiculo_f, marca_del_vehiculo_f, modelo_f, propetario_f, telefono_f, correo_f, direccion_fisica_f, valor_seleccionado_manual, estado_f]
                print (agregar_cita (citas, final))
            
            else:
                MessageBox.showerror ("Error", "Las fechas u horas son inválidas o no se ingreso ningúna")
                return
        else:
            MessageBox.showerror ("Error", "La información ingresada en los campos en blanco no son validos")
            return
            
    def agregar_cita(citas, cita):
        if citas == []:
            nodo = [cita]
            hijo_izquierdo = [[]]
            return nodo + hijo_izquierdo
        else:
            return agregar_cita_aux(citas, cita)
    
    def agregar_cita_aux(nodo, cita):
        if len(nodo) == 2:
            hoja = [cita]
            return nodo + [[cita, []]]
        else:
            return nodo[:2] + [agregar_cita_aux(nodo[-1], cita)]
    
    def mandar_correo (correo):
        if var_manual.get () == True:
            #fecha_seleccionada = calendario_fecha.get_date ()
            #hora_seleccionada = hora_entry.get ()
            pass

        #Definir credenciales del servidos SMTP
        if "gmail" in correo:
            smtp_port = 587
            smtp_server = "smtp.gmail.com"

        elif "hotmail" or "outlook" in correo:
            smtp_port = 587
            smtp_server = "smtp.live.com"


        #Información del correo
        correo_from = "josemiguel4484@gmail.com"
        correo_to = correo
        titulo = "Revisión Técnica de Vehículos (ReTeVe) / Cita Información Importante"
        clave_from = "xxvnbsyriavzxhep"

        #Creación del objeto MIME para definir las partes del correo
        msg = MIMEMultipart ()
        msg['From'] = correo_from
        msg['To'] = correo_to
        msg['Subject'] = titulo
        
        #Construcción del correo
        if var_manual.get () == True:
            body = f"""Saludos usuario, se le envió este correo electrónico debido a la solicitud de revisión técnica vehícular a nombre de esta dirección electrónica. Tome en cuenta que su cita será el día y hora respectivamente""" + " " + str(fecha_seleccionada) + " " + str(hora_seleccionada) 

        elif var_automatico.get () == True:
            body = f"""Saludos usuario, se le envió este correo electrónico debido a la solicitud de revisión técnica vehícular a nombre de esta dirección electrónica. Tome en cuenta que su cita será el día y hora respectivamente""" + " " + str (valor_seleccionado_automatico)


        #Agregar el cuerpo del correo en el mensaje
        msg.attach (MIMEText (body, 'plain'))

        
        text = msg.as_string ()

        #Connectar con el servidor
        TIE_server = smtplib.SMTP (smtp_server, smtp_port, timeout = 60 )
        TIE_server.starttls ()
        TIE_server.login(correo_from, clave_from)


        TIE_server.sendmail (correo_from, correo_to, text) #Enviar el correo
        TIE_server.quit () #Salir del servidor



        

    ventana_programar_citas = tk.Toplevel ()
    ventana_programar_citas.title ("Programar una cita")
    ventana_programar_citas.geometry ("900x750")

    #Elementos (Widgets)
    titulo_programar_citas = tk.Label (ventana_programar_citas, text = "Programar una cita", font = "Helvetica 20 bold")
    titulo_programar_citas.grid (row = 0, column = 0, padx = 300, pady = 40)
    instrucciones_programar_citas = tk.Label (ventana_programar_citas, text = "Para agregar una cita, agregue la información solicitada.", font = "Helvetica 13")
    instrucciones_programar_citas.place (x = 220, y = 90)


    #Tipo de cita elementos
    var_primera_vez = tk.BooleanVar ()
    var_reinspeccion = tk.BooleanVar ()
    tipo_cita_label = tk.Label (ventana_programar_citas, text = "Tipo de cita:", font = "Helvetica 14 bold")
    tipo_cita_primera_vez = tk.Checkbutton (ventana_programar_citas, text = "Primera vez", variable = var_primera_vez, command = lambda : bloquear_reinspeccion ())
    tipo_cita_reinspeccion = tk.Checkbutton (ventana_programar_citas, text = "Reinspección", variable = var_reinspeccion, command = lambda : bloquear_primera_vez ())
    tipo_cita_label.place (x = 220, y = 160)
    tipo_cita_primera_vez.place (x = 220, y = 200)
    tipo_cita_reinspeccion.place (x = 325, y = 200)


    #Número de placa elementos
    numero_placa_label = tk.Label (ventana_programar_citas, text= "Número de placa:", font = "Helvetica 14 bold")
    numero_placa_entry = tk.Entry (ventana_programar_citas, textvariable = numero_placa, width = 15, font = "Helvetica 12")
    numero_placa_label.place (x = 220, y = 260)
    numero_placa_entry.place (x = 220, y = 300)


    #Tipo de vehículo elementos"
    tipo_vehiculo_label = tk.Label (ventana_programar_citas, text = "Tipo de vehículo:", font = "Helvetica 14 bold")
    tipo_vehiculo_combobox = ttk.Combobox (ventana_programar_citas, values = lista_vehiculos, width = 30, state = "readonly")
    tipo_vehiculo_label.place (x= 220, y= 360)
    tipo_vehiculo_combobox.place (x= 220, y = 400)

    #Marca del vehículo elementos
    marca_del_vehiculo_label = tk.Label (ventana_programar_citas, text = "Marca del vehículo:", font = "Helvetica 14 bold")
    marca_del_vehiculo_entry = tk.Entry (ventana_programar_citas, textvariable = marca_vehiculo, width = 15,  font = "Helvetica 12")
    marca_del_vehiculo_label.place (x= 220, y=  460)
    marca_del_vehiculo_entry.place (x= 220, y= 500)

    #Modelo elementos
    modelo_label = tk.Label (ventana_programar_citas, text = "Modelo:", font = "Helvetica 14 bold" )
    modelo_entry = tk.Entry (ventana_programar_citas, textvariable = modelo, width = 15, font = "Helvetica 12" )
    modelo_label.place (x= 220, y= 560)
    modelo_entry.place (x= 220, y= 600)

    #Propetario elementos
    propetario_label = tk.Label (ventana_programar_citas, text = "Propetario:", font = "Helvetica 14 bold")
    propetario_entry = tk.Entry (ventana_programar_citas, textvariable = propetario, width = 20, font = "Helvetica 12 ")
    propetario_label.place (x = 450, y = 160)
    propetario_entry.place (x = 450, y = 200)

    #Telefono elementos
    telefono_label = tk.Label (ventana_programar_citas, text = "Teléfono:", font = "Helvetica 14 bold")
    telefono_entry = tk.Entry (ventana_programar_citas, textvariable = telefono, width = 20, font = "Helvetica 12")
    telefono_label.place (x = 450, y =  260)
    telefono_entry.place (x = 450, y = 300)

    #Correo elementos
    correo_label = tk.Label (ventana_programar_citas, text = "Correo electrónico:", font = "Helvetica 14 bold")
    correo_entry = tk.Entry (ventana_programar_citas, textvariable = correo, width = 20, font = "Helvetica 12")
    correo_label.place (x = 450, y = 360)
    correo_entry.place (x = 450, y = 400)

    #Dirección física elementos
    direccion_fisica_label = tk.Label (ventana_programar_citas, text = "Dirección física:", font = "Helvetica 14 bold")
    direccion_fisica_entry = tk.Entry (ventana_programar_citas, text = direccion_fisica, font = "Helvetica 9", width = 25)
    direccion_fisica_label.place (x = 450, y = 460)
    direccion_fisica_entry.place (x = 450, y = 500)

    #Fecha y hora de las citas
    
    fecha_label = tk.Label (ventana_programar_citas, text = "Fecha y hora", font = "Helvetica 14 bold")
    fecha_label.place (x= 450, y = 560)

    var_automatico = tk.BooleanVar ()
    var_manual = tk.BooleanVar ()
    manual = tk.Checkbutton (ventana_programar_citas, text = "Manual", variable = var_manual, command = lambda : mostrar_manual ())
    automatico = tk.Checkbutton (ventana_programar_citas, text = "Automático", variable = var_automatico, command = lambda : mostrar_automatico ())
    manual.place (x= 450, y =600)
    automatico.place (x= 520, y = 600)

    #Agendar cita o cancelar elementos:
    boton_guardar = tk.Button (ventana_programar_citas, text = "Agendar la cita", font = "Helvetica 10 bold", bg = "#08f26e", width =  23, height = 3, command = lambda: guardar_cita ())
    boton_guardar.place (x = 220, y = 650)

    boton_cancelar = tk.Button (ventana_programar_citas, text = "Cancelar asignación de cita", font = "Helvetica 10 bold", bg = "#ff3333", height = 3, command = lambda: ventana_programar_citas.destroy () )
    boton_cancelar.place (x = 450, y = 650)

def cancelar_citas ():
    def modificar_estado_cita_cancelada (citas, numero_cita, numero_placa):
        global bandera_encontrar
        bandera_encontrar = False
        numero_cita = eval (numero_cita)
        numero_placa = str (numero_placa)
        if numero_cita == "" or numero_placa == "":
            MessageBox.showerror ("Error", "Porfavor llene todos los campos solicitados")
            return
        
        print (modificar_estado_cita_cancelada_aux (citas, numero_cita, numero_placa))


        if not bandera_encontrar:
            MessageBox.showerror ("Error", "No se encontró la cita con los datos solicitados")
            return
        
    def modificar_estado_cita_cancelada_aux (citas, numero_cita, numero_placa):
        global bandera_encontrar
        if citas == []:
            return []
    
        elif isinstance (citas [0], list):
            if not ((citas [0]) == []) and numero_cita == citas [0] [0] and citas [0] [-1] == "PENDIENTE" and numero_placa == citas [0] [2]:
                citas [0] [-1] = "CANCELADA"
                bandera_encontrar = True
            return [modificar_estado_cita_cancelada_aux (citas [0], numero_cita, numero_placa)] + modificar_estado_cita_cancelada_aux (citas [1:], numero_cita, numero_placa)

        else:
            return [citas [0]] + modificar_estado_cita_cancelada_aux (citas [1:], numero_cita, numero_placa)
    
    ventana_cancelar_citas = tk.Toplevel ()
    ventana_cancelar_citas.geometry ("600x350")

    #Elementos de Bienvenida
    label_principal_cancelar_citas = tk.Label (ventana_cancelar_citas, text = "Cancelar cita", font = "Helvetica 20 bold")
    label_principal_cancelar_citas.place (x= 200, y = 40)
    instruccion_cancelar_citas = tk.Label (ventana_cancelar_citas, text = "Ingrese en los campos en blanco sus datos correspondientes", font = "Helvetica 13")
    instruccion_cancelar_citas.place (x= 75, y = 85)

    #Elementos de la cita
    numero_cita_label_cancelar = tk.Label (ventana_cancelar_citas, text = "Número de cita:", font = "Helvetica 14 bold")
    numero_cita_label_cancelar.place (x = 70, y = 140)
    numero_placa_label_cancelar = tk.Label (ventana_cancelar_citas, text = "Número de placa:", font = "Helvetica 14 bold")
    numero_placa_label_cancelar.place (x = 360, y = 140)
    numero_cita_entry_cancelar = tk.Entry (ventana_cancelar_citas, textvariable = contador_citas_cancelar, font = "Helvetica 12", width = 16, justify = "center")
    numero_cita_entry_cancelar.place (x = 75, y = 190)
    numero_placa_entry_cancelar = tk.Entry (ventana_cancelar_citas, textvariable = numero_placa_cancelar, font = "Helvetica 12", width = 18, justify = "center")
    numero_placa_entry_cancelar.place (x = 360, y = 190)

    boton_cancelar_cita = tk.Button (ventana_cancelar_citas, text = "Cancelar cita", font = "Helvetica 10 bold" , width = 23, height = 3, bg = "#08f26e", command = lambda: modificar_estado_cita_cancelada (citas, numero_cita_entry_cancelar.get (), numero_placa_entry_cancelar.get ()))
    boton_cancelar_cita.place (x = 195, y = 260)






def acerca_de():
    MessageBox.showinfo("Acerca de", "Programa ReTeVe\nVersión del programa 1.0\
\nFecha de creación: 19/06/2023\nDesarrollado por: Emmanuel Rodríguez Rivas y Jose Miguel González Barrantes")
    


#---------------------------Programa principal (ventana principal) ----------------------------
ventana_principal = tk.Tk ()
ventana_principal.title ("Menú principal ReTeVe")
ventana_principal.geometry ("540x480")
ventana_principal.config (bg= "white")



#Menú de barra de la ventana principal
menuBarra = Menu(ventana_principal)
menuBarra.add_command (label = "Lista de Fallas", command = lambda: lista_de_fallas ())
menuBarra.add_command (label = "Configuración del sistema", command = lambda: configuracion_sistema ())
menuBarra.add_command (label = "Ayuda", command = lambda: ayuda ())
menuBarra.add_command (label = "Acerca de", command= lambda: acerca_de ())
menuBarra.add_command (label= "Salir", command = lambda: salir ())
ventana_principal.config (menu = menuBarra)

#Elementos ventana principal
bienvenida_menu = tk.Label (ventana_principal, text = "Menú ReTeVe: Revisión Técnica de Vehículos", font = "Helvetica 15 bold", bg = "white")
bienvenida_menu.place (x= 12, y = 50)
bienvenida = Label (ventana_principal, text = "Bienvenido al programa de revisión de vehiculos ReTeVe", font = "Helvetica 9 bold", bg = "white")
bienvenida.place (x= 12, y = 100)
navegacion = tk.Label (ventana_principal, text = "Para continuar, por favor utilice las opciones de la parte superior o inferior de la ventana.", font = "Helvetica 9 bold", bg = "white")
navegacion.place (x= 12, y = 150)

#Botones de opciones principales
boton_programar_cita = tk.Button (ventana_principal, text = "Programar cita", font = "Helvetica 10 bold", width = 20, height = 3, bg = "#C7D0D7", command = lambda: programar_citas())
boton_programar_cita.place (x= 70, y = 230)
boton_cancelar_cita = tk.Button (ventana_principal, text = "Cancelar cita",font = "Helvetica 10 bold",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: cancelar_citas () )
boton_cancelar_cita.place (x= 70, y = 330)
boton_ingresar_cita = tk.Button (ventana_principal, text = "Ingresar cita",font = "Helvetica 10 bold",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: ingresar_citas () )
boton_ingresar_cita.place (x= 300, y = 230)
boton_tablero = tk.Button (ventana_principal, text = "Tablero revisión",font = "Helvetica 10 bold", width = 20, height = 3, bg = "#C7D0D7", command = lambda: tablero_revision () )
boton_tablero.place (x= 300, y = 330)

#Funciones del programa
contador_citas = 1
bandera_entro_configuracion = False
cantidad_de_horas_mostrar = []

citas = [[1, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], 
            [[2, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], []]]

valor_seleccionado_manual = None
valor_seleccionado_automatico = None
numero_placa_cancelar = tk.StringVar ()
contador_citas_cancelar = tk.StringVar ()
numero_placa = tk.StringVar ()
marca_vehiculo = tk.StringVar ()
modelo = tk.StringVar ()
propetario = tk.StringVar ()
telefono = tk.StringVar ()
correo = tk.StringVar ()
direccion_fisica = tk.StringVar ()

cant_lineas_trabajo = StringVar()
hora_inicial = StringVar()
hora_final = StringVar()
minutos_cada_cita = StringVar() 
cant_max_dias_reinspeccion = StringVar()
fallas_graves_para_no_circular = StringVar() 
meses_considerados_automatico = StringVar()
porcentaje_IVA= StringVar()
tarifa_modificada = StringVar()

"""particular_menor_igual_3500 = 
particular_entre_3500_y_8000 = 
carga_pesada_mayor_igual_8000= 
taxis = 
buses = 
motos = 
equipo_obras = 
equipo_agricola = """


#Variables fijas de la configuración
cant_lineas_trabajo_fija = 6
hora_inicial_fija = 6
hora_final_fija = 21
minutos_cada_cita_fija = 20 
cant_max_dias_reinspeccion_fija = 30
fallas_graves_para_no_circular_fija = 4 
meses_considerados_automatico_fija = 1
porcentaje_IVA_fija = 13.0
particular_menor_igual_3500_fija = 10920
particular_entre_3500_y_8000_fija = 14380
carga_pesada_mayor_igual_8000_fija= 14380
taxis_fija = 11785
buses_fija = 14380
motos_fija = 7195
equipo_obras_fija = 14380
equipo_agricola_fija = 6625

tarifas = [particular_menor_igual_3500_fija, particular_entre_3500_y_8000_fija, carga_pesada_mayor_igual_8000_fija,
           taxis_fija, buses_fija, motos_fija, equipo_obras_fija, equipo_agricola_fija]

lista_vehiculos = ["Automóvil particular y vehículo de carga liviana (<3500kg)", "Automóvil particular y vehículo de carga liviana (3500kg - 8000kg)", "Vehículo de carga pesada y cabezales (8000kg -)", "Taxis", "Busetas", "Motocicletas", "Equipo especial de obras", "Equipo especial de agrícola"]


ventana_principal.mainloop ()




