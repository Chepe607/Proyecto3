#Proyecto #3
#Realizado por Emmanuel Rodríguez y José Miguel González Barrantes
"""Información importante"""

from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from datetime import datetime
from email_validator import validate_email, EmailNotValidError


#Programa principal (ventana principal)
ventana_principal = tk.Tk ()
ventana_principal.title ("Menú principal ReTeVe")
ventana_principal.geometry ("480x480")
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
boton_programar_cita = tk.Button (ventana_principal, text = "Programar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: programar_citas () )
boton_programar_cita.place (x= 40, y = 230)
boton_cancelar_cita = tk.Button (ventana_principal, text = "Cancelar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: cancelar_citas () )
boton_cancelar_cita.place (x= 40, y = 330)
boton_ingresar_cita = tk.Button (ventana_principal, text = "Ingresar cita",  width = 20, height = 3, bg = "#C7D0D7", command = lambda: ingresar_citas () )
boton_ingresar_cita.place (x= 300, y = 230)
boton_tablero = tk.Button (ventana_principal, text = "Tablero revisión", width = 20, height = 3, bg = "#C7D0D7", command = lambda: tablero_revision () )
boton_tablero.place (x= 300, y = 330)

#Funciones del programa
contador_citas = 1
numero_placa = tk.StringVar ()
marca_vehiculo = tk.StringVar ()
modelo = tk.StringVar ()
propetario = tk.StringVar ()
telefono = tk.StringVar ()
correo = tk.StringVar ()

lista_vehiculos = ["Automóvil particular y vehículo de carga liviana (<3500kg)", "Automóvil particular y vehículo de carga liviana (3500kg - 8000kg)", "Vehículo de carga pesada y cabezales (8000kg -)", "Taxis", "Busetas", "Motocicletas", "Equipo especial de obras", "Equipo especial de agrícola"]
def programar_citas ():

    def es_correo_valido(correo):
        testEmail = str(correo)
        try:
            #Validar el que el coreo sea valido (Syntax)
            emailObject = validate_email(testEmail)
            testEmail = emailObject.email
            return True
        except EmailNotValidError as errorMsg:
            return False
    
    def validar_entries ():
        if len (numero_placa) > 8:
            MessageBox.showerror ("Error", "El número de placa deber estar entre 1 y 8 caracteres")
        if len (numero_placa) == 0:
            MessageBox.showerror ("Error", "Debe ingresar un número de placa")

        if len (marca_vehiculo) > 15 or len (marca_del_vehiculo) < 3:
            MessageBox.showerror ("Error", "La marca del vehículo debe ser mayor o igual a 3 caracteres y menor o igual a 15 caracteres")
        if len (marca_vehiculo) == 0:
            MessageBox.showerror ("Error", "Debe ingresar una marca de vehículo")
            
        if len (modelo) > 15:
            MessageBox.showerror ("Error", "El modelo a ingresar debe tener menos de 15 caracteres")

        if len (modelo) < 1:
            MessageBox.showerror ("Error", "Debe ingresar un modelo del medio de transporte")

        if len (propetario) > 40 or len (propetario) < 6:
            MessageBox.showerror ("Error", "El dato a ingresar del propetario debe tener una extensión entre 6 y 40 caracteres")

        

    ventana_programar_citas = tk.Toplevel ()
    ventana_programar_citas.title ("Programar una cita")
    ventana_programar_citas.geometry ("800x1000")

    #Elementos (Widgets)

    #Tipo de cita elementos
    var = tk.BooleanVar ()
    tipo_cita_label = tk.Label (ventana_programar_citas, text = "Tipo de cita:", font = "Helvetica 13 bold")
    tipo_cita_primera_vez = tk.Checkbutton (ventana_programar_citas, text = "Primera vez", variable = var)
    tipo_cita_reinspeccion = tk.Checkbutton (ventana_programar_citas, text = "Reinspección", variable = var)

    #Número de placa elementos
    numero_placa_label = tk.Label (ventana_programar_citas, text= "Número de placa:", font = "Helvetica 13 bold")
    numero_placa_entry = tk.Entry (ventana_programar_citas, textvariable = numero_placa, width = 5, font = "Helvetica 9 bold")

    #Tipo de vehículo elementos"
    tipo_vehiculo_label = tk.Label (ventana_programar_citas, text = "Tipo de vehículo:", font = "Helvetica 13 bold")
    tipo_vehiculo_combobox = ttk.Combobox (ventana_programar_citas, values = lista_vehiculos, width = 30, state = "readonly")


    #Marca del vehículo elementos
    marca_del_vehiculo_label = tk.Label (ventana_programar_citas, text = "Marca del vehículo:", font = "Helvetica 13 bold")
    marca_del_vehiculo_entry = tk.Entry (ventana_programar_citas, textvariable = marca_vehiculo, width = 5,  font = "Helvetica 9 bold")
    
    #Modelo elementos
    modelo_label = tk.Label (ventana_programar_citas, text = "Modelo:", )
    modelo_entry = tk.Entry (ventana_programar_citas, textvariable = modelo, width = 5, font = "Helvetica 9 bold" )

    #Propetario elementos
    propetario_label = tk.Label (ventana_programar_citas, text = "Propetario:", font = "Helvetica 13 bold")
    propetario_entry = tk.Entry (ventana_programar_citas, textvariable = propetario, width = 5, font = "Helvetica 9 bold")

    #Telefono elementos
    telefono_label = tk.Label (ventana_programar_citas, text = "Teléfono:", font = "Helvetica 13 bold")
    telefono_entry = tk.Entry (ventana_programar_citas, textvariable = telefono, width = 5, font = "Helvetica 9 bold")
    
    #Correo elementos
    correo_label = tk.Label (ventana_programar_citas, text = "Correo electrónico:", font = "Helvetica 13 bold")
    correo_entry = tk.Entry (ventana_programar_citas, textvariable = correo, width = 5, font = "Helvetica 9 bold")

                               
ventana_principal.mainloop ()




