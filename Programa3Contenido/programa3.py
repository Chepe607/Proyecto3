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

#Funciones
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

        if len (direccion_fisica.get ()) < 10 or len (direccion_fisica.get ()) > 40:
            MessageBox.showerror ("Error", "La dirección física debe ser una entre 10 y 40 caracteres")
            return False
        
        if var_automatico.get () == False and var_manual.get () == False:
            MessageBox.showerror ("Error", "Debe seleccionar al menos un tipo de cita")
            return False
        
        return True
    def generar_horas ():
        global cantidad_de_horas_mostrar
        hora_comienzo = 8
        hora_termino = 20
        duracion_citas = 20
        meses_a_considerar = 3
        hora_actual = datetime.now ()

        #Lista de las horas a mostrar:
        
        hora_actual_mod = hora_actual
        mes_termino = hora_actual.month + meses_a_considerar
        anio_termino = hora_actual.year + (mes_termino > 12)
        if mes_termino % 12 != 0:
            mes_termino = mes_termino % 12
        else:
            mes_termino = 12
        hora_termino_mod = datetime(anio_termino, mes_termino, hora_actual.day, hora_termino)
        while hora_actual_mod <= hora_termino_mod:
            if hora_comienzo <= hora_actual_mod.hour < hora_termino:
                cantidad_de_horas_mostrar.append(hora_actual_mod.strftime("%d/%m/%Y %I:%M %p"))
                
            hora_actual_mod += timedelta(minutes=duracion_citas)
            

    def mostrar_manual ():
        valor_actual_manual = var_manual.get ()
        hora_seleccionada = tk.StringVar ()


        def validar_hora_manual (hora_v): #Validación de las horas al seleccionar de manera manual
            try:
                datetime.strptime (hora_v, "%I:%M %p")
                return True
            except ValueError:
                return False
            

        def boton_confirmacion (): #Acción de guardar los datos de manera manual
            fecha_seleccionada = calendario_fecha.get_date ()
            hora_seleccionada = hora_entry.get ()

            validacion = validar_hora_manual (hora_seleccionada)
            if validacion == True:
                print ("Pasa #1", fecha_seleccionada, hora_seleccionada)
                return True, fecha_seleccionada, hora_seleccionada
            else:
                MessageBox.showerror ("Error", "Hora indicada es inválida")
                return False, -1, -1
            
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


    def mostrar_automatico ():
        valor_actual_automatico = var_automatico.get ()

        def guardar_fecha_automatico (): #Obtener el dato seleccionado del listbox
            indice_valor_seleccionado = fecha_listbox.curselection() [0]
            valor_seleccionado = fecha_listbox.get (indice_valor_seleccionado)
            print (valor_seleccionado)

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

    def bloquear_reinspeccion ():
        valor_actual_primera_vez = var_primera_vez.get ()

        if valor_actual_primera_vez == True:
            tipo_cita_reinspeccion.config (state = "disable")
        
        else:
            tipo_cita_reinspeccion.config (state = "normal")

    def bloquear_primera_vez ():
        valor_actual_reinspeccion = var_reinspeccion.get ()

        if valor_actual_reinspeccion == True:
            tipo_cita_primera_vez.config (state = "disable")
        else:
            tipo_cita_primera_vez.config (state = "normal")

    def guardar_cita ():
        validacion = validar_entries ()
        if validacion == True:
            print ("Prueba #1 PASA")
        else:
            print ("No pasa")
    



        

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
cantidad_de_horas_mostrar = []
numero_placa = tk.StringVar ()
marca_vehiculo = tk.StringVar ()
modelo = tk.StringVar ()
propetario = tk.StringVar ()
telefono = tk.StringVar ()
correo = tk.StringVar ()
direccion_fisica = tk.StringVar ()

#Variables



lista_vehiculos = ["Automóvil particular y vehículo de carga liviana (<3500kg)", "Automóvil particular y vehículo de carga liviana (3500kg - 8000kg)", "Vehículo de carga pesada y cabezales (8000kg -)", "Taxis", "Busetas", "Motocicletas", "Equipo especial de obras", "Equipo especial de agrícola"]


ventana_principal.mainloop ()




