from tkinter import *

Base =Tk()
Usuario=StringVar()
Clave= StringVar()
Base.title("Bienvenido al Sistema REGEX")
Base.config(bg="#F2F3F4",width=600, height=400)

Label(Base, text="Usuario:",bg="#F2F3F4").grid(column=0, row=0, sticky=(N, S ,E))
userEntry=Entry(Base, textvariable=Usuario)
userEntry.grid(column=1, row=0, padx=15, pady=10, columnspan=2)
Label(Base, text="Contraseña:", bg="#F2F3F4").grid(column=0, row=1,sticky=(N, S ,E))
claveEntry=Entry(Base, textvariable=Clave, show="*")
claveEntry.grid(column=1, row=1, padx=15, pady=10, columnspan=2)

botonAcceso=Button(Base, text="Ingresar")
botonAcceso.config(bg="#5DADE2",fg="#5DADE2")
botonAcceso.grid(column=2, row=3, pady=20, padx=15,sticky=(E))

userEntry.focus()
Base.mainloop()