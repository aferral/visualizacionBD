# -*- coding: cp1252 -*-
import Pmw

from SearchCriteria import *
from DatosRadio import vistaRadio
from patronesRecurrentes import filtrarPaciente

class Demo:
    def __init__(self, parent):
        self.filtroId = StringVar()

        self.grupoFiltro = Pmw.Group(parent, tag_text = 'Filtrar Id')
        self.grupoFiltro.grid(row=0,column=0,sticky=E, padx=5, pady=5)

        self.group = Pmw.Group(parent, tag_text = 'Radiografia')
        self.group.grid(row=1,column=0,sticky=E, padx=5, pady=5)

        self.groupBotones = Pmw.Group(parent, tag_text = 'Accion')
        self.groupBotones.grid(row=2,column=0,sticky=E, padx=5, pady=5)

        Label(self.grupoFiltro.interior(),
            text = 'IdRadio:').grid(row=0,column=0,sticky=W, padx=5, pady=5)

        Entry(self.grupoFiltro.interior(),textvariable=self.filtroId).grid(row=0,column=1)
        Button(self.grupoFiltro.interior(),text="Filtrar",command= self.filter).grid(row=0,column=2,sticky=W, padx=5, pady=5)

        Label(self.grupoFiltro.interior(),
            text = 'RUT sin codigo ver:').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.grupoFiltro.interior())
        self.runentry.grid(row=1,column=1,sticky=W, padx=5, pady=5)


        #FIn de filtro

        #Aca la vista de la radiografia
        self.vistaRadio = vistaRadio(self.group)

        #Button "Filtro"
        Button(self.grupoFiltro.interior(),text="Filtrar",command= lambda: filtrarPaciente(
            self.runentry,self.vistaRadio.getWidget('PacienteCombo'),None)
               ).grid(row=1,column=2,sticky=W, padx=5, pady=5)


        #Botones editar o eliminar

        Button(self.groupBotones.interior(), text="Editar", command = self.edit).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        Button(self.groupBotones.interior(), text="Borrar", command = self.delete).grid(row=0,column=1,sticky=W, padx=5, pady=5)

    def filter(self):

        idABuscar = self.filtroId.get()
        self.vistaRadio.recreateFromId(int(idABuscar))


        pass
    def edit(self):
        self.vistaRadio.edit()

    def delete(self):
        self.vistaRadio.deleteCurrentRelations()
        self.vistaRadio.deleteCurrentRadio()
        pass