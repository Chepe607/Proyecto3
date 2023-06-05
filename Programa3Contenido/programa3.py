#Proyecto #3
#Realizado por Emmanuel Rodríguez y José Miguel González Barrantes
"""Información importante"""

#Módulos
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from datetime import datetime, timedelta
#from email_validator import validate_email, EmailNotValidError
import validate_email


#Programa principal (ventana principal)
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
bienvenida = tk.Label (ventana_principal, text = "Bienvenido al programa de revisión de vehiculos ReTeVe", font = "Helvetica 9 bold", bg = "white")
bienvenida.place (x= 12, y = 100)
navegacion = tk.Label (ventana_principal, text = "Para continuar, por favor utilice las opciones de la parte superior o inferior de la ventana.", font = "Helvetica 9 bold", bg = "white")
navegacion.place (x= 12, y = 150)

#Botones de opciones principales
boton_programar_cita = tk.Button (ventana_principal, text = "Programar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: programar_citas())
boton_programar_cita.place (x= 40, y = 230)
boton_cancelar_cita = tk.Button (ventana_principal, text = "Cancelar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: cancelar_citas () )
boton_cancelar_cita.place (x= 40, y = 330)
boton_ingresar_cita = tk.Button (ventana_principal, text = "Ingresar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: ingresar_citas () )
boton_ingresar_cita.place (x= 300, y = 230)
boton_tablero = tk.Button (ventana_principal, text = "Tablero revisión", width = 20, height = 3, bg = "#C7D0D7", command = lambda: tablero_revision () )
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

lista_vehiculos = ["Automóvil particular y vehículo de carga liviana (<3500kg)", "Automóvil particular y vehículo de carga liviana (3500kg - 8000kg)", "Vehículo de carga pesada y cabezales (8000kg -)", "Taxis", "Busetas", "Motocicletas", "Equipo especial de obras", "Equipo especial de agrícola"]
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
        if len (numero_placa) > 8:
            MessageBox.showerror ("Error", "El número de placa deber estar entre 1 y 8 caracteres")
        if len (numero_placa) == 0:
            MessageBox.showerror ("Error", "Debe ingresar un número de placa")

        if len (marca_vehiculo) > 15 or len (marca_vehiculo) < 3:
            MessageBox.showerror ("Error", "La marca del vehículo debe ser mayor o igual a 3 caracteres y menor o igual a 15 caracteres")
        if len (marca_vehiculo) == 0:
            MessageBox.showerror ("Error", "Debe ingresar una marca de vehículo")
            
        if len (modelo) > 15:
            MessageBox.showerror ("Error", "El modelo a ingresar debe tener menos de 15 caracteres")

        if len (modelo) < 1:
            MessageBox.showerror ("Error", "Debe ingresar un modelo del medio de transporte")

        if len (propetario) > 40 or len (propetario) < 6:
            MessageBox.showerror ("Error", "El dato a ingresar del propetario debe tener una extensión entre 6 y 40 caracteres")

        if len (direccion_fisica) < 10 or len (direccion_fisica) > 40:
            MessageBox.showerror ("Error", "La dirección física debe ser una entre 10 y 40 caracteres")

    def generar_horas ():
        global cantidad_de_horas_mostrar
        hora_comienzo = 8
        hora_termino = 20
        duracion_citas = 20

        hora_actual = datetime.now ()

        #Lista de las horas a mostrar:
        if hora_comienzo <= hora_actual.hour <= hora_termino:
            hora_actual_mod = hora_actual
            hora_termino_mod = datetime.now ().replace (hour= hora_termino, minute = 0, second = 0)
            #Generar las listas de horas:
            while hora_actual_mod <= hora_termino_mod:
                cantidad_de_horas_mostrar.append (hora_actual_mod.strftime ("%d/%m/%Y %I:%M %p"))

                hora_actual_mod += timedelta(minutes = duracion_citas)
            
        print (cantidad_de_horas_mostrar)


        

    ventana_programar_citas = tk.Toplevel ()
    ventana_programar_citas.title ("Programar una cita")
    ventana_programar_citas.geometry ("900x750")

    #Elementos (Widgets)
    titulo_programar_citas = tk.Label (ventana_programar_citas, text = "Programar una cita", font = "Helvetica 20 bold")
    titulo_programar_citas.grid (row = 0, column = 0, padx = 300, pady = 40)
    instrucciones_programar_citas = tk.Label (ventana_programar_citas, text = "Para agregar una cita, agregue la información solicitada.", font = "Helvetica 13")
    instrucciones_programar_citas.place (x = 220, y = 90)
    boton = tk.Button (ventana_programar_citas, command = lambda: generar_horas ())
    boton.place (x= 500, y = 0)


    #Tipo de cita elementos
    var_primera_vez = tk.BooleanVar ()
    var_reinspeccion = tk.BooleanVar ()
    tipo_cita_label = tk.Label (ventana_programar_citas, text = "Tipo de cita:", font = "Helvetica 14 bold")
    tipo_cita_primera_vez = tk.Checkbutton (ventana_programar_citas, text = "Primera vez", variable = var_primera_vez)
    tipo_cita_reinspeccion = tk.Checkbutton (ventana_programar_citas, text = "Reinspección", variable = var_reinspeccion)
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
    manual = tk.Checkbutton (ventana_programar_citas, text = "Manual", variable = var_manual)
    automatico = tk.Checkbutton (ventana_programar_citas, text = "Automático", variable = var_automatico)
    manual.place (x= 450, y =600)
    automatico.place (x= 520, y = 600)
    if var_automatico == True and var_manual == False:
        lista_horas_listbox = tk.Variable (value = cantidad_de_horas_mostrar)
        fecha_listbox = tk.Listbox (ventana_programar_citas, listvariable= lista_horas_listbox, height = 5)
        fecha_listbox.place (x = 520, y = 750)

def acerca_de():
    MessageBox.showinfo("Acerca de", "Programa ReTeVe\nVersión del programa 1.0\
\nFecha de creación: 19/06/2023\nDesarrollado por: Emmanuel Rodríguez Rivas y Jose Miguel Gonzáles Barrantes")
    

ventana_principal.mainloop ()




