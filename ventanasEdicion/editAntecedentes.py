# -*- coding: cp1252 -*-
import Pmw

from librerias.SearchCriteria import *
from tools.fillDb import *


class Demo:
    def __init__(self, parent):
        self.group = Pmw.Group(parent, tag_text = 'Antecedentes')
        self.group.grid(row=1,column=1,sticky=E, padx=5, pady=5)
        ####filtro

        self.run = Label(self.group.interior(), 
            text = 'IdRadio:').grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=1)

        #####filtro

        self.groupTrabajo = Pmw.Group(self.group.interior(), tag_text = 'Trabajo')
        self.groupTrabajo.grid(row=1,column=1)
        
        self.checkTrabajo = IntVar()
        Checkbutton(self.groupTrabajo.interior(), variable=self.checkTrabajo).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.trabajo = Label(self.groupTrabajo.interior(), 
                text = 'Trabajo:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.varTrabajo = StringVar()
        self.trabjoentry = Entry(self.groupTrabajo.interior(),textvariable = self.varTrabajo).grid(row=0,column=2)

        self.buttonTrabajoplus = Button(self.groupTrabajo.interior(),text="+",
                            command= lambda: self.plusField(self.trabajoArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonTrabajominus = Button(self.groupTrabajo.interior(),text="-",
                            command= lambda: self.minus(self.trabajoArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ######################################################################
        

        ##Medicamentos
        self.groupMedicamentos = Pmw.Group(self.group.interior(), tag_text = 'Medicamentos')
        self.groupMedicamentos.grid(row=2,column=1)
        
        self.checkMed = IntVar()
        Checkbutton(self.groupMedicamentos.interior(), variable=self.checkMed).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.medicamentos= Label(self.groupMedicamentos.interior(), text="Medicamentos:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.medicamentoValue = StringVar()
        self.medicamentoCombo = ttk.Combobox(self.groupMedicamentos.interior(), textvariable=self.medicamentoValue,
                                state='readonly')

        self.medicamentoCombo.grid(row=0,column=2)
        
        self.buttonMedicamentosplus = Button(self.groupMedicamentos.interior(),text="+",
                            command= lambda: self.plusField(self.medicamentoArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonMedicamentosminus = Button(self.groupMedicamentos.interior(),text="-",
                            command= lambda: self.minus(self.medicamentoArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        #########################################################################

        
        ##Alergia
        self.groupAlergia = Pmw.Group(self.group.interior(), tag_text = 'Alergia')
        self.groupAlergia.grid(row=3,column=1)
        
        self.checkAlergia = IntVar()
        Checkbutton(self.groupAlergia.interior(), variable=self.checkAlergia).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        
        self.alergia= Label(self.groupAlergia.interior(), text="Alergias:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.alergiaValue = StringVar()
        self.alergiaCombo = ttk.Combobox(self.groupAlergia.interior(), textvariable=self.alergiaValue,
                                state='readonly')

        self.alergiaCombo.grid(row=0,column=2)

        self.buttonAlergiaplus = Button(self.groupAlergia.interior(),text="+",
                            command= lambda: self.plusField(self.alergiaArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonAlergiaminus = Button(self.groupAlergia.interior(),text="-",
                            command= lambda: self.minus(self.alergiaArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ##########################################################################

        
        ##Adiccion
        self.groupAdiccion = Pmw.Group(self.group.interior(), tag_text = 'Adiccion')
        self.groupAdiccion.grid(row=4,column=1)
        
        self.checkAdiccion = IntVar()
        Checkbutton(self.groupAdiccion.interior(), variable=self.checkAdiccion).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        
        self.adiccion= Label(self.groupAdiccion.interior(), text="Adiccion:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.adiccionValue = StringVar()
        self.adiccionCombo = ttk.Combobox(self.groupAdiccion.interior(), textvariable=self.adiccionValue,
                                state='readonly')

        self.adiccionCombo.grid(row=0,column=2)

        self.buttonAdiccionplus = Button(self.groupAdiccion.interior(),text="+",
                            command= lambda: self.plusField(self.adiccionArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonAdiccionminus = Button(self.groupAdiccion.interior(),text="-",
                            command= lambda: self.minus(self.adiccionArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ########################################################################

        self.groupComentario = Pmw.Group(self.group.interior(), tag_text = 'Comentario')
        self.groupComentario.grid(row=5,column=1)
        self.checkComentario = IntVar()
        Checkbutton(self.groupComentario.interior(), variable=self.checkComentario).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.comentario1 = Label(self.groupComentario.interior(),
                text = 'Comentario:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.comentarioentry1 = Entry(self.groupComentario.interior())
        self.comentarioentry1.grid(row=0,column=3)

       #########################################################################


        self.group3 = Pmw.Group(self.group.interior(), tag_text = 'Intervenciones')
        self.group3.grid(row=6,column=1)

        self.checkIntervencion = IntVar()
        Checkbutton(self.group3.interior(), variable=self.checkIntervencion).grid(row=0,column=0,sticky=W, padx=5, pady=5)


        self.fechaint = Label(self.group3.interior(),
                text = 'Fecha:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.varF2 = StringVar()
        self.varF2.set('Today')
        self.fechaintdate= Label(self.group3.interior(), textvariable = self.varF2).grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.fechaintbutton = Button(self.group3.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF2)).grid(row=0,column=2,sticky=E, padx=5, pady=5)

        self.nombreop = Label(self.group3.interior(),
                text = 'Nombre Intervencion:').grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.nombreopentry = Entry(self.group3.interior())
        self.nombreopentry.grid(row=1,column=2)

        self.doc = Label(self.group3.interior(),
                text = 'Doctor:').grid(row=2,column=1,sticky=W, padx=5, pady=5)
        self.docentry = Entry(self.group3.interior())
        self.docentry.grid(row=2,column=2)


       #########################################################################
       #########################################################################


        #Agrupar cada cosa por su propio grupo

        self.listaVarTrabajo=[self.varTrabajo]
        self.listaVarmedicamento=[self.medicamentoValue]
        self.listaVaralergia=[self.alergiaValue]
        self.listaVaradiccion=[self.adiccionValue]


        listaTrabajoEntrys = [self.trabjoentry]
        listaMedCombo = [self.medicamentoCombo]
        listaAlergiaCombo = [self.alergiaCombo]
        listaAdiccionCombo = [self.adiccionCombo]
        
        

        #Antecedentes
        self.trabajoArray = [0, self.listaVarTrabajo, self.groupTrabajo.interior(), listaTrabajoEntrys,self.checkTrabajo]
        self.medicamentoArray = [1, self.listaVarmedicamento, self.groupMedicamentos.interior(), listaMedCombo,self.checkMed]
        self.alergiaArray = [2, self.listaVaralergia, self.groupAlergia.interior(), listaAlergiaCombo,self.checkAlergia]
        self.adiccionArray = [3, self.listaVaradiccion, self.groupAdiccion.interior(), listaAdiccionCombo,self.checkAdiccion]


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
