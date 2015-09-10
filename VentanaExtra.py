# -*- coding: cp1252 -*-
import Tkinter
import Pmw
from Tkinter import *
import ttk




class Demo:
    def __init__(self, parent, tipo):
        #
        #Grupo de Creacion
        #
        self.tipo = tipo
        self.groupcrear = Pmw.Group(parent,
                tag_pyclass = Tkinter.Button,
                tag_text='Crear')
        self.groupcrear.configure(tag_command = self.groupcrear.toggle)
        self.groupcrear.pack(fill = 'both', expand = 1, padx = 6, pady = 6)

        self.nuevo= Label(self.groupcrear.interior(),
                          text="Nuevo "+tipo+" :").grid(row=0,column=0,sticky=W,
                                                   padx=5, pady=5)
        self.crearentry = Entry(self.groupcrear.interior(), width= 25).grid(row=0,column=1)

        
        self.buttoncrear = Button(self.groupcrear.interior(),text="Crear",
                            command= self.crear).grid(row=1,column=2,sticky=E,
                                                        padx=5, pady=5)
        





        #
        #Grupo de Borrado
        #
        self.groupborrar = Pmw.Group(parent,
                tag_pyclass = Tkinter.Button,
                tag_text='Borrar')
        self.groupborrar.configure(tag_command = self.groupborrar.toggle)
        self.groupborrar.pack(fill = 'both', expand = 1, padx = 6, pady = 6)

        self.itemaborrar= Label(self.groupborrar.interior(),
                             text=tipo+" a borrar :").grid(row=0,column=0,sticky=W,
                                                      padx=5, pady=5)
        self.itemValue = StringVar()
        self.itemCombo = ttk.Combobox(self.groupborrar.interior(),
                                          textvariable=self.itemValue,
                                          state='readonly')
        self.itemCombo['values'] = ()
        self.itemCombo.grid(row=0,column=1)

        self.buttonborrar = Button(self.groupborrar.interior(),text="Borrar",
                            command= self.borrar).grid(row=1,column=2,sticky=E,
                                                        padx=5, pady=5)




        #
        #Grupo de Editar
        #
        self.groupeditar = Pmw.Group(parent,
                tag_pyclass = Tkinter.Button,
                tag_text='Editar')
        self.groupeditar.configure(tag_command = self.groupeditar.toggle)
        self.groupeditar.pack(fill = 'both', expand = 1, padx = 6, pady = 6)

        self.itemaeditar= Label(self.groupeditar.interior(),
                             text=tipo+" a editar :").grid(row=0,column=0,sticky=W,
                                                      padx=5, pady=5)
        self.itemValue1 = StringVar()
        self.itemValue2 = StringVar()
        self.itemCombo1 = ttk.Combobox(self.groupeditar.interior(),
                                          postcommand=self.update,
                                          textvariable=self.itemValue1,
                                          state='readonly')
        self.itemCombo1['values'] = ('Enfermedad1', 'Enfermedad2', 'Enfermedad3', 'Enfermedad4')
        self.itemCombo1.current(0)
        self.itemCombo1.grid(row=0,column=1)
        


        self.nuevo= Label(self.groupeditar.interior(),
                          text="Nuevo "+tipo+" :").grid(row=1,column=0,sticky=W,
                                                   padx=5, pady=5)
        self.editarentry = Entry(self.groupeditar.interior(),
                                 textvariable=self.itemValue2).grid(row=1,column=1)

        self.buttoneditar = Button(self.groupeditar.interior(),text="Editar",
                            command= self.editar).grid(row=2,column=2,sticky=E,
                                                        padx=5, pady=5)




        
    def crear(self):
        #crea al paciente
        print "Se esta creando"


    def borrar(self):
        #borra al paciente
        print "Se esta borrando"


    def editar(self):
        #borra al paciente
        print "Se esta editando"

    def update(self):
        self.itemValue2.set(self.itemValue1.get())
