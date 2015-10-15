# -*- coding: cp1252 -*-
import Pmw

import VentanaExtra
from ventanasEdicion import ventanaEditarPaciente
import editRadio
import editAntecedentes
from librerias.SearchCriteria import *
from tools.fillDb import *
from patronesRecurrentes import filtrarPaciente

from librerias.querys.queryList import *
import WidgetContainer

class Demo:
    def __init__(self, parent):
        self.currentIdRadio = None
        self.parent = parent
        
        Pmw.aboutversion('1.0')
        Pmw.aboutcopyright('Copyright UchileDB\nAll rights reserved')
        Pmw.aboutcontact(
            'For information about this application contact:\n' +
            '  My Help Desk\n' +
            '  Phone: +XXXXXXXXXX\n' +
            '  email: help@my.company.com.au\n' +
            '  aferral and argorthas'
        )
        self.about = Pmw.AboutDialog(parent, applicationname = 'My Application')
        self.about.withdraw()


        #################################################

        # Create the Balloon for this toplevel.
        self.balloon = Pmw.Balloon(parent)

        # Create and install the MenuBar.
        menuBar = Pmw.MainMenuBar(parent,
                balloon = self.balloon)
        parent.configure(menu = menuBar)
        self.menuBar = menuBar

        # Add some buttons to the MainMenuBar.
        menuBar.addmenu('Create', 'Close this window or exit')
        menuBar.addmenuitem('Create', 'command', 'Exit the application',
                #command = lambda: self.createPaciente(queryAddMedicamento,queryDeleteMedicamento,queryUpdateMedicamento,queryListaMedicamento,self.actualizaListas),
                command = self.createPaciente,
                label = 'Paciente')

        menuBar.addmenu('Edit','asd')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Medicamento",
                                                 queryAddMedicamento,queryDeleteMedicamento,
                                                 queryUpdateMedicamento,queryListaMedicamento,
                                                 self.actualizaListas),
                label = 'Medicamento')

        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Alergia",queryAddAlergia,
                                                 queryDeleteAlergia,
                                                 queryUpdateAlergia,
                                                 queryListaAlergia,
                                                 self.actualizaListas),
                label = 'Alergia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Droga",queryAddDroga,
                                                 queryDeleteDroga,
                                                 queryUpdateDroga,
                                                 queryListaDroga,
                                                 self.actualizaListas),
                label = 'Droga')
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                #command = lambda: self.editRadio(queryAddMedicamento,queryDeleteMedicamento,queryUpdateMedicamento,queryListaMedicamento,self.actualizaListas),
                command = self.editRadio,
                label = 'Radio')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                #command = lambda: self.editAntecedentes(queryAddMedicamento,queryDeleteMedicamento,queryUpdateMedicamento,queryListaMedicamento,self.actualizaListas),
                command = self.editAntecedentes,
                label = 'Antecedentes')
        
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Procedencia",
                                                 queryAddProce,queryDeleteProce,
                                                 queryUpdateProce,queryListaProce,
                                                 self.actualizaListas),
                label = 'Procedencia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Zona",
                                                 queryAddZona,queryDeleteZona,
                                                 queryUpdateZona,queryListaZona,
                                                 self.actualizaListas),
                label = 'Zona')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Tipo",
                                                 queryAddTipo,queryDeleteTipo,
                                                 queryUpdateTipo,queryListaTipo,
                                                 self.actualizaListas),
                label = 'Tipo')
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Tipo",
                                                 queryAddEnfermedad,queryDeleteEnfermedad,
                                                 queryUpdateEnfermedad,queryListaEnfermedad,
                                                 self.actualizaListas),
                label = 'Enfermedad')


        menuBar.addmenu('Help', 'Set user preferences')
        menuBar.addmenuitem('Help', 'command', 'Set general preferences',
                command = self.execute,
                label = 'About')




        #############################################################################




        
        # Create and pack the NoteBook.
        self.notebook = Pmw.NoteBook(parent)
        self.notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        # Add the "Gemeral" page to the notebook.
        self.page = self.notebook.add('General')
        self.notebook.tab('General').focus_set()

        # Create the "Paciente" contents of the page.
        self.group = Pmw.Group(self.page, tag_text = 'Esta radiografia pertenece a :')
        self.group.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.run = Label(self.group.interior(), 
            text = 'RUT sin codigo ver:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=2)



        #Button "Filtro"
        self.filtrar = Button(self.group.interior(),text="Filtrar",
                            command= lambda: filtrarPaciente(self.runentry,self.pacienteCombo,None)).grid(row=0,column=3,sticky=W, padx=5, pady=5)

       #Combo box de nombre + apellido / este combo se rellenara ahora
        self.paciente= Label(self.group.interior(), text="Paciente:").grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.pacienteValue = StringVar()
        self.pacienteCombo = ttk.Combobox(self.group.interior(), textvariable=self.pacienteValue,
                                state='readonly')
        self.pacienteCombo['values'] = ()
        self.pacienteCombo.grid(row=1,column=2)

        

        # Create the "Radiografia" contents of the page.
        self.group1 = Pmw.Group(self.page, tag_text = 'Radiografia \nTodos los campos son obligatorios')
        self.group1.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        
        
        self.ids = Label(self.group1.interior(), 
            text = 'Id:').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        self.idsentry = Entry(self.group1.interior())
        self.idsentry.grid(row=1,column=1)


        
        self.groupEnf = LabelFrame(self.group1.interior())
        self.groupEnf.grid(row=2,column=0,sticky=NW)

        self.groupEnfCombo = LabelFrame(self.group1.interior(),bd=0)
        self.groupEnfCombo.grid(row=2,column=1)

        self.groupEnfB = LabelFrame(self.group1.interior(),bd=0)
        self.groupEnfB.grid(row=2,column=2,sticky=NW)
        
        Label(self.groupEnf, text="Enfermedad:").grid(row=0,column=0,sticky=W, padx=5, pady=5)


        self.contEnf = []
        cont = WidgetContainer.Contenedor(self.groupEnf)

        cont.add(ttk.Combobox,"Enfermedad",True,state='readonly').grid(row=0,column=0)
        cont.add(ttk.Combobox,"Confirmado",True,state='readonly').grid(row=0,column=1)
        cont.add(Entry,"Comentario",True,).grid(row=0,column=2)

        cont.grid(row=0,column=1)
        self.contEnf.append(cont)

        #fsfjdfdjksfjdk;sfk;dk; sj;d kj;lsdk;l jsd;fl jsdkl;fj l;kdsfksd;j fd

        enfButtonPlus = Button(self.groupEnfB,text="+",
                            command= lambda: self.expPlus(self.contEnf,self.groupEnf)
                               ).grid(row=0,column=2,sticky=E, padx=5, pady=5)
        enfButtonMinus = Button(self.groupEnfB,text="-",
                            command= lambda: self.expMinus(self.contEnf)
                                ).grid(row=0,column=3,sticky=E, padx=5, pady=5)

        self.frame = Label(self.group1.interior(),
            text = 'Frames \n>1 usar (;)  :').grid(row=3,column=0,sticky=W, padx=5, pady=5)
        self.frameentry = Entry(self.group1.interior())
        self.frameentry.grid(row=3,column=1)

        # Create and pack the dropdown ComboBox.
        self.zona= Label(self.group1.interior(), text="Zona:").grid(row=4,column=0,sticky=W, padx=5, pady=5)
        self.zonaValue = StringVar()
        self.zonaCombo = ttk.Combobox(self.group1.interior(), textvariable=self.zonaValue,
                                state='readonly')

        self.zonaCombo.grid(row=4,column=1)

        
       # Create and pack the dropdown ComboBox.
        self.tipo= Label(self.group1.interior(), text="Tipo:").grid(row=5,column=0,sticky=W, padx=5, pady=5)
        self.tipoValue = StringVar()
        self.tipoCombo = ttk.Combobox(self.group1.interior(), textvariable=self.tipoValue,
                                state='readonly')
        self.tipoCombo.grid(row=5,column=1)

        self.fecha= Label(self.group1.interior(), text="Fecha").grid(row=6,column=0,sticky=W, padx=5, pady=5)
        self.varF1 = StringVar()
        self.varF1.set('Today')
        self.fechadate= Label(self.group1.interior(), textvariable = self.varF1).grid(row=6,column=1,sticky=W, padx=5, pady=5)
        self.datechange1 = Button(self.group1.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF1)).grid(row=6,column=1,sticky=E, padx=5, pady=5)

        self.procedencia= Label(self.group1.interior(), text="Procedencia:").grid(row=7,column=0,sticky=W, padx=5, pady=5)
        self.procedenciaValue = StringVar()
        self.procedenciaCombo = ttk.Combobox(self.group1.interior(), textvariable=self.procedenciaValue,
                                state='readonly')
        self.procedenciaCombo.grid(row=7,column=1)

        
        self.comentario0 = Label(self.group1.interior(), 
                text = 'Comentario:').grid(row=9,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry0 = Entry(self.group1.interior())
        self.comentarioentry0.grid(row=9,column=1)

        


        # Add another page
        self.page1 = self.notebook.add('Antecedentes')
        #self.groupLabel = Pmw.Group(self.page1)
        #self.groupLabel.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        #Label(self.groupLabel.interior(), text="Trabajando con radiografia de id : "+str(self.getCurrentIdRadio())).grid(row=0,column=0,sticky=W, padx=5, pady=5)
       # Create the "Radiografia" contents of the page.
        ##Trabajo
        self.groupTrabajo = Pmw.Group(self.page1, tag_text = 'Trabajo')
        self.groupTrabajo.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
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
        self.groupMedicamentos = Pmw.Group(self.page1, tag_text = 'Medicamentos')
        self.groupMedicamentos.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
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
        self.groupAlergia = Pmw.Group(self.page1, tag_text = 'Alergia')
        self.groupAlergia.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
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
        self.groupAdiccion = Pmw.Group(self.page1, tag_text = 'Adiccion')
        self.groupAdiccion.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
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

        self.groupComentario = Pmw.Group(self.page1, tag_text = 'Comentario')
        self.groupComentario.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        self.checkComentario = IntVar()
        Checkbutton(self.groupComentario.interior(), variable=self.checkComentario).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.comentario1 = Label(self.groupComentario.interior(),
                text = 'Comentario:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.comentarioentry1 = Entry(self.groupComentario.interior())
        self.comentarioentry1.grid(row=0,column=3)

       #########################################################################


        self.group3 = Pmw.Group(self.page1, tag_text = 'Intervenciones')
        self.group3.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

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

        self.notebook.setnaturalsize()

        self.statusValue= StringVar()
        self.statusValue.set("Status:")
        self.status = Label(parent,textvariable=self.statusValue).pack()

       #########################################################################
       #########################################################################




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

       #########################################################################
       #########################################################################


        # Create and pack the ButtonBox.
        self.buttonBox = Pmw.ButtonBox(parent,
                labelpos = 'w',
                label_text = '                                                                                           ',
                frame_borderwidth = 2,
                frame_relief = 'groove')
        self.buttonBox.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        # Add some buttons to the ButtonBox.
        self.buttonBox.add('Crear', command = self.crearRadiografia)


        # Make all the buttons the same width.
        self.buttonBox.alignbuttons()




        self.actualizaListas()
    def getCurrentIdRadio(self):
        return self.currentIdRadio
    def setCurrentIdRadio(self,newId):
        self.currentIdRadio = newId
    def updateF0(self,x):
        self.varF0.set(x.strftime('%Y-%m-%d'))
        return

    def updateF1(self,x):
        self.varF1.set(x.strftime('%Y-%m-%d'))
        return

    def updateF2(self,x):
        self.varF2.set(x.strftime('%Y-%m-%d'))
        return

    def createWindowsAndBind(self,fun):
        print fun
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)

    def crearRadiografia(self):

        #TODO chequear que esten todos los campos rellenos
        try:
            valId = str(self.idsentry.get())
            valFecha = str(self.varF1.get())
            valZona = str(self.zonaValue.get())
            valProc = str(self.procedenciaValue.get())
            valTipo = str(self.tipoValue.get())
            valComent = str(self.comentarioentry0.get())
            valPacName = str(self.pacienteValue.get().split(",")[2])
            valPacApell = str(self.pacienteValue.get().split(",")[0])
            valPacRun = str(self.pacienteValue.get().split(",")[1])

            params = (valId,valFecha,valZona,valProc,valTipo,valComent,valPacName,valPacApell,valPacRun,)
        except Exception, e :
            print str(e)
            self.statusValue.set("Status: "+"Todo los campos deben rellenarse")
            return
        try:
            askDb(queryInsertRadio,params)
            self.statusValue.set("Status: "+"Radiografia agregada")
        except Exception, e:
            self.statusValue.set("Status: "+str(e))

        #Setea que estamos usando esta id
        self.setCurrentIdRadio(self.idsentry.get())

        #Agrega las distintas enfermedades y los distintos frames
        for contenedor in self.contEnf:
            valorEnf = contenedor.get('Enfermedad')
            valorConf = contenedor.get('Confirmado')
            valorComent = contenedor.get('Comentario')
            valorId = str(self.getCurrentIdRadio())

            askDb(queryAddEnfToRad, (valorEnf,valorConf,valorId,valorComent,))

        #Agrega los distintos frames
        listaDeFrames = self.frameentry.get().split(";")
        for elem in listaDeFrames:
            stringTemp = elem.strip()
            askDb(queryAddFrame,(stringTemp,str(self.getCurrentIdRadio())))

        #Comienza agregar antecedentes

        #Por todos los antecedentes

        #Generar un trabajo si esta activado

        if(self.trabajoArray[4].get() == 1):
            print "Ahora tenemos activado el checkboxTrabajo"
            for varTrabajo in self.trabajoArray[1]:
                idCreated = generarTrabajo(True,trabajo=varTrabajo.get())
                joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())
        #Generar un medicamento si esta activado
        if(self.medicamentoArray[4].get() == 1):
            print "Ahora tenemos activado el checkboxMedicamenteo"
            for varMed in self.medicamentoArray[1]:
                #Debo buscar id Correpondiente a seleccion
                queryIdMed = 'SELECT "IdMedicamento" FROM "Medicamento" WHERE "NombreMedicamento" = %s '
                params = (varMed.get(),)
                idMed = askDb(queryIdMed,params)[0][0]
                print "Id med resultante "+str(idMed)
                idCreated = generarMedPres(True,idMed=str(idMed))
                joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())
        #Generar un alergia si esta activado
        if(self.adiccionArray[4].get() == 1):
            print "Ahora tenemos activado el checkBoxAdiccioon"
            for varAdic in self.adiccionArray[1]:
                #Debo buscar id Correpondiente a seleccion
                queryIdAdiccion = 'SELECT "IdSustanciaAdiccion" FROM "SustanciaAdiccion" WHERE "NombreSustanciaAdiccion" = %s '
                params = (varAdic.get(),)
                idAdiccion = askDb(queryIdAdiccion,params)[0][0]
                print "Id adiccion resultante "+str(idAdiccion)
                idCreated = generaraUnAdiccion(1,1,True,idSus = str(idAdiccion),month='2')
                joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())

        #Generar un adiccion si esta activado
        if(self.alergiaArray[4].get() == 1):
            print "Ahora tenemos activado el checkboxAlergia"
            for varAlergia in self.alergiaArray[1]:
                #Debo buscar id Correpondiente a seleccion
                queryIdAlergia = 'SELECT "IdSustanciaAlergia" FROM "SustanciaAlergia" WHERE "NombreSustanciaAlergia" = %s'
                params = (varAlergia.get(),)
                idAlergia = askDb(queryIdAlergia,params)[0][0]
                print "Id alergia resultante "+str(idAlergia)
                idCreated = generaraUnAlergico(1,1,True,idSus= str(idAlergia) )
                joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())

        #Generar un intervencion si esta activado
        if self.checkIntervencion.get() == 1:
            idCreated = generaraUnIntervencion(True,date = self.varF2.get(), operation = self.nombreopentry.get(), dr = self.docentry.get())
            joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())
        #Generar comentario
        if self.checkComentario.get() == 1:
            idCreated = generarUnComentario(True,comment=self.comentarioentry1.get())
            joinAntecedenteRadiografia(idCreated,self.getCurrentIdRadio())



    def actualizaListas(self): #Actualiza enfermedades, medicamentos, alergias, procedencias

        queryEnfName =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
        queryMedName =  'SELECT "NombreMedicamento" FROM "Medicamento" '
        queryTipos =  'SELECT "nombreT" FROM "TipoR" '
        queryRadiZone =  'SELECT DISTINCT "nombreZ" FROM "Zonas" ORDER BY "nombreZ" '
        querySustanciaAlergia =  'SELECT DISTINCT "NombreSustanciaAlergia" FROM "SustanciaAlergia" ORDER BY "NombreSustanciaAlergia" '
        querySustanciaAdiccion =  'SELECT DISTINCT "NombreSustanciaAdiccion" FROM "SustanciaAdiccion" ORDER BY "NombreSustanciaAdiccion" '
        queryProcedencia = 'SELECT DISTINCT "nombreP" FROM "Procedencias" ORDER BY "nombreP"'


        #Actualiza enfermedas, Confirmados
        listaEnf = auxProcessList(queryEnfName,"")
        listaConf = ("True","False");
        for contenedor in self.contEnf:
            print "Actualizando contenedor"
            contenedor.update("Enfermedad",listaEnf)
            contenedor.update("Confirmado",listaConf)


        listaMed = auxProcessList(queryMedName,"")
        for combo in self.medicamentoArray[3]:
            combo['values'] = tuple(listaMed)

        self.zonaCombo['values'] = tuple(auxProcessList(queryRadiZone,""))
        self.tipoCombo['values'] = tuple(auxProcessList(queryTipos,""))

        listaAlerg = auxProcessList(querySustanciaAlergia,"")
        for combo in self.alergiaArray[3]:
            combo['values'] = tuple(listaAlerg)

        listaAdiccion = auxProcessList(querySustanciaAdiccion,"")
        for combo in self.adiccionArray[3]:
            combo['values'] = tuple(listaAdiccion)

        self.procedenciaCombo['values'] = tuple(auxProcessList(queryProcedencia,""))


        pass

    def newWindow(self, tipo, queryAdd, queryDelet, queryEdit, queryLista,updateFunction):
        t = Tkinter.Toplevel(self.parent)
        ventana = VentanaExtra.Demo(t,tipo, queryAdd, queryDelet, queryEdit,queryLista,updateFunction)
        pass
    
    def execute(self):
        self.about.show()


    def expPlus(self,lista,where):
        print len(lista)
        newRow = lista[0].clone(where)
        newRow.grid(row=len(lista),column=1, padx=5, pady=5)
        lista.append(newRow)
        self.actualizaListas()
        pass
    def expMinus(self,lista):
        disable = lista.pop()
        disable.grid_forget()
        pass

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


    def auxProcessList(self,StringQuery,params):
        try:
            listRes = askDb(StringQuery,params)
        except Exception, e:
            self.statusValue.set("Status: "+str(e))

        for i in range(len(listRes)):
            listRes[i] = listRes[i][0]
        return listRes

    ####################################################

    def createPaciente(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = ventanaEditarPaciente.Demo(t)
        pass
    
    def editAntecedentes(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = editAntecedentes.Demo(t)
        pass
    
    def editRadio(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = editRadio.Demo(t)
        pass
    
    #####################################################



root = Tkinter.Tk()
demo = Demo(root)
root.mainloop()
