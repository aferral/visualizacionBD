# -*- coding: cp1252 -*-
import Pmw

from librerias.SearchCriteria import *
from tools.fillDb import *


class Demo:
    def __init__(self, parent):
        self.group = Pmw.Group(parent, tag_text = 'Radiografia')
        self.group.grid(row=1,column=1,sticky=E, padx=5, pady=5)

        self.run = Label(self.group.interior(), 
            text = 'IdRadio:').grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=1)



        self.groupEnf = LabelFrame(self.group.interior(),bd=0)
        self.groupEnf.grid(row=1,column=0,sticky=NW)
        self.groupEnfCombo = LabelFrame(self.group.interior(),bd=0)
        self.groupEnfCombo.grid(row=1,column=1)
        self.groupEnfB = LabelFrame(self.group.interior(),bd=0)
        self.groupEnfB.grid(row=1,column=2,sticky=NW)
        
        self.enfermedad= Label(self.groupEnf, text="Enfermedad:").grid(sticky=W, padx=5, pady=5)
        self.enfermedadValue = StringVar()
        self.enfermedadCombo = ttk.Combobox(self.groupEnfCombo, textvariable=self.enfermedadValue,
                                state='readonly')
        self.enfermedadCombo.grid(row=0,column=2)
        enfButtonPlus = Button(self.groupEnfB,text="+",
                            command= lambda: self.plusField(self.enfArray)).grid(row=0,column=2,sticky=E, padx=5, pady=5)
        enfButtonMinus = Button(self.groupEnfB,text="-",
                            command= lambda: self.minus(self.enfArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5) 


        self.confirmado= Label(self.group.interior(), text="Confirmado:").grid(row=2,column=0,sticky=W, padx=5, pady=5)
        self.confirmadoValue = StringVar()
        self.confirmadoCombo = ttk.Combobox(self.group.interior(), textvariable=self.confirmadoValue,
                                state='readonly')
        self.confirmadoCombo.grid(row=2,column=1)

        self.frame = Label(self.group.interior(),
            text = 'Frames \n>1 usar (;)  :').grid(row=3,column=0,sticky=W, padx=5, pady=5)
        self.frameentry = Entry(self.group.interior())
        self.frameentry.grid(row=3,column=1)

        
        
        self.comentario0 = Label(self.group.interior(), 
                text = 'Comentario:').grid(row=4,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry0 = Entry(self.group.interior())
        self.comentarioentry0.grid(row=4,column=1)



        self.editarRadiografia = Button(parent,text="Editar",
                            command= self.editarRadio).grid(row=2,column=1,sticky=E, padx=5, pady=5)

        listaEnfCombo = [self.enfermedadCombo]
        self.listaVarEnf = [self.enfermedadValue]
        self.enfArray = [4, self.listaVarEnf, self.groupEnfCombo, listaEnfCombo]


    def editarRadio(self):

        #crea al paciente


        params = self.getParamsPaciente()
        try:
            askDb(queryAddPaciente,params)
            self.statusValue.set("Status: "+"Paciente agregado")
        except Exception, e:
            self.statusValue.set("Status: "+str(e))


    def plusField(self,aArray):
        n=aArray[0]
        aVariable = StringVar()
        widgetToAdd = None
        if (n == 0):
            widgetToAdd = Entry(aArray[2],textvariable = aVariable)
        else:
            widgetToAdd =ttk.Combobox(aArray[2], textvariable=aVariable,
                                    state='readonly')

        widgetToAdd.grid(row=len(aArray[3]),column=2, padx=5, pady=5)
        aArray[3].append(widgetToAdd)
        aArray[1].append(aVariable)
        self.actualizaListas()
        pass


    def minus(self,aArray):
        if (len(aArray[3])>1):
            disable = aArray[3].pop()
            disable.grid_forget()
        pass
