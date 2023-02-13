from tkinter import *
from tkinter import ttk

window=Tk()
icono=PhotoImage(file='img/logo_halcon.png')
window.iconphoto(True, icono)
etqTexto=ttk.Label(window, text='Etiqueta de sólo texto ')
etqTexto.grid()

imagen=PhotoImage(file='img/logo_halcon.png')

etqImagen=ttk.Label(window, image=imagen).grid()
#etqImagen['image']=imagen

etqCombinada=ttk.Label(window, text='etiqueta combinada',compound='center', image=imagen).grid()


window.mainloop()

