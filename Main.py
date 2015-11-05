__author__ = 'Argorthas'

import Tkinter
import tkMessageBox
import Ingresosinpmw
import runVis

top = Tkinter.Tk()

def createIngreso():
        t = Tkinter.Toplevel(top)
        ventana = Ingresosinpmw.Demo(t)
        pass

def createBusqueda():
        t = Tkinter.Toplevel(top)
        ventana = runVis.Demo(t)
        pass

nuevo= Tkinter.Label(top,text="Bases de Datos\n para imagenologia toraxica").pack(padx=5,pady=5)
marco = Tkinter.Frame(top)
B = Tkinter.Button(marco, text ="Ingreso\n de Datos", command = createIngreso,height=10,width=20)
B.grid(row=1,column=0,padx=10, pady=10)
C = Tkinter.Button(marco, text ="Busqueda\n de Datos", command = createBusqueda,height=10,width=20)
C.grid(row=1,column=1,padx=10, pady=10)
marco.pack()
top.mainloop()
