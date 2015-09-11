# -*- coding: cp1252 -*-
import Tkinter
import Pmw
from Tkinter import *
import ttk
from Calendar import *
import VentanaExtra
from SearchCriteria import *

import psycopg2

queryInsertRadio = 'INSERT INTO "Radiografia"("IdRadio", "Fecha", "Zona", "Procedencia", ' \
                '"Tipo", "Comentario", "RUNPaciente", "NombrePaciente") VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'

queryFiltrarPaciente = 'SELECT "Nombres","Apellidos","RUN" FROM "Paciente" '
queryAddPaciente = 'INSERT INTO "Paciente" ("Sexo", "RUN", "Nombres", "Apellidos", "FechaNac" ) ' \
                'VALUES (%s, %s, %s, %s, %s)'

class Demo:
    def __init__(self, parent):
        
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

        self.varCheckRut = IntVar()
        Checkbutton(self.group.interior(), variable=self.varCheckRut).grid(row=0,column=0)
        self.run = Label(self.group.interior(), 
            text = 'RUT:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=2)
        
        self.varCheckNombre = IntVar()
        Checkbutton(self.group.interior(), variable=self.varCheckNombre).grid(row=1,column=0)
        self.nombre = Label(self.group.interior(), 
            text = 'Nombre:')
        self.nombre.grid(row=1,column=1,sticky=W, padx=5, pady=5)

        self.nombreentry = Entry(self.group.interior())
        self.nombreentry.grid(row=1,column=2)

        self.varCheckApellidos = IntVar()
        Checkbutton(self.group.interior(), variable=self.varCheckApellidos).grid(row=2,column=0)
        self.apellidos = Label(self.group.interior(),
            text = 'Apellido:')
        self.apellidos.grid(row=2,column=1,sticky=W, padx=5, pady=5)

        self.apellidoEntry = Entry(self.group.interior())
        self.apellidoEntry.grid(row=2,column=2)


        #Button "Filtro"
        self.filtrar = Button(self.group.interior(),text="Filtrar",
                            command= self.filtrarPaciente).grid(row=2,column=3,sticky=W, padx=5, pady=5)

        self.varSexo = IntVar()
        Checkbutton(self.group.interior(), variable=self.varSexo).grid(row=3,column=0)
        self.sexo= Label(self.group.interior(), 
            text="Sexo:").grid(row=3,column=1,sticky=W, padx=5, pady=5)
        self.boolsexo = IntVar()
        self.radiobuttonm=Radiobutton(self.group.interior(), text="M", variable=self.boolsexo, value=1).grid(row=3,column=2,sticky=W)
        self.radiobuttonh=Radiobutton(self.group.interior(), text="H", variable=self.boolsexo, value=2).grid(row=3,column=2,sticky=E)

        self.varFechaNac = IntVar()
        Checkbutton(self.group.interior(), variable=self.varFechaNac).grid(row=4,column=0)
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
        self.group1 = Pmw.Group(self.page, tag_text = 'Radiografia')
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

        self.frame = Label(self.group1.interior(), 
            text = 'Frames Si es mas de uno usar (;)  :').grid(row=2,column=0,sticky=W, padx=5, pady=5)
        self.frameentry = Entry(self.group1.interior()).grid(row=2,column=1)
        
        
        self.enfermedad= Label(self.group1.interior(), text="Enfermedad:").grid(row=3,column=0,sticky=W, padx=5, pady=5)
        self.enfermedadValue = StringVar()
        self.enfermedadCombo = ttk.Combobox(self.group1.interior(), textvariable=self.enfermedadValue,
                                state='readonly')
        self.enfermedadCombo['values'] = ('Enfermedad1', 'Enfermedad2', 'Enfermedad3', 'Enfermedad4')
        self.enfermedadCombo.current(0)
        self.enfermedadCombo.grid(row=3,column=1)

        # Create and pack the dropdown ComboBox.
        self.zona= Label(self.group1.interior(), text="Zona:").grid(row=4,column=0,sticky=W, padx=5, pady=5)
        self.zonaValue = StringVar()
        self.zonaCombo = ttk.Combobox(self.group1.interior(), textvariable=self.zonaValue,
                                state='readonly')
        self.zonaCombo['values'] = ('cornsilk1', 'snow1', 'seashell1', 'antiquewhite1')
        self.zonaCombo.current(0)
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
        self.procedenciaCombo['values'] = ('Ambulatorio', 'procedencia1', 'procedencia2')
        self.procedenciaCombo.current(0)
        self.procedenciaCombo.grid(row=7,column=1)

        
        self.comentario0 = Label(self.group1.interior(), 
                text = 'Comentario:').grid(row=8,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry0 = Entry(self.group1.interior()).grid(row=8,column=1)

        


        # Add another page
        self.page1 = self.notebook.add('Antecedentes')

       # Create the "Radiografia" contents of the page.
        ##Trabajo
        self.groupTrabajo = Pmw.Group(self.page1, tag_text = 'Trabajo')
        self.groupTrabajo.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
        self.var1 = IntVar()
        Checkbutton(self.groupTrabajo.interior(), variable=self.var1).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.trabajo = Label(self.groupTrabajo.interior(), 
                text = 'Trabajo:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.trabjoentry = Entry(self.groupTrabajo.interior()).grid(row=0,column=2)

        self.buttonTrabajoplus = Button(self.groupTrabajo.interior(),text="+",
                            command= lambda: self.plusEntry(self.trabajoArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonTrabajominus = Button(self.groupTrabajo.interior(),text="-",
                            command= lambda: self.minus(self.trabajoArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ######################################################################
        

        ##Medicamentos
        self.groupMedicamentos = Pmw.Group(self.page1, tag_text = 'Medicamentos')
        self.groupMedicamentos.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
        self.var2 = IntVar()
        Checkbutton(self.groupMedicamentos.interior(), variable=self.var2).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.medicamentos= Label(self.groupMedicamentos.interior(), text="Medicamentos:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.medicamentoValue = StringVar()
        self.medicamentoCombo = ttk.Combobox(self.groupMedicamentos.interior(), textvariable=self.medicamentoValue,
                                state='readonly')
        self.medicamentoCombo['values'] = ('ibuprofeno','etc')
        self.medicamentoCombo.current(0)
        self.medicamentoCombo.grid(row=0,column=2)
        
        self.buttonMedicamentosplus = Button(self.groupMedicamentos.interior(),text="+",
                            command= lambda: self.plusCombo(self.medicamentoArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonMedicamentosminus = Button(self.groupMedicamentos.interior(),text="-",
                            command= lambda: self.minus(self.medicamentoArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        #########################################################################

        
        ##Alergia
        self.groupAlergia = Pmw.Group(self.page1, tag_text = 'Alergia')
        self.groupAlergia.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
        self.var3 = IntVar()
        Checkbutton(self.groupAlergia.interior(), variable=self.var3).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        
        self.alergia= Label(self.groupAlergia.interior(), text="Alergias:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.alergiaValue = StringVar()
        self.alergiaCombo = ttk.Combobox(self.groupAlergia.interior(), textvariable=self.alergiaValue,
                                state='readonly')
        self.alergiaCombo['values'] = ('bichos','etc')
        self.alergiaCombo.current(0)
        self.alergiaCombo.grid(row=0,column=2)

        self.buttonAlergiaplus = Button(self.groupAlergia.interior(),text="+",
                            command= lambda: self.plusCombo(self.alergiaArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonAlergiaminus = Button(self.groupAlergia.interior(),text="-",
                            command= lambda: self.minus(self.alergiaArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ##########################################################################

        
        ##Adiccion
        self.groupAdiccion = Pmw.Group(self.page1, tag_text = 'Adiccion')
        self.groupAdiccion.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        
        self.var4 = IntVar()
        Checkbutton(self.groupAdiccion.interior(), variable=self.var4).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        
        self.adiccion= Label(self.groupAdiccion.interior(), text="Adiccion:").grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.adiccionValue = StringVar()
        self.adiccionCombo = ttk.Combobox(self.groupAdiccion.interior(), textvariable=self.adiccionValue,
                                state='readonly')
        self.adiccionCombo['values'] = ('PastaBase','etc')
        self.adiccionCombo.current(0)
        self.adiccionCombo.grid(row=0,column=2)

        self.buttonAdiccionplus = Button(self.groupAdiccion.interior(),text="+",
                            command= lambda: self.plusCombo(self.adiccionArray)).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        self.buttonAdiccionminus = Button(self.groupAdiccion.interior(),text="-",
                            command= lambda: self.minus(self.adiccionArray)).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ########################################################################

        
        self.comentario1 = Label(self.groupAdiccion.interior(), 
                text = 'Comentario:').grid(row=4,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry1 = Entry(self.groupAdiccion.interior()).grid(row=4,column=1)
        #########################################################################
        #Declarar arreglos para multiplicar basuras
        #########################################################################
        #Obj1.grid_forget()
        #Agrupar cada cosa por su propio grupo
        self.medicamentoVar=[self.medicamentoValue]
        self.alergiaVar=[self.alergiaValue]
        self.adiccionVar=[self.adiccionValue]
        

        self.trabajoArray=[0,0,self.groupTrabajo,self.trabjoentry]
        self.medicamentoArray=[1,self.medicamentoVar,self.groupMedicamentos,self.medicamentoCombo]
        self.alergiaArray=[2,self.alergiaVar,self.groupAlergia,self.alergiaCombo]
        self.adiccionArray=[3,self.adiccionVar,self.groupAdiccion,self.adiccionCombo]



        #########################################################################
        

        self.group3 = Pmw.Group(self.page1, tag_text = 'Intervenciones')
        self.group3.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.var5 = IntVar()
        Checkbutton(self.group3.interior(), variable=self.var5).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        

        self.fechaint = Label(self.group3.interior(), 
                text = 'Fecha:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.varF2 = StringVar()
        self.varF2.set('Today')
        self.fechaintdate= Label(self.group3.interior(), textvariable = self.varF2).grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.fechaintbutton = Button(self.group3.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF2)).grid(row=0,column=2,sticky=E, padx=5, pady=5)

        self.nombreop = Label(self.group3.interior(), 
                text = 'Nombre Intervencion:').grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.nombreopentry = Entry(self.group3.interior()).grid(row=1,column=2)

        self.doc = Label(self.group3.interior(), 
                text = 'Doctor:').grid(row=2,column=1,sticky=W, padx=5, pady=5)
        self.docentry = Entry(self.group3.interior()).grid(row=2,column=2)

        self.notebook.setnaturalsize()

        self.statusValue= StringVar()
        self.statusValue.set("Status:")
        self.status = Label(parent,textvariable=self.statusValue).pack()




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


        self.checkboxes=[self.var1,self.var2,self.var3,self.var4,self.var5]

        self.actualizaListas()

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
        print 'You play to be GOD'
        #filtrar por los checkboxes
        #self.var1,self.var2,self.var3,self.var4,self.var5 son los Tkinter.IntVar() :D
        #hacer el filtro de que se crea
        for var in self.checkboxes:
            print var.get()

        params = (str(self.idsentry.get()),str(self.varF1.get()),str(self.zonaValue.get()),str(self.procedenciaValue.get()),
                  str(self.tipoValue.get()),str("Esto es comentaro")
                  ,str(self.pacienteValue.get().split(",")[1]),str(self.pacienteValue.get().split(",")[0]),)
        try:
            askDb(queryInsertRadio,params)
        except Exception, e:
            self.statusValue.set("Status: "+str(e))


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
            whereString += '"Nombres" = %s AND '
            params = params + (str(varNombre),)
        if (varApellido != ''):
            whereString += '"Apellidos" = %s AND '
            params = params + (str(varApellido),)
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

        if(len(listRes) != 0):
            for i in range(len(listRes)):
                listRes[i] = listRes[i][0]+","+str(listRes[i][1])
            self.pacienteCombo['values'] = tuple(listRes)
            self.pacienteCombo.current(0)

    def getParamsPaciente(self):
        varSexo = 'M'
        if self.varSexo.get():
            if self.boolsexo.get() == 1:
                varSexo = 'H'
        varRun = self.runentry.get().strip()
        varNombre = self.nombreentry.get().strip()
        varApellido = self.apellidoEntry.get().strip()
        varFecha = self.varF0.get().strip()
        print "Comienzo filtro y update de ComboBox"
        print "Agregando con rut ",varRun
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

        query1 =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
        query2 =  'SELECT "NombreMedicamento" FROM "Medicamento" '
        query3 =  'SELECT DISTINCT "Zona" FROM "Radiografia" ORDER BY "Zona" '
        query4 =  'SELECT DISTINCT "NombreSustancia" FROM "Sustancia" ORDER BY "NombreSustancia" '
        query5 = 'SELECT DISTINCT "Procedencia" FROM "Radiografia" ORDER BY "Procedencia" '

        self.enfermedadCombo['values'] = tuple(auxProcessList(query1,""))

        self.medicamentoCombo['values'] = tuple(auxProcessList(query2,""))

        self.zonaCombo['values'] = tuple(auxProcessList(query3,""))

        self.alergiaCombo['values'] = tuple(auxProcessList(query4,""))

        self.adiccionCombo['values'] = tuple(auxProcessList(query4,""))

        self.procedenciaCombo['values'] = tuple(auxProcessList(query5,""))

        query6 = 'SELECT "Nombre","RUN" FROM "Paciente" ORDER BY RANDOM() LIMIT 5 '
        self.pacienteCombo['values'] = tuple(auxProcessList(query6,""))

        pass

    def newWindow(self, tipo):
        t = Tkinter.Toplevel(self.parent)
        ventana = VentanaExtra.Demo(t,tipo)
        pass
    
    def execute(self):
        self.about.show()

    def plusCombo(self,aArray):
        n=aArray[0]
        aVariable = StringVar()
        aCombo =ttk.Combobox(aArray[2].interior(), textvariable=aVariable,
                                state='readonly')
        #######Relleno segun tipo, puse n =0 de pajero, seguramente tendre que poner en [0] el tipo
        #####0 = trabajo(no se usa)
        #####1 = medicamento
        #####2 = alergia
        #####3 = adiccion
        
        if (n==1):
            aCombo['values'] = ('ibuprofeno', 'aspirina', 'etc')
        if (n==2):
            aCombo['values'] = ('queso', 'bichos', 'plata')
        if (n==3):
            aCombo['values'] = ('pastaBase','Alcohol','asdasd')
        aCombo.current(0)
        aCombo.grid(row=len(aArray)-3,column=2, padx=5, pady=5)
        aArray.append(aCombo)
        aArray[1].append(aVariable)
        pass
         


    def plusEntry(self,aArray):
        aEntry = Entry(aArray[2].interior())
        aEntry.grid(row=len(aArray)-3,column=2, padx=5, pady=5)
        aArray.append(aEntry)
        pass
        


    def minus(self,aArray):
        if (aArray[1]==0):
            aArray[1].pop()
        disable = aArray.pop()
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
