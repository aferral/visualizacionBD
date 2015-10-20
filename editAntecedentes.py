# -*- coding: cp1252 -*-
import Pmw

from SearchCriteria import *
from modeloAntecedentes import vistaAntecedentes


class Demo:
    def __init__(self, parent):
        self.group = Pmw.Group(parent, tag_text = 'Radiografia')
        self.group.grid(row=1,column=0,sticky= N, padx=5, pady=5)

        ####Inicio el Filtro

        Label(self.group.interior(), text = 'IdRadio:').grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.entryIdFiltro = Entry(self.group.interior())
        self.entryIdFiltro.grid(row=0,column=1)

        Button(self.group.interior(),text="Filtrar",command= self.filter).\
            grid(row=0,column=2,sticky=W, padx=5, pady=5)


        ##### Ventana de antecedentes

        self.groupAntecedentes = Pmw.Group(parent, tag_text = 'Antecedentes')
        self.groupAntecedentes.grid(row=2,column=0)

        self.vistaAntece = vistaAntecedentes(self.groupAntecedentes)

        self.groupBotones = Pmw.Group(parent, tag_text = 'Acciones')
        self.groupBotones.grid(row=3,column=0)

        Button(self.groupBotones.interior(),text = 'Actualizar',command = self.actualiza).grid(column=0, row=0)

    def filter(self):
        idToUse = self.entryIdFiltro.get()
        self.vistaAntece.recreateFromId(idToUse)
        pass
    def actualiza(self):
        idRadio = self.entryIdFiltro.get()
        self.vistaAntece.editFromCurrent(idRadio)
