# -*- coding: cp1252 -*-
import Tkinter
import Pmw
from Tkinter import *
import ttk
from SearchCriteria import askDb



class Demo:
    def __init__(self, parent, tipo, consultaAdd, consultaDele, consultaEdit, consultaLista,foreignFun):
        #
        #Grupo de Creacion
        #
        self.consultaInsert = consultaAdd
        self.consultaDelet = consultaDele
        self.consultaEdit = consultaEdit
        self.consultaLista = consultaLista

        self.updateFun = foreignFun;

        self.tipo = tipo
        self.groupcrear = Pmw.Group(parent,
                tag_pyclass = Tkinter.Button,
                tag_text='Crear')
        self.groupcrear.configure(tag_command = self.groupcrear.toggle)
        self.groupcrear.pack(fill = 'both', expand = 1, padx = 6, pady = 6)

        self.nuevo= Label(self.groupcrear.interior(),
                          text="Nuevo "+tipo+" :").grid(row=0,column=0,sticky=W,
                                                   padx=5, pady=5)
        self.createVar = StringVar()
        self.crearentry = Entry(self.groupcrear.interior(), width= 25, textvariable = self.createVar)
        self.crearentry.grid(row=0,column=1)

        
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
        self.deleteVar = StringVar()
        self.itemCombo = ttk.Combobox(self.groupborrar.interior(),
                                          textvariable=self.deleteVar,
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
        self.updateVar = StringVar()
        self.newUpdateVar = StringVar()
        self.itemCombo1 = ttk.Combobox(self.groupeditar.interior(),
                                          postcommand=self.update,
                                          textvariable=self.updateVar,
                                          state='readonly')

        self.itemCombo1.grid(row=0,column=1)
        


        self.nuevo= Label(self.groupeditar.interior(),
                          text="Nuevo "+tipo+" :").grid(row=1,column=0,sticky=W,
                                                   padx=5, pady=5)
        self.editarentry = Entry(self.groupeditar.interior(),
                                 textvariable=self.newUpdateVar).grid(row=1,column=1)

        self.buttoneditar = Button(self.groupeditar.interior(),text="Editar",
                            command= self.editar).grid(row=2,column=2,sticky=E,
                                                        padx=5, pady=5)

        self.update()


        
    def crear(self):
        print "Se esta creando"
        params = (str(self.createVar.get()),)
        askDb(self.consultaInsert,params)

        self.update()


    def borrar(self):
        print "Se esta borrando"
        print str(self.deleteVar.get())
        nombreViejo = str(self.deleteVar.get()).split(",")[1]
        params = (nombreViejo,)
        askDb(self.consultaDelet,params)

        self.update()

    def editar(self):
        print "Se esta editando"
        nombreViejo = str(self.updateVar.get()).split(",")[1]
        nombreNuevo = str(self.newUpdateVar.get())
        params = (nombreNuevo,nombreViejo,)
        askDb(self.consultaEdit,params)

        self.update()

    def update(self):
        print "Actualizando lista de entidades "+str(self.tipo)
        params = ('',)
        lista = askDb(self.consultaLista,params)
        listaOut = []
        for elem in lista:
            listaOut.append(str(elem[0])+","+str(elem[1]))
        self.itemCombo['values'] = tuple(listaOut)
        self.itemCombo1['values'] = tuple(listaOut)
        if len(lista) > 0:
            self.itemCombo1.current(0)
            self.itemCombo.current(0)
        self.updateFun()
