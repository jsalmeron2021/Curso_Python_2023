from tkinter import *
from tkinter import ttk

window=Tk()
window.title('Muestra de Widgets')
Frame1=LabelFrame(window, text='Etiquetas y Cuadros de Texto')
Frame1.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
Frame1.config(width='300', height='200',border='4', relief='groove')

ttk.Label(Frame1, text='Nombre: ').grid(row=0, column=0, sticky=(W))
Nombre=ttk.Entry(Frame1)
Nombre.grid(row=0, column=1, sticky=(W, E), padx=5)

ttk.Label(Frame1, text='A. Paterno: ').grid(row=1, column=0, sticky=(W))
aPaterno=ttk.Entry(Frame1)
aPaterno.grid(row=1, column=1, sticky=(W, E), padx=5)

ttk.Label(Frame1, text='A. Materno: ').grid(row=2, column=0, sticky=(W))
aMaterno=ttk.Entry(Frame1)
aMaterno.grid(row=2, column=1, sticky=(W, E), padx=5)

ttk.Label(Frame1, text='Correo: ').grid(row=3, column=0, sticky=(W))
correo=ttk.Entry(Frame1)
correo.grid(row=3, column=1, sticky=(W, E), padx=5)

ttk.Label(Frame1, text='Móvil: ').grid(row=4, column=0, sticky=(W))
movil=ttk.Entry(Frame1)
movil.grid(row=4, column=1, sticky=(W, E), padx=5)

Frame2=LabelFrame(window, text='Aficiones:')
Frame2.grid(row=1, column=0, padx=10, pady=6, columnspan=2, sticky=(W, E))
Frame2.config(width='300', height='120',border='2', relief='raised')
#etqAficiones=ttk.Label(Frame2, text='Aficiones: ')
#etqAficiones.grid(row=0, column=0)
Aficiones=''
chkLeer=ttk.Checkbutton(Frame2, text='Leer', textvariable=Aficiones)
chkLeer.grid(row=1, column=0)
chkMusica=ttk.Checkbutton(Frame2, text='Música', textvariable=Aficiones)
chkMusica.grid(row=1, column=1)
chkVideojuegos=ttk.Checkbutton(Frame2, text='Videojuegos', textvariable=Aficiones)
chkVideojuegos.grid(row=1, column=2, sticky=(E), pady=5)

botonGuardar=ttk.Button(window, text='Guardar')
botonGuardar.grid(row=2, column=0, sticky=(W), padx=10, pady=5)

botonCancelar=ttk.Button(window, text='Cancelar')
botonCancelar.grid(row=2, column=1, sticky=(W))
Opcion='Estados (32)'
comboEstados=ttk.Combobox(window, textvariable=Opcion)
comboEstados['values']=('elija el Estado donde radica','Baja California', 'Baja California Sur', 'Sonora', 'Sinaloa')
comboEstados.current(0)
comboEstados.grid(row=1, column=2, padx=10)

Frame3=LabelFrame(window, text='Ocupación:')
Frame3.grid(row=0, column=2, padx=10, pady=6, columnspan=2, sticky=(W, E))
Frame3.config(width='300', height='120',border='2', relief='flat')

Ocupacion=None
ttk.Radiobutton(Frame3, text='Estudiante', variable=Ocupacion, value=1).grid(sticky=(W))
ttk.Radiobutton(Frame3, text='Empleado', variable=Ocupacion, value=2).grid(sticky=(W))
ttk.Radiobutton(Frame3, text='Desempleado', variable=Ocupacion, value=3).grid(sticky=(W))

window.mainloop()