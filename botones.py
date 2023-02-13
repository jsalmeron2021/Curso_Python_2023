from tkinter import *
from tkinter import ttk

window=Tk()

boton=ttk.Button(window, text='Botón de sólo texto').grid()

imagen=PhotoImage(file='img/logo_halcon16.png')
botonImagen=ttk.Button(window, image=imagen).grid()

botonCombinado=ttk.Button(window, image=imagen, compound='bottom').grid()

chkBotton=ttk.Checkbutton(window, text='Opción 1').grid()

window.mainloop()