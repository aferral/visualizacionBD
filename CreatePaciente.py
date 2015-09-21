# -*- coding: cp1252 -*-
import Tkinter
import Pmw
from Tkinter import *
import ttk
from Calendar import *
import VentanaExtra
from SearchCriteria import *
from fillDb import *

import psycopg2


class Demo:
    def __init__(self, parent):
        self.group = Pmw.Group(parent, tag_text = 'Paciente')
        self.group.grid(row=1,column=1,sticky=E, padx=5, pady=5)

        self.run = Label(self.group.interior(), 
            text = 'RUT:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=2)
        
        self.nombre = Label(self.group.interior(), 
            text = 'Nombre:')
        self.nombre.grid(row=1,column=1,sticky=W, padx=5, pady=5)

        self.nombreentry = Entry(self.group.interior())
        self.nombreentry.grid(row=1,column=2)

        self.apellidos = Label(self.group.interior(),
            text = 'Apellido:')
        self.apellidos.grid(row=2,column=1,sticky=W, padx=5, pady=5)

        self.apellidoEntry = Entry(self.group.interior())
        self.apellidoEntry.grid(row=2,column=2)


        
        self.sexo= Label(self.group.interior(), 
            text="Sexo:").grid(row=3,column=1,sticky=W, padx=5, pady=5)
        self.boolsexo = IntVar()
        self.radiobuttonm=Radiobutton(self.group.interior(), text="M", variable=self.boolsexo, value=1).grid(row=3,column=2,sticky=W)
        self.radiobuttonh=Radiobutton(self.group.interior(), text="H", variable=self.boolsexo, value=2).grid(row=3,column=2,sticky=E)

        self.fechanac= Label(self.group.interior(), text="FechaNac:").grid(row=4,column=1,sticky=W, padx=5, pady=5)
        self.varF0 = StringVar()
        self.varF0.set('Today')

        self.fechanacdate= Label(self.group.interior(), textvariable = self.varF0).grid(row=4,column=2,sticky=W, padx=5, pady=5)
        self.datechange0 = Button(self.group.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF0))
        self.datechange0.grid(row=4,column=3,sticky=E, padx=5, pady=5)

        self.crearPaciente = Button(parent,text="Crear",
                            command= self.crearPaciente).grid(row=2,column=1,sticky=E, padx=5, pady=5)


    def crearPaciente(self):

        #crea al paciente


        params = self.getParamsPaciente()
        try:
            askDb(queryAddPaciente,params)
            self.statusValue.set("Status: "+"Paciente agregado")
        except Exception, e:
            self.statusValue.set("Status: "+str(e))

    def updateF0(self,x):
        self.varF0.set(x.strftime('%Y-%m-%d'))
        return

    def createWindowsAndBind(self,fun):
        print fun
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)
