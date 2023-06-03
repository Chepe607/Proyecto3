#Proyecto #3
#Realizado por Emmanuel Rodríguez y José Miguel González Barrantes
"""Información importante"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox

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
navegacion = tk.Label (ventana_principal, text = "Para continuar, por favor utilice las opciones de la parte superior de la ventana.", font = "Helvetica 9 bold", bg = "white")
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

def programar_citas ():
    ventana_programar_citas = tk.Toplevel ()
    ventana_programar_citas.title ("Programar una cita")
    ventana_programar_citas.geometry ("800x1000")

    tipo_cita_label = tk.Label (ventana_programar_citas, text = "Tipo de cita:", font = "Helvetica 13 bold")
ventana_principal.mainloop ()




