#Proyecto #3
#Realizado por Emmanuel Rodríguez y José Miguel González Barrantes
"""Información importante"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox

#Programa principal (ventana principal)
ventana_principal = tk.Tk ()
ventana_principal.title ("Menú principal ReTeVe")
ventana_principal.geometry ("500x500")


#Menú de barra de la ventana principal
menuBarra = Menu(ventana_principal)
menuBarra.add_command (label= "Programar citas", command= lambda: programar_citas () )
menuBarra.add_command (label = "Cancelar citas", command= lambda: cancelar_citas ())
menuBarra.add_command (label = "Ingreso a citas", command = lambda : ingresar_cita ())
menuBarra.add_command (label = "Tablero de revisión", command = lambda: tablero_revision ())
menuBarra.add_command (label = "Lista de Fallas", command = lambda: lista_de_fallas ())
menuBarra.add_command (label = "Configuración del sistema", command = lambda: configuracion_sistema ())
menuBarra.add_command (label = "Ayuda", command = lambda: ayuda ())
menuBarra.add_command (label = "Acerca de", command= lambda: acerca_de ())
menuBarra.add_command (label= "Salir", command = lambda: salir ())




