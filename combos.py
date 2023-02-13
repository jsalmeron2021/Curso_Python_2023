from tkinter import *
from tkinter import ttk

window=Tk()

estado=StringVar()

comboEstados=ttk.Combobox(window, textvariable=estado)
comboEstados.grid()
comboEstados['values']=('Jalisco', 'Nayarit', 'Baja California Sur', 'Sonora')



window.mainloop()