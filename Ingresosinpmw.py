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

queryInsertRadio = 'INSERT INTO "Radiografia"("IdRadio", "Fecha", "Zona", "Procedencia", ' \
                '"Tipo", "Comentario", "RUNPaciente", "NombresPaciente","ApellidosPaciente") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'

queryFiltrarPaciente = 'SELECT "Nombres","Apellidos","RUN" FROM "Paciente" '
queryAddPaciente = 'INSERT INTO "Paciente" ("Sexo", "RUN", "Nombres", "Apellidos", "FechaNac" ) ' \
                'VALUES (%s, %s, %s, %s, %s)'
queryAddEnfToRad = 'INSERT INTO "Representa"( "NombreE", "Confirmado","IdRadio") VALUES (%s, %s, %s);'

queryAddFrame = 'INSERT INTO "Frames"( "NumOfFrame", "IdRadio") VALUES (%s, %s);'


queryAddAntece = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
 'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
class Demo:
    def __init__(self, parent):
        self.currentIdRadio = None
        self.parent = parent
        
        Pmw.aboutversion('9.9')
        Pmw.aboutcopyright('Copyright My Company 1999\nAll rights reserved')
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
        menuBar.addmenu('File', 'Close this window or exit')
        menuBar.addmenuitem('File', 'command', 'Close this window',
                command = PrintOne('Action: close'),
                label = 'Close')
        menuBar.addmenuitem('File', 'separator')
        menuBar.addmenuitem('File', 'command', 'Exit the application',
                command = PrintOne('Action: exit'),
                label = 'Exit')

        menuBar.addmenu('Edit','asd')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Medicamento"),
                label = 'Medicamento')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Alergia"),
                label = 'Alergia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Droga"),
                label = 'Droga')

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
        self.group = Pmw.Group(self.page, tag_text = 'Paciente')
        self.group.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        #self.varCheckRut = IntVar()
        #Checkbutton(self.group.interior(), variable=self.varCheckRut).grid(row=0,column=0)
        self.run = Label(self.group.interior(), 
            text = 'RUT:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=2)
        
        #self.varCheckNombre = IntVar()
        #Checkbutton(self.group.interior(), variable=self.varCheckNombre).grid(row=1,column=0)
        self.nombre = Label(self.group.interior(), 
            text = 'Nombre:')
        self.nombre.grid(row=1,column=1,sticky=W, padx=5, pady=5)

        self.nombreentry = Entry(self.group.interior())
        self.nombreentry.grid(row=1,column=2)

        #self.varCheckApellidos = IntVar()
        #Checkbutton(self.group.interior(), variable=self.varCheckApellidos).grid(row=2,column=0)
        self.apellidos = Label(self.group.interior(),
            text = 'Apellido:')
        self.apellidos.grid(row=2,column=1,sticky=W, padx=5, pady=5)

        self.apellidoEntry = Entry(self.group.interior())
        self.apellidoEntry.grid(row=2,column=2)


        #Button "Filtro"
        self.filtrar = Button(self.group.interior(),text="Filtrar",
                            command= self.filtrarPaciente).grid(row=2,column=3,sticky=W, padx=5, pady=5)

        #self.varSexo = IntVar()
        #Checkbutton(self.group.interior(), variable=self.varSexo).grid(row=3,column=0)
        self.sexo= Label(self.group.interior(), 
            text="Sexo:").grid(row=3,column=1,sticky=W, padx=5, pady=5)
        self.boolsexo = IntVar()
        self.radiobuttonm=Radiobutton(self.group.interior(), text="M", variable=self.boolsexo, value=1).grid(row=3,column=2,sticky=W)
        self.radiobuttonh=Radiobutton(self.group.interior(), text="H", variable=self.boolsexo, value=2).grid(row=3,column=2,sticky=E)

        #self.varFechaNac = IntVar()
        #Checkbutton(self.group.interior(), variable=self.varFechaNac).grid(row=4,column=0)
        self.fechanac= Label(self.group.interior(), text="FechaNac:").grid(row=4,column=1,sticky=W, padx=5, pady=5)
        self.varF0 = StringVar()
        self.varF0.set('Today')

        self.fechanacdate= Label(self.group.interior(), textvariable = self.varF0).grid(row=4,column=2,sticky=W, padx=5, pady=5)
        self.datechange0 = Button(self.group.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF0))
        self.datechange0.grid(row=4,column=1,sticky=E, padx=5, pady=5)

        self.crearPaciente = Button(self.group.interior(),text="Crear",
                            command= self.crearPaciente).grid(row=5,column=2,sticky=E, padx=5, pady=5)
                
        
        
        

        # Create the "Radiografia" contents of the page.
        self.group1 = Pmw.Group(self.page, tag_text = 'Radiografia **Todos los campos son obligatorios')
        self.group1.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.paciente= Label(self.group1.interior(), text="Paciente:").grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.pacienteValue = StringVar()
        self.pacienteCombo = ttk.Combobox(self.group1.interior(), textvariable=self.pacienteValue,
                                state='readonly')
        self.pacienteCombo['values'] = ()
        self.pacienteCombo.grid(row=0,column=1)
        
        
        self.ids = Label(self.group1.interior(), 
            text = 'Id:').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        self.idsentry = Entry(self.group1.interior())
        self.idsentry.grid(row=1,column=1)


        

        self.groupEnf = Pmw.Group(self.group1.interior(), tag_text = 'Enfermedad')
        self.groupEnf.grid(row=2,column=0)
        self.enfermedad= Label(self.groupEnf.interior(), text="Enfermedad:").grid(row=0,column=2, padx=5, pady=5)
        self.enfermedadValue = StringVar()
        self.enfermedadCombo = ttk.Combobox(self.groupEnf.interior(), textvariable=self.enfermedadValue,
                                state='readonly')
        self.enfermedadCombo.grid(row=0,column=2)

        enfButtonPlus = Button(self.groupEnf.interior(),text="+",
                            command= lambda: self.plusField(self.enfArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        enfButtonMinus = Button(self.groupEnf.interior(),text="-",
                            command= lambda: self.minus(self.enfArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)

        self.frame = Label(self.group1.interior(),
            text = 'Frames Si es mas de uno usar (;)  :').grid(row=3,column=0,sticky=W, padx=5, pady=5)
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
        self.tipoCombo['values'] = ('Radiografia', 'Escaner', 'Resonancia')
        self.tipoCombo.current(0)
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
                text = 'Comentario:').grid(row=8,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry0 = Entry(self.group1.interior())
        self.comentarioentry0.grid(row=8,column=1)

        


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

        self.checkIntervencion

        #Agrupar cada cosa por su propio grupo
        self.listaVarEnf = [self.enfermedadValue]
        self.listaVarTrabajo=[self.varTrabajo]
        self.listaVarmedicamento=[self.medicamentoValue]
        self.listaVaralergia=[self.alergiaValue]
        self.listaVaradiccion=[self.adiccionValue]

        listaEnfCombo = [self.enfermedadCombo]
        listaTrabajoEntrys = [self.trabjoentry]
        listaMedCombo = [self.medicamentoCombo]
        listaAlergiaCombo = [self.alergiaCombo]
        listaAdiccionCombo = [self.adiccionCombo]
        
        self.enfArray = [4, self.listaVarEnf, self.groupEnf, listaEnfCombo]

        #Antecedentes
        self.trabajoArray = [0, self.listaVarTrabajo, self.groupTrabajo, listaTrabajoEntrys,self.checkTrabajo]
        self.medicamentoArray = [1, self.listaVarmedicamento, self.groupMedicamentos, listaMedCombo,self.checkMed]
        self.alergiaArray = [2, self.listaVaralergia, self.groupAlergia, listaAlergiaCombo,self.checkAlergia]
        self.adiccionArray = [3, self.listaVaradiccion, self.groupAdiccion, listaAdiccionCombo,self.checkAdiccion]

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

        try:
            params = (str(self.idsentry.get()),str(self.varF1.get()),str(self.zonaValue.get()),str(self.procedenciaValue.get()),
                      str(self.tipoValue.get()),str(self.comentarioentry0.get()),str(self.pacienteValue.get().split(",")[2])
                      ,str(self.pacienteValue.get().split(",")[0]),str(self.pacienteValue.get().split(",")[1]),)
        except Exception, e :
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
        for enfVar in self.enfArray[1]:
            askDb(queryAddEnfToRad, (str(enfVar.get()),True,str(self.getCurrentIdRadio()),))

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




    def processUnaryAntecedente(self,lista,query):
        if(lista[4].get() == 1): #Ve si esta activada checkbox
            #Consigue todos los rellenos de X
            for varString in self.trabajoArray[1]:
                #Agrega nuevo antecedente y consige esa id
                idJustAdded = askDb(queryAddAntece, '')[0][0]
                #Envia solicitud sql de X y anexa a idRadio actual
                params = (idJustAdded,varString.get(),)
                askDb(query,params)



    def filtrarPaciente(self):

        (varSexo,varRun,varNombre,varApellido,varFecha,) = self.getParamsPaciente()
        whereString = ""
        params = ()
        if (varSexo != ''):
            whereString += '"Sexo" = %s AND '
            params = params + (str(varSexo),)
        if (varRun != ''):
            whereString += '"RUN" = %s AND '
            params = params + (str(varRun),)
        if (varNombre != ''):
            whereString += '"Nombres" LIKE %s AND '
            params = params + ("%"+str(varNombre)+"%",)
        if (varApellido != ''):
            whereString += '"Apellidos" LIKE %s AND '
            params = params + ("%"+str(varApellido)+"%",)
        if (varFecha != 'Today'):
            whereString += '"FechaNac" < %s AND '
            params = params + (str(varFecha),)
        if(whereString != ""):
            whereString = "WHERE "+whereString[:-4]


        listRes = []
        try:
            listRes = askDb(queryFiltrarPaciente + whereString,params)
        except Exception, e:
            self.statusValue.set("Status: "+str(e))
        if len(listRes) == 0:
            listRes = ["No hay resultados"]
        else:
            for i in range(len(listRes)):
                listRes[i] = listRes[i][0]+","+str(listRes[i][1])+","+str(listRes[i][2])
        self.pacienteCombo['values'] = tuple(listRes)
        self.pacienteCombo.current(0)

    def getParamsPaciente(self):
        varSexo = 'M'
        if self.boolsexo.get():
            if self.boolsexo.get() == 1:
                varSexo = 'H'
        varRun = self.runentry.get().strip()
        varNombre = self.nombreentry.get().strip()
        varApellido = self.apellidoEntry.get().strip()
        varFecha = self.varF0.get().strip()
        print "Comienzo filtro y update de ComboBox"
        print "Rut ",varRun
        print "nombre ",varNombre
        print "apellido ",varApellido
        print "Sexo ",str(varSexo)
        print "FechaNac ",varFecha
        return (varSexo,varRun,varNombre,varApellido,varFecha,)

    def crearPaciente(self):

        #crea al paciente


        params = self.getParamsPaciente()
        try:
            askDb(queryAddPaciente,params)
            self.statusValue.set("Status: "+"Paciente agregado")
        except Exception, e:
            self.statusValue.set("Status: "+str(e))

    def actualizaListas(self):

        queryEnfName =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
        queryMedName =  'SELECT "NombreMedicamento" FROM "Medicamento" '
        queryRadiZone =  'SELECT DISTINCT "Zona" FROM "Radiografia" ORDER BY "Zona" '
        querySustanciaAlergia =  'SELECT DISTINCT "NombreSustanciaAlergia" FROM "SustanciaAlergia" ORDER BY "NombreSustanciaAlergia" '
        querySustanciaAdiccion =  'SELECT DISTINCT "NombreSustanciaAdiccion" FROM "SustanciaAdiccion" ORDER BY "NombreSustanciaAdiccion" '
        queryProcedencia = 'SELECT DISTINCT "Procedencia" FROM "Radiografia" ORDER BY "Procedencia" '

        listaEnf = auxProcessList(queryEnfName,"")
        for combo in self.enfArray[3]:
            combo['values'] = tuple(listaEnf)

        listaMed = auxProcessList(queryMedName,"")
        for combo in self.medicamentoArray[3]:
            combo['values'] = tuple(listaMed)

        self.zonaCombo['values'] = tuple(auxProcessList(queryRadiZone,""))

        listaAlerg = auxProcessList(querySustanciaAlergia,"")
        for combo in self.alergiaArray[3]:
            combo['values'] = tuple(listaAlerg)

        listaAdiccion = auxProcessList(querySustanciaAdiccion,"")
        for combo in self.adiccionArray[3]:
            combo['values'] = tuple(listaAdiccion)

        self.procedenciaCombo['values'] = tuple(auxProcessList(queryProcedencia,""))


        pass

    def newWindow(self, tipo):
        t = Tkinter.Toplevel(self.parent)
        ventana = VentanaExtra.Demo(t,tipo)
        pass
    
    def execute(self):
        self.about.show()

    def plusField(self,aArray):
        n=aArray[0]
        aVariable = StringVar()
        widgetToAdd = None
        if (n == 0):
            widgetToAdd = Entry(aArray[2].interior(),textvariable = aVariable)
        else:
            widgetToAdd =ttk.Combobox(aArray[2].interior(), textvariable=aVariable,
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
    
class PrintOne:
    def __init__(self, text):
        self.text = text

    def __call__(self):
        print self.text




root = Tkinter.Tk()
demo = Demo(root)
root.mainloop()
