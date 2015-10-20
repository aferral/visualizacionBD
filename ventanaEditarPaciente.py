# -*- coding: cp1252 -*-

import Pmw

from SearchCriteria import *
from patronesRecurrentes import filtrarPaciente
from patronesRecurrentes import crearPaciente
from patronesRecurrentes import updateEntrys
from patronesRecurrentes import updatePaciente
from patronesRecurrentes import deletePaciente

class Demo:
    def __init__(self, parent):
        self.groupCreate = Pmw.Group(parent, tag_text = 'Crear paciente')
        self.groupCreate.grid(row=1,column=0,sticky=E, padx=5, pady=5)

        self.groupEdit = Pmw.Group(parent, tag_text = 'Editar o borrar paciente (SOLO FECHA NAC/SEXO)')
        self.groupEdit.grid(row=2,column=0,sticky=E, padx=5, pady=5)

        #--------------------------Grupo CREAR Paciente ------------------------------------------
        #Variables importantes
        self.varRun = StringVar()
        self.varNombre = StringVar()
        self.varApellido = StringVar()
        self.boolsexo = IntVar()
        self.varFecha = StringVar()
        self.varFecha.set('Today')

        #Construcciones y grideo
        Label(self.groupCreate.interior(),
            text = 'RUT:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        Entry(self.groupCreate.interior(),textvariable=self.varRun).grid(row=0,column=2)

        Label(self.groupCreate.interior(),
            text = 'Nombre:').grid(row=1,column=1,sticky=W, padx=5, pady=5)

        Entry(self.groupCreate.interior(),textvariable=self.varNombre).grid(row=1,column=2)

        Label(self.groupCreate.interior(),
            text = 'Apellido:').grid(row=2,column=1,sticky=W, padx=5, pady=5)

        Entry(self.groupCreate.interior(),textvariable=self.varApellido).grid(row=2,column=2)

        Label(self.groupCreate.interior(),
            text="Sexo:").grid(row=3,column=1,sticky=W, padx=5, pady=5)

        Radiobutton(self.groupCreate.interior(), text="M", variable=self.boolsexo, value=0).grid(row=3,column=2,sticky=W)
        Radiobutton(self.groupCreate.interior(), text="H", variable=self.boolsexo, value=1).grid(row=3,column=2,sticky=E)

        Label(self.groupCreate.interior(), text="FechaNac:").grid(row=4,column=1,sticky=W, padx=5, pady=5)
        Label(self.groupCreate.interior(), textvariable = self.varFecha).grid(row=4,column=2,sticky=W, padx=5, pady=5)
        Button(self.groupCreate.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateFechaCreate)
               ).grid(row=4,column=3,sticky=E, padx=5, pady=5)


        Button(self.groupCreate.interior(),text="Crear",command= self.createPac
               ).grid(row=5,column=1,sticky=E, padx=5, pady=5)


        #--------------------------Grupo EDITAR Paciente ------------------------------------------
        #Variables importantes
        self.varRunEdit = StringVar()
        self.varNombEdit = StringVar()
        self.varApeEdit = StringVar()
        self.boolsexEdit = IntVar()
        self.varFecEdit = StringVar()
        self.varFecEdit.set('Today')

        self.pacienteValue = StringVar()

        Label(self.groupEdit.interior(),
            text = 'RUT sin codigo ver:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        Entry(self.groupEdit.interior(),textvariable=self.varRunEdit).grid(row=0,column=2)

        Button(self.groupEdit.interior(),text="Filtrar",
                            command = self.filterAndUpdate ).grid(row=0,column=3,sticky=W, padx=5, pady=5)

        #Combo box de nombre + apellido / este combo se rellenara ahora
        Label(self.groupEdit.interior(), text="Paciente:").grid(row=1,column=1,sticky=W, padx=5, pady=5)

        self.pacienteCombo = ttk.Combobox(self.groupEdit.interior(), textvariable=self.pacienteValue,
                                state='readonly')
        self.pacienteCombo['values'] = ()
        self.pacienteCombo.bind('<<ComboboxSelected>>',self.updateNow)
        self.pacienteCombo.grid(row=1,column=2)

        Label(self.groupEdit.interior(),text = 'Nombre:').grid(row=2,column=1,sticky=W, padx=5, pady=5)

        Label(self.groupEdit.interior(),textvariable=self.varNombEdit).grid(row=2,column=2)

        Label(self.groupEdit.interior(),text = 'Apellido:').grid(row=3,column=1,sticky=W, padx=5, pady=5)

        Label(self.groupEdit.interior(),textvariable=self.varApeEdit).grid(row=3,column=2)

        Label(self.groupEdit.interior(),text="Sexo:").grid(row=4,column=1,sticky=W, padx=5, pady=5)

        Radiobutton(self.groupEdit.interior(), text="M", variable=self.boolsexEdit, value=0).grid(row=4,column=2,sticky=W)
        Radiobutton(self.groupEdit.interior(), text="H", variable=self.boolsexEdit, value=1).grid(row=4,column=2,sticky=E)

        Label(self.groupEdit.interior(), text="FechaNac:").grid(row=5,column=1,sticky=W, padx=5, pady=5)

        Label(self.groupEdit.interior(), textvariable = self.varFecEdit).grid(row=5,column=2,sticky=W, padx=5, pady=5)
        Button(self.groupEdit.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateFechaEdit)
               ).grid(row=5,column=3,sticky=E, padx=5, pady=5)

        Button(self.groupEdit.interior(),text="Editar",
                            command= self.editAndUpdate).grid(row=6,column=0,sticky=E, padx=5, pady=5)
        Button(self.groupEdit.interior(),text="Borrar",
                            command= self.deleteAndUpdate).grid(row=6,column=1,sticky=E, padx=5, pady=5)

    def createPac(self):
        crearPaciente(
            self.boolsexo,
            self.varRun,
            self.varNombre,
            self.varApellido,
            self.varFecha)
    def filterAndUpdate(self):
        filtrarPaciente(self.varRunEdit,self.pacienteCombo,None)
        self.updateNow(None)

    def editAndUpdate(self):
        updatePaciente(
            self.boolsexEdit,
            self.varRunEdit,
            self.varNombEdit,
            self.varApeEdit,
            self.varFecEdit)
        self.updateNow(None)
    def deleteAndUpdate(self):
        deletePaciente(self.pacienteCombo)
        self.updateNow(None)

    def updateNow(self,event):
        updateEntrys(self.varRunEdit,self.varNombEdit,
             self.varApeEdit,self.boolsexEdit,
             self.varFecEdit,self.pacienteValue)

    def updateFechaCreate(self,x):
        self.varFecha.set(x.strftime('%Y-%m-%d'))
        return
    def updateFechaEdit(self,x):
        self.varFecEdit.set(x.strftime('%Y-%m-%d'))
        return

    def createWindowsAndBind(self,fun):
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)

